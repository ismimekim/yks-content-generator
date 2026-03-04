"use client";

import { useState, useCallback, useRef, useEffect } from "react";
import type { Message, Platform, Language, StyleSource } from "@/lib/types";

export interface ChatState {
  messages: Message[];
  isLoading: boolean;
  error: string | null;
}

export function useChat(
  platform: Platform,
  contentType: string,
  language: Language,
  styleSource: StyleSource
) {
  const [chatState, setChatState] = useState<ChatState>({
    messages: [],
    isLoading: false,
    error: null,
  });
  const messagesRef = useRef<Message[]>([]);

  useEffect(() => {
    messagesRef.current = chatState.messages;
  }, [chatState.messages]);

  const sendMessage = useCallback(
    async (content: string, trends?: string[]) => {
      const userMessage: Message = {
        id: crypto.randomUUID(),
        role: "user",
        content,
        timestamp: Date.now(),
      };

      setChatState((prev) => ({
        ...prev,
        messages: [...prev.messages, userMessage],
        isLoading: true,
        error: null,
      }));

      try {
        const outboundMessages = [...messagesRef.current, userMessage];

        const response = await fetch("/api/chat", {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({
            messages: outboundMessages,
            platform,
            contentType,
            language,
            styleSource,
            trends,
          }),
        });

        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }

        const reader = response.body?.getReader();
        const decoder = new TextDecoder();

        if (!reader) {
          throw new Error("No response body");
        }

        let assistantContent = "";
        let sseBuffer = "";
        const assistantMessage: Message = {
          id: crypto.randomUUID(),
          role: "assistant",
          content: "",
          timestamp: Date.now(),
        };

        // Add empty assistant message immediately
        setChatState((prev) => ({
          ...prev,
          messages: [...prev.messages, assistantMessage],
        }));

        const processSseBuffer = (flush = false) => {
          const events = sseBuffer.split("\n\n");
          if (!flush) {
            sseBuffer = events.pop() ?? "";
          } else {
            sseBuffer = "";
          }

          for (const event of events) {
            const dataLines = event
              .split("\n")
              .filter((line) => line.startsWith("data: "))
              .map((line) => line.slice(6).trim());

            for (const data of dataLines) {
              if (!data || data === "[DONE]") {
                continue;
              }

              try {
                const parsed = JSON.parse(data);
                if (parsed.text) {
                  assistantContent += parsed.text;

                  setChatState((prev) => ({
                    ...prev,
                    messages: prev.messages.map((msg) =>
                      msg.id === assistantMessage.id
                        ? { ...msg, content: assistantContent }
                        : msg
                    ),
                  }));
                }
              } catch {
                // Intentionally ignore partial/incomplete JSON chunks.
              }
            }
          }
        };

        while (true) {
          const { done, value } = await reader.read();
          if (done) break;

          sseBuffer += decoder.decode(value, { stream: true });
          processSseBuffer(false);
        }

        sseBuffer += decoder.decode();
        processSseBuffer(true);

        setChatState((prev) => ({
          ...prev,
          isLoading: false,
        }));
      } catch (error) {
        console.error("Chat error:", error);
        setChatState((prev) => ({
          ...prev,
          isLoading: false,
          error: error instanceof Error ? error.message : "Failed to send message",
        }));
      }
    },
    [platform, contentType, language, styleSource]
  );

  const clearMessages = useCallback(() => {
    setChatState({
      messages: [],
      isLoading: false,
      error: null,
    });
  }, []);

  const setMessages = useCallback((messages: Message[]) => {
    setChatState((prev) => ({
      ...prev,
      messages,
    }));
  }, []);

  return {
    messages: chatState.messages,
    isLoading: chatState.isLoading,
    error: chatState.error,
    sendMessage,
    clearMessages,
    setMessages,
  };
}
