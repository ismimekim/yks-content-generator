"use client";

import { Badge } from "@/components/ui/badge";
import {
  Select,
  SelectContent,
  SelectItem,
  SelectTrigger,
  SelectValue,
} from "@/components/ui/select";
import {
  PLATFORMS,
  CONTENT_TYPES,
  LANGUAGES,
  STYLE_SOURCES,
  type Platform,
  type Language,
  type StyleSource,
} from "@/lib/types";
import { Search, Loader2 } from "lucide-react";
import { Button } from "@/components/ui/button";

interface ConfigPanelProps {
  platform: Platform;
  contentType: string;
  language: Language;
  styleSource: StyleSource;
  onPlatformChange: (platform: Platform) => void;
  onContentTypeChange: (contentType: string) => void;
  onLanguageChange: (language: Language) => void;
  onStyleSourceChange: (style: StyleSource) => void;
  onSearchTrends: () => void;
  isSearching?: boolean;
  trends?: string[];
}

export function ConfigPanel({
  platform,
  contentType,
  language,
  styleSource,
  onPlatformChange,
  onContentTypeChange,
  onLanguageChange,
  onStyleSourceChange,
  onSearchTrends,
  isSearching,
  trends,
}: ConfigPanelProps) {
  const contentTypes = CONTENT_TYPES[platform] || [];

  return (
    <div className="border-b bg-background/95 backdrop-blur supports-[backdrop-filter]:bg-background/60">
      <div className="max-w-3xl mx-auto px-4 py-2">
        <div className="flex flex-wrap items-center gap-2">
          {/* Platform Selector */}
          <Select value={platform} onValueChange={(v) => onPlatformChange(v as Platform)}>
            <SelectTrigger className="w-[140px] h-8 text-xs">
              <SelectValue placeholder="Platform" />
            </SelectTrigger>
            <SelectContent>
              {PLATFORMS.map((p) => (
                <SelectItem key={p.value} value={p.value}>
                  {p.label}
                </SelectItem>
              ))}
            </SelectContent>
          </Select>

          {/* Content Type Selector */}
          <Select value={contentType} onValueChange={onContentTypeChange}>
            <SelectTrigger className="w-[130px] h-8 text-xs">
              <SelectValue placeholder="İçerik Türü" />
            </SelectTrigger>
            <SelectContent>
              {contentTypes.map((ct) => (
                <SelectItem key={ct.value} value={ct.value}>
                  {ct.label}
                </SelectItem>
              ))}
            </SelectContent>
          </Select>

          {/* Language Toggle */}
          <div className="flex border rounded-md h-8">
            {LANGUAGES.map((lang) => (
              <button
                key={lang.value}
                onClick={() => onLanguageChange(lang.value)}
                className={`px-3 text-xs font-medium transition-colors ${
                  language === lang.value
                    ? "bg-primary text-primary-foreground"
                    : "bg-transparent text-muted-foreground hover:text-foreground"
                } ${lang.value === "tr" ? "rounded-l-md" : "rounded-r-md"}`}
              >
                {lang.label}
              </button>
            ))}
          </div>

          {/* Style Source */}
          <Select
            value={styleSource}
            onValueChange={(v) => onStyleSourceChange(v as StyleSource)}
          >
            <SelectTrigger className="w-[190px] h-8 text-xs">
              <SelectValue placeholder="Stil Kaynağı" />
            </SelectTrigger>
            <SelectContent>
              {STYLE_SOURCES.map((style) => (
                <SelectItem key={style.value} value={style.value}>
                  {style.label}
                </SelectItem>
              ))}
            </SelectContent>
          </Select>

          {/* Search Trends Button */}
          <Button
            variant="outline"
            size="sm"
            className="h-8 gap-1 text-xs"
            onClick={onSearchTrends}
            disabled={isSearching}
          >
            {isSearching ? (
              <Loader2 className="w-3 h-3 animate-spin" />
            ) : (
              <Search className="w-3 h-3" />
            )}
            Trend Ara
          </Button>

          {/* Active Trends */}
          {trends && trends.length > 0 && (
            <div className="flex gap-1 flex-wrap">
              {trends.slice(0, 3).map((trend, i) => (
                <Badge key={i} variant="secondary" className="text-xs">
                  {trend.length > 20 ? trend.substring(0, 20) + "..." : trend}
                </Badge>
              ))}
              {trends.length > 3 && (
                <Badge variant="outline" className="text-xs">
                  +{trends.length - 3}
                </Badge>
              )}
            </div>
          )}
        </div>
      </div>
    </div>
  );
}
