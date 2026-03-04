"use client";

import { useState, useEffect, useCallback } from "react";
import type {
  ChatSession,
  Message,
  Platform,
  Language,
  StyleSource,
} from "@/lib/types";

const STORAGE_KEY = "odaklan-sm-chats";

export function useChatHistory() {
  const [sessions, setSessions] = useState<ChatSession[]>([]);
  const [activeSessionId, setActiveSessionId] = useState<string | null>(null);

  // Load sessions from localStorage
  useEffect(() => {
    try {
      const stored = localStorage.getItem(STORAGE_KEY);
      if (stored) {
        const parsed = JSON.parse(stored) as ChatSession[];
        setSessions(parsed);
        if (parsed.length > 0) {
          setActiveSessionId(parsed[0].id);
        }
      }
    } catch (error) {
      console.error("Failed to load chat history:", error);
    }
  }, []);

  // Save sessions to localStorage
  const saveSessions = useCallback((updatedSessions: ChatSession[]) => {
    setSessions(updatedSessions);
    try {
      localStorage.setItem(STORAGE_KEY, JSON.stringify(updatedSessions));
    } catch (error) {
      console.error("Failed to save chat history:", error);
    }
  }, []);

  // Create new session
  const createSession = useCallback(
    (
      platform?: Platform,
      language: Language = "tr",
      styleSource: StyleSource = "oguz_usta"
    ): string => {
      const newSession: ChatSession = {
        id: crypto.randomUUID(),
        title: "Yeni Sohbet",
        messages: [],
        platform,
        language,
        styleSource,
        createdAt: Date.now(),
        updatedAt: Date.now(),
      };

      const updated = [newSession, ...sessions];
      saveSessions(updated);
      setActiveSessionId(newSession.id);
      return newSession.id;
    },
    [sessions, saveSessions]
  );

  // Update session messages
  const updateSessionMessages = useCallback(
    (sessionId: string, messages: Message[]) => {
      const updated = sessions.map((s) => {
        if (s.id === sessionId) {
          // Auto-generate title from first user message
          let title = s.title;
          if (title === "Yeni Sohbet" && messages.length > 0) {
            const firstUserMsg = messages.find((m) => m.role === "user");
            if (firstUserMsg) {
              title =
                firstUserMsg.content.length > 40
                  ? firstUserMsg.content.substring(0, 40) + "..."
                  : firstUserMsg.content;
            }
          }

          return {
            ...s,
            title,
            messages,
            updatedAt: Date.now(),
          };
        }
        return s;
      });

      saveSessions(updated);
    },
    [sessions, saveSessions]
  );

  // Update session config
  const updateSessionConfig = useCallback(
    (
      sessionId: string,
      config: {
        platform?: Platform;
        contentType?: string;
        language?: Language;
        styleSource?: StyleSource;
      }
    ) => {
      const updated = sessions.map((s) =>
        s.id === sessionId ? { ...s, ...config, updatedAt: Date.now() } : s
      );
      saveSessions(updated);
    },
    [sessions, saveSessions]
  );

  // Delete session
  const deleteSession = useCallback(
    (sessionId: string) => {
      const updated = sessions.filter((s) => s.id !== sessionId);
      saveSessions(updated);

      if (activeSessionId === sessionId) {
        setActiveSessionId(updated.length > 0 ? updated[0].id : null);
      }
    },
    [sessions, saveSessions, activeSessionId]
  );

  // Get active session
  const activeSession = sessions.find((s) => s.id === activeSessionId) || null;

  return {
    sessions,
    activeSession,
    activeSessionId,
    setActiveSessionId,
    createSession,
    updateSessionMessages,
    updateSessionConfig,
    deleteSession,
  };
}
