"use client";

import { useEffect, useRef, useState } from "react";
import { MessageBubble } from "./MessageBubble";
import { ChatInput } from "./ChatInput";
import type { Message } from "@/lib/types";

interface ChatContainerProps {
  messages: Message[];
  isLoading: boolean;
  onSend: (message: string) => void;
}

export function ChatContainer({ messages, isLoading, onSend }: ChatContainerProps) {
  const scrollRef = useRef<HTMLDivElement>(null);
  const scrollContainerRef = useRef<HTMLDivElement>(null);
  const [autoScroll, setAutoScroll] = useState(true);

  // Auto-scroll to bottom only if user hasn't scrolled up
  useEffect(() => {
    if (scrollRef.current && autoScroll) {
      scrollRef.current.scrollIntoView({ behavior: "smooth" });
    }
  }, [messages, autoScroll]);

  // Detect if user scrolls up manually
  const handleScroll = () => {
    const el = scrollContainerRef.current;
    if (el) {
      const isNearBottom = el.scrollHeight - el.scrollTop - el.clientHeight < 150;
      setAutoScroll(isNearBottom);
    }
  };

  return (
    <div className="flex flex-col h-full">
      {/* Messages area with manual scroll control */}
      <div
        ref={scrollContainerRef}
        onScroll={handleScroll}
        className="flex-1 overflow-y-auto"
      >
        <div className="max-w-3xl mx-auto pb-4">
          {messages.length === 0 ? (
            <div className="flex items-center justify-center h-full min-h-[300px]">
              <div className="text-center space-y-4">
                <div className="text-4xl">👋</div>
                <h2 className="text-2xl font-bold">Merhaba!</h2>
                <p className="text-muted-foreground">
                  Sosyal medya içerik üretiminde uzman AI agent&apos;ım.
                  <br />
                  Platform, içerik türü ve dil seçtikten sonra bana ne tür içerik istediğini anlat.
                </p>
              </div>
            </div>
          ) : (
            messages.map((message) => (
              <MessageBubble key={message.id} message={message} />
            ))
          )}
          {isLoading && (
            <div className="flex gap-3 px-4 py-4">
              <div className="flex-shrink-0 w-8 h-8 rounded-full bg-gradient-to-br from-violet-500 to-fuchsia-500 flex items-center justify-center">
                <div className="w-4 h-4" />
              </div>
              <div className="flex-1">
                <div className="flex items-center gap-2 mb-1">
                  <span className="text-sm font-medium">SM Agent</span>
                </div>
                <div className="flex gap-1">
                  <div className="w-2 h-2 bg-muted-foreground/30 rounded-full animate-pulse" />
                  <div className="w-2 h-2 bg-muted-foreground/30 rounded-full animate-pulse delay-100" />
                  <div className="w-2 h-2 bg-muted-foreground/30 rounded-full animate-pulse delay-200" />
                </div>
              </div>
            </div>
          )}
          <div ref={scrollRef} />
        </div>
      </div>

      {/* Scroll to bottom button when not auto-scrolling */}
      {!autoScroll && messages.length > 0 && (
        <button
          onClick={() => {
            setAutoScroll(true);
            scrollRef.current?.scrollIntoView({ behavior: "smooth" });
          }}
          className="absolute bottom-24 right-8 z-10 bg-primary text-primary-foreground rounded-full p-2 shadow-lg hover:opacity-90 transition-opacity"
        >
          ↓
        </button>
      )}

      {/* Input */}
      <ChatInput onSend={onSend} isLoading={isLoading} />
    </div>
  );
}
