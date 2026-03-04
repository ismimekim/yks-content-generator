// ========================================
// LINGUISTIC PATTERNS (From 100 Shorts Analysis)
// ========================================

export const LINGUISTIC_PATTERNS = {
  // Top 50 words by frequency
  topWords: {
  "bir": 211,
  "ve": 97,
  "bu": 90,
  "\u00e7ok": 80,
  "de": 72,
  "g\u00f6r\u00fc\u015f\u00fcr\u00fcz": 68,
  "o": 64,
  "yani": 64,
  "yok": 61,
  "var": 60,
  "da": 57,
  "ne": 56,
  "i\u00e7in": 56,
  "m\u0131": 48,
  "ben": 46,
  "daha": 44,
  "mi": 44,
  "her": 42,
  "ama": 39,
  "tyt": 39,
  "tane": 39,
  "zaman": 36,
  "en": 36,
  "ya": 35,
  "\u015fey": 33,
  "soru": 32,
  "de\u011fil": 32,
  "iyi": 31,
  "ders": 31,
  "nas\u0131l": 30,
  "kadar": 29,
  "\u015fu": 29,
  "ki": 29,
  "tekrar": 28,
  "g\u00fcn": 28,
  "zaten": 27,
  "sonra": 27,
  "kitap": 27,
  "sen": 25,
  "abi": 25,
  "gibi": 24,
  "hoca": 23,
  "3": 23,
  "zor": 22,
  "veya": 22,
  "ayt": 21,
  "iki": 21,
  "b\u00f6yle": 20,
  "ancak": 20,
  "konuyu": 19
},

  // Sentence templates (extracted from real data)
  sentenceTemplates: [
    "[Iddia]. Yani [açıklama].",
    "Peki [soru]? [Cevap].",
    "[Tavsiye]. Şunu yap: [Eylem].",
  ],

  // Flow connectors by position
  flowConnectors: {
    hookToAmplify: ['Yani...', 'Anlayacağınız...'],
    amplifyToAgitate: ['Peki...', 'Fakat...'],
    agitateToSolve: ['Şunu yap...', 'Önce...', 'Sonra...'],
    solveToClose: ['Görüşürüz', 'Seviliyorsunuz'],
  },
};

// Voice calibration thresholds
export const VOICE_THRESHOLDS = {
  avgSentenceLength: 77.0,
  medianSentenceLength: 69,
  targetLengthRange: [8, 25],
};