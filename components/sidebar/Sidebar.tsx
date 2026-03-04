"use client";

import { cn } from "@/lib/utils";
import { Button } from "@/components/ui/button";
import { ScrollArea } from "@/components/ui/scroll-area";
import { Separator } from "@/components/ui/separator";
import { ThemeToggle } from "@/components/theme/ThemeToggle";
import {
  Plus,
  MessageSquare,
  Trash2,
  PanelLeftClose,
  PanelLeftOpen,
} from "lucide-react";
import type { ChatSession } from "@/lib/types";

interface SidebarProps {
  sessions: ChatSession[];
  activeSessionId: string | null;
  onSelectSession: (id: string) => void;
  onNewChat: () => void;
  onDeleteSession: (id: string) => void;
  isOpen: boolean;
  onToggle: () => void;
}

export function Sidebar({
  sessions,
  activeSessionId,
  onSelectSession,
  onNewChat,
  onDeleteSession,
  isOpen,
  onToggle,
}: SidebarProps) {
  return (
    <>
      {/* Mobile overlay */}
      {isOpen && (
        <div
          className="fixed inset-0 bg-black/50 z-40 md:hidden"
          onClick={onToggle}
        />
      )}

      {/* Sidebar */}
      <div
        className={cn(
          "fixed md:relative z-50 h-full bg-muted/50 border-r transition-all duration-300",
          isOpen ? "w-64" : "w-0 md:w-0"
        )}
      >
        {isOpen && (
          <div className="flex flex-col h-full w-64">
            {/* Header */}
            <div className="p-3 flex items-center justify-between">
              <h1 className="font-bold text-lg bg-gradient-to-r from-violet-500 to-fuchsia-500 bg-clip-text text-transparent">
                SM Agent
              </h1>
              <div className="flex items-center gap-1">
                <ThemeToggle />
                <Button variant="ghost" size="icon" className="h-8 w-8" onClick={onToggle}>
                  <PanelLeftClose className="w-4 h-4" />
                </Button>
              </div>
            </div>

            {/* New Chat Button */}
            <div className="px-3 pb-2">
              <Button
                onClick={onNewChat}
                className="w-full gap-2"
                variant="outline"
              >
                <Plus className="w-4 h-4" />
                Yeni Sohbet
              </Button>
            </div>

            <Separator />

            {/* Chat Sessions */}
            <ScrollArea className="flex-1 px-2 py-2">
              {sessions.length === 0 ? (
                <p className="text-xs text-muted-foreground text-center py-4">
                  Henüz sohbet yok
                </p>
              ) : (
                <div className="space-y-1">
                  {sessions.map((session) => (
                    <div
                      key={session.id}
                      className={cn(
                        "group flex items-center gap-2 px-3 py-2 rounded-lg cursor-pointer text-sm transition-colors",
                        session.id === activeSessionId
                          ? "bg-primary/10 text-primary"
                          : "hover:bg-muted text-foreground"
                      )}
                      onClick={() => onSelectSession(session.id)}
                    >
                      <MessageSquare className="w-4 h-4 flex-shrink-0" />
                      <span className="truncate flex-1">{session.title}</span>
                      <button
                        onClick={(e) => {
                          e.stopPropagation();
                          onDeleteSession(session.id);
                        }}
                        className="opacity-0 group-hover:opacity-100 transition-opacity p-1 rounded hover:bg-destructive/10 hover:text-destructive"
                      >
                        <Trash2 className="w-3 h-3" />
                      </button>
                    </div>
                  ))}
                </div>
              )}
            </ScrollArea>

            {/* Footer */}
            <Separator />
            <div className="p-3">
              <p className="text-xs text-muted-foreground text-center">
                🦉 Baykuş Mentörlük
              </p>
            </div>
          </div>
        )}
      </div>

      {/* Toggle button when closed */}
      {!isOpen && (
        <Button
          variant="ghost"
          size="icon"
          className="fixed top-3 left-3 z-30 h-8 w-8"
          onClick={onToggle}
        >
          <PanelLeftOpen className="w-4 h-4" />
        </Button>
      )}
    </>
  );
}
