/**
 * Intent Detection System for YKS Content Generator
 * 
 * Detects user intent from message to select appropriate response mode:
 * - PRODUCE_CONTENT: Generate actual content (Oğuz Usta SHORT format)
 * - GET_STRATEGY: Provide strategic advice/analysis (consultant mode)
 * - GET_IDEAS: Suggest content ideas/angles (list format OK)
 */

export enum UserIntent {
  PRODUCE_CONTENT = "produce", // "hazırla", "üret", "yaz"
  GET_STRATEGY = "strategy",    // "fikrin var mı?", "ne düşünüyorsun"
  GET_IDEAS = "ideas",          // "öner", "angle", "seçenek"
}

/**
 * PromptMode type (matches lib/prompts.ts)
 */
export type PromptMode = "angles" | "direct";

export interface IntentDetectionResult {
  intent: UserIntent;
  confidence: number; // 0-1
  signals: string[];  // matched keywords
}

/**
 * Turkish intent signals for each mode
 */
const INTENT_SIGNALS = {
  [UserIntent.PRODUCE_CONTENT]: [
    "hazırla", "üret", "yaz", "lazım", "ihtiyacım var",
    "oluştur", "yap", "script", "içerik", "caption",
    "metin", "post", "reel", "short"
  ],
  [UserIntent.GET_STRATEGY]: [
    "fikrin var mı", "ne düşünüyorsun", "değerlendir",
    "nasıl buldun", "objektif değerlendir", "analiz et",
    "geliştirme alanları", "iyileştir"
  ],
  [UserIntent.GET_IDEAS]: [
    "öner", "angle", "seçenek", "alternatif", "başka ne",
    "farklı yaklaşım", "versiyon", "çıkarım", "idea"
  ],
};

/**
 * Detect user intent from message
 * 
 * Priority: PRODUCE_CONTENT > GET_STRATEGY > GET_IDEAS
 * (produce has highest priority to avoid confusion)
 */
export function detectIntent(message: string): IntentDetectionResult {
  const lowerMessage = message.toLowerCase().normalize('NFKD');
  
  // Count matches for each intent
  const scores: { [key: string]: number } = {};
  const matchedSignals: { [key: string]: string[] } = {};
  
  for (const [intent, signals] of Object.entries(INTENT_SIGNALS)) {
    scores[intent] = 0;
    matchedSignals[intent] = [];
    
    for (const signal of signals) {
      if (lowerMessage.includes(signal)) {
        scores[intent]++;
        matchedSignals[intent].push(signal);
      }
    }
  }
  
  // Priority order
  const priorityOrder = [UserIntent.PRODUCE_CONTENT, UserIntent.GET_STRATEGY, UserIntent.GET_IDEAS];
  
  // Find highest priority intent with matches
  for (const intent of priorityOrder) {
    if (scores[intent] > 0) {
      return {
        intent: intent as UserIntent,
        confidence: Math.min(scores[intent] * 0.3, 1),
        signals: matchedSignals[intent],
      };
    }
  }
  
  // Default: PRODUCE_CONTENT
  return {
    intent: UserIntent.PRODUCE_CONTENT,
    confidence: 0.5,
    signals: ["default"],
  };
}

/**
 * Get prompt mode based on intent
 * Maps UserIntent to PromptMode ("direct" | "angles")
 *
 * PRODUCE_CONTENT → "direct" (produce the content directly)
 * GET_STRATEGY/GET_IDEAS → "angles" (provide strategic angles/options)
 */
export function getPromptMode(intent: UserIntent): PromptMode {
  switch (intent) {
    case UserIntent.PRODUCE_CONTENT:
      return "direct"; // Produce content directly (SHORT format)
    case UserIntent.GET_STRATEGY:
    case UserIntent.GET_IDEAS:
      return "angles"; // Provide strategic angles/options
  }
}

/**
 * Should enforce SHORT format constraints?
 */
export function shouldEnforceShortFormat(intent: UserIntent): boolean {
  return intent === UserIntent.PRODUCE_CONTENT;
}

/**
 * Should allow list format?
 */
export function shouldAllowListFormat(intent: UserIntent): boolean {
  return intent !== UserIntent.PRODUCE_CONTENT;
}

/**
 * Should allow meta-talk?
 */
export function shouldAllowMetaTalk(intent: UserIntent): boolean {
  return intent !== UserIntent.PRODUCE_CONTENT;
}
