"use client";

import { useState, useEffect, useCallback, useRef } from "react";
import { Sidebar } from "@/components/sidebar/Sidebar";
import { ChatContainer } from "@/components/chat/ChatContainer";
import { ConfigPanel } from "@/components/config/ConfigPanel";
import { useChat } from "@/hooks/useChat";
import { useChatHistory } from "@/hooks/useChatHistory";
import type { Platform, Language, StyleSource } from "@/lib/types";

export default function HomePage() {
  const [sidebarOpen, setSidebarOpen] = useState(true);
  const [platform, setPlatform] = useState<Platform>("instagram");
  const [contentType, setContentType] = useState<string>("post");
  const [language, setLanguage] = useState<Language>("tr");
  const [styleSource, setStyleSource] = useState<StyleSource>("oguz_usta");
  const [trends, setTrends] = useState<string[] | undefined>();
  const [isSearching, setIsSearching] = useState(false);

  // Refs to prevent infinite loops
  const isLoadingSession = useRef(false);
  const initializedRef = useRef(false);

  const {
    sessions,
    activeSession,
    activeSessionId,
    setActiveSessionId,
    createSession,
    updateSessionMessages,
    updateSessionConfig,
    deleteSession,
  } = useChatHistory();

  const { messages, isLoading, sendMessage, clearMessages, setMessages } =
    useChat(platform, contentType, language, styleSource);

  // Initialize first session (only once)
  useEffect(() => {
    if (!initializedRef.current && sessions.length === 0) {
      initializedRef.current = true;
      createSession(platform, language, styleSource);
    } else if (!initializedRef.current && sessions.length > 0) {
      initializedRef.current = true;
    }
  }, [sessions.length]);

  // Load active session messages when session changes
  useEffect(() => {
    if (activeSession && !isLoadingSession.current) {
      isLoadingSession.current = true;
      setMessages(activeSession.messages);
      setPlatform(activeSession.platform || "instagram");
      setLanguage(activeSession.language || "tr");
      setStyleSource(activeSession.styleSource || "oguz_usta");
      // Reset after a tick
      setTimeout(() => {
        isLoadingSession.current = false;
      }, 100);
    }
  }, [activeSessionId]);

  // Save messages to history when they change (but not during session loading)
  useEffect(() => {
    if (activeSessionId && messages.length > 0 && !isLoadingSession.current) {
      updateSessionMessages(activeSessionId, messages);
    }
  }, [messages]);

  // Update content type when platform changes
  useEffect(() => {
    const contentTypesMap: Record<string, string[]> = {
      instagram: ["post", "story", "reel", "carousel", "igtv"],
      tiktok: ["video", "caption", "hashtags"],
      twitter: ["tweet", "thread", "poll"],
      youtube: ["title", "description", "script", "thumbnail"],
      linkedin: ["post", "article", "carousel"],
      facebook: ["post", "story", "reel"],
      pinterest: ["pin", "idea-pin"],
      threads: ["thread", "post"],
      snapchat: ["snap", "story"],
    };

    const types = contentTypesMap[platform] || ["post"];
    if (!types.includes(contentType)) {
      setContentType(types[0]);
    }
  }, [platform]);

  // Save config changes (debounced via ref check)
  useEffect(() => {
    if (activeSessionId && !isLoadingSession.current) {
      updateSessionConfig(activeSessionId, { platform, language, styleSource });
    }
  }, [platform, language, styleSource]);

  const handleSendMessage = useCallback(
    async (content: string) => {
      await sendMessage(content, trends);
    },
    [sendMessage, trends]
  );

  const handleNewChat = useCallback(() => {
    clearMessages();
    setTrends(undefined);
    createSession(platform, language, styleSource);
  }, [clearMessages, createSession, platform, language, styleSource]);

  const handleSelectSession = useCallback(
    (id: string) => {
      clearMessages();
      setActiveSessionId(id);
    },
    [clearMessages, setActiveSessionId]
  );

  const handleDeleteSession = useCallback(
    (id: string) => {
      if (id === activeSessionId) {
        clearMessages();
      }
      deleteSession(id);
    },
    [activeSessionId, clearMessages, deleteSession]
  );

  const handleSearchTrends = useCallback(async () => {
    setIsSearching(true);
    try {
      const response = await fetch("/api/search", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          query: `${platform} social media content trends`,
          platform,
        }),
      });

      if (response.ok) {
        const data = await response.json();
        setTrends(data.trends || []);
      } else {
        console.error("Search API returned error:", response.status);
      }
    } catch (error) {
      console.error("Failed to search trends:", error);
    } finally {
      setIsSearching(false);
    }
  }, [platform]);

  return (
    <div className="flex h-screen overflow-hidden">
      <Sidebar
        sessions={sessions}
        activeSessionId={activeSessionId}
        onSelectSession={handleSelectSession}
        onNewChat={handleNewChat}
        onDeleteSession={handleDeleteSession}
        isOpen={sidebarOpen}
        onToggle={() => setSidebarOpen(!sidebarOpen)}
      />

      <div className="flex-1 flex flex-col min-w-0">
        <ConfigPanel
          platform={platform}
          contentType={contentType}
          language={language}
          styleSource={styleSource}
          onPlatformChange={setPlatform}
          onContentTypeChange={setContentType}
          onLanguageChange={setLanguage}
          onStyleSourceChange={setStyleSource}
          onSearchTrends={handleSearchTrends}
          isSearching={isSearching}
          trends={trends}
        />

        <ChatContainer
          messages={messages}
          isLoading={isLoading}
          onSend={handleSendMessage}
        />
      </div>
    </div>
  );
}
