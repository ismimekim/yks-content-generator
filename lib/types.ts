// Platform types
export type Platform = 
  | "instagram"
  | "tiktok"
  | "twitter"
  | "youtube"
  | "linkedin"
  | "facebook"
  | "pinterest"
  | "threads"
  | "snapchat";

// Content type by platform
export type ContentType = {
  instagram: "post" | "story" | "reel" | "carousel" | "igtv";
  tiktok: "video" | "caption" | "hashtags";
  twitter: "tweet" | "thread" | "poll";
  youtube: "title" | "description" | "script" | "thumbnail";
  linkedin: "post" | "article" | "carousel";
  facebook: "post" | "story" | "reel";
  pinterest: "pin" | "idea-pin";
  threads: "thread" | "post";
  snapchat: "snap" | "story";
};

// Language
export type Language = "tr" | "en";

// Style source (persona blend)
export type StyleSource = "oguz_usta";

// Message role
export type MessageRole = "user" | "assistant";

// Chat message
export interface Message {
  id: string;
  role: MessageRole;
  content: string;
  timestamp: number;
}

// Chat session
export interface ChatSession {
  id: string;
  title: string;
  messages: Message[];
  platform?: Platform;
  contentType?: string;
  language: Language;
  styleSource?: StyleSource;
  createdAt: number;
  updatedAt: number;
}

// Chat request
export interface ChatRequest {
  messages: Message[];
  platform: Platform;
  contentType: string;
  language: Language;
  styleSource?: StyleSource;
  trends?: string[];
}

// Search request
export interface SearchRequest {
  query: string;
  platform?: Platform;
}

// Search result
export interface SearchResult {
  title: string;
  url: string;
  snippet: string;
  score?: number;
}

// Search response
export interface SearchResponse {
  results: SearchResult[];
  answer?: string;
  trends?: string[];
}

// Platform config
export const PLATFORMS: { value: Platform; label: string }[] = [
  { value: "instagram", label: "Instagram" },
  { value: "tiktok", label: "TikTok" },
  { value: "twitter", label: "X (Twitter)" },
  { value: "youtube", label: "YouTube" },
  { value: "linkedin", label: "LinkedIn" },
  { value: "facebook", label: "Facebook" },
  { value: "pinterest", label: "Pinterest" },
  { value: "threads", label: "Threads" },
  { value: "snapchat", label: "Snapchat" },
];

// Content types by platform
export const CONTENT_TYPES: Record<Platform, { value: string; label: string }[]> = {
  instagram: [
    { value: "post", label: "Post" },
    { value: "story", label: "Story" },
    { value: "reel", label: "Reel Script" },
    { value: "carousel", label: "Carousel" },
    { value: "igtv", label: "IGTV" },
  ],
  tiktok: [
    { value: "video", label: "Video Script" },
    { value: "caption", label: "Caption" },
    { value: "hashtags", label: "Hashtags" },
  ],
  twitter: [
    { value: "tweet", label: "Tweet" },
    { value: "thread", label: "Thread" },
    { value: "poll", label: "Poll" },
  ],
  youtube: [
    { value: "title", label: "Video Title" },
    { value: "description", label: "Description" },
    { value: "script", label: "Script" },
    { value: "thumbnail", label: "Thumbnail Text" },
  ],
  linkedin: [
    { value: "post", label: "Post" },
    { value: "article", label: "Article" },
    { value: "carousel", label: "Carousel" },
  ],
  facebook: [
    { value: "post", label: "Post" },
    { value: "story", label: "Story" },
    { value: "reel", label: "Reel" },
  ],
  pinterest: [
    { value: "pin", label: "Pin" },
    { value: "idea-pin", label: "Idea Pin" },
  ],
  threads: [
    { value: "thread", label: "Thread" },
    { value: "post", label: "Post" },
  ],
  snapchat: [
    { value: "snap", label: "Snap" },
    { value: "story", label: "Story" },
  ],
};

// Language options
export const LANGUAGES: { value: Language; label: string }[] = [
  { value: "tr", label: "Türkçe" },
  { value: "en", label: "English" },
];

// Style sources
export const STYLE_SOURCES: { value: StyleSource; label: string }[] = [
  { value: "oguz_usta", label: "Oğuz Usta YKS" },
];
