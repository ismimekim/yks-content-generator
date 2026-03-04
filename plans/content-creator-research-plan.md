# Content Creator Agent - Web Araştırma Planı

## 📊 Mevcut Data Analizi

### Oğuz Usta Style Profilerinden Çıkarılan İstatistikler

**SHORTS (100 video, 52k karakter):**
- `yani`: 31 kez açıklama
- `gençler`: 15 kez hitap
- `asla`/`kesinlikle`/`mutlaka`: vurgu kelimeleri
- `hiç`: 15 kez
- Emojiler: 🦉(75), 🚀(24)
- Kategoriler: Genel(73), Soru-Cevap(10), Deneme(5)

**YATAY (123 video, 2.2M karakter):**
- `yani`: 119 kez açıklama
- `gençler`: 112 kez hitap
- `hiç`: 105 kez, `kesinlikle`: 96 kez
- Geçiş kelimeleri: `peki`(78), `şimdi gençler`(75), `sonra da`(66)
- Emojiler: 🎙️(12), 🦉(2)
- Kategoriler: Genel(44), Taktik Rehber(16), Soru-Cevap(16)

---

## 🌐 Web Araştırma Konuları

### 1. GitHub: awesome-claude-skills

**Aranacak repolar:**
```
https://github.com/travisvn/awesome-claude-skills
https://github.com/BehiSecc/awesome-claude-skills
```

**Aranacak skill'ler:**
- Content writing / Content creation
- Social media management
- Copywriting
- Marketing
- Brand voice
- Persona development
- Prompt engineering for content

**Beklenen output:**
- Skill dosyalarının yapısı
- System prompt örnekleri
- Property control tanımları
- Best practice'ler

---

### 2. Social Media Content Trends (2025-2026)

**Aranacak terimler:**
```
- TikTok hook formulas 2025
- Instagram Reel viral structure
- YouTube Shorts algorithm 2025
- Social media content psychology
- Gen Z language patterns
- Short-form content optimization
- Hook completion rate
- Audience retention strategies
```

**Beklenen output:**
- Güncel hook tipleri
- Algorithm preference'ları
- Content uzunluk optimizasyonları
- Engagement artırma teknikleri

---

### 3. Content Creator System Prompts

**Aranacak terimler:**
```
- Claude content creator system prompt
- AI copywriting prompt engineering
- Social media agent persona
- Brand voice development prompt
- Educational content generation
- YKS education AI prompt
```

**Beklenen output:**
- Industry standard system prompt yapıları
- Persona tanımlama yaklaşımları
- Knowledge base entegrasyonu

---

### 4. Hook Formülasyonları

**Aranacak terimler:**
```
- Viral hook formulas TikTok
- Instagram Reel hook patterns
- YouTube Shorts click-through
- Hook psychology attention span
- First 3 seconds optimization
- Curiosity gap hooks
- Pattern interrupt content
```

**Beklenen output:**
- Hook framework'leri (AIDA, PAS, SCQA, vb.)
- Hook başarı metrikleri
- Platform spesifik hook farkları

---

### 5. Turkish Social Media Landscape

**Aranacak terimler:**
```
- Duolingo TR Instagram strategy
- Netflix TR social media
- Turkish brand voice Gen Z
- Türkiye sosyal medya trendleri 2025
- Turkish education content creators
- YKS sosyal medya stratejisi
```

**Beklenen output:**
- Türk marka voice örnekleri
- YKS içerik üreticileri analizi
- Türk Gen Z dili pattern'leri

---

## 🎯 Araştırma Sonrası Yapılacaklar

### 1. Skill Dosyası Oluşturma

```typescript
// lib/content-creator-skill.ts
export const CONTENT_CREATOR_SKILL = {
  name: "content-creator",
  version: "1.0.0",
  
  persona: {
    // TBWA × Duolingo × Oğuz Usta fusion
    role: "Elite Social Media Strategist",
    expertise: ["YKS", "Education", "Turkish Social Media", "Gen Z"],
  },
  
  hooks: {
    // Gerçek veriden + web araştırmasından
    short: [...6 tip],
    yatay: [...format],
  },
  
  knowledge: {
    // YKS know-how
    // Kaynaklar + nedenleri
    // Takvim optimizasyonu
  },
  
  output_format: {
    // Platform spesifik
    // Length guidelines
    // Emoji usage
    // Hashtag strategy
  }
};
```

### 2. Prompt System Integration

```typescript
// lib/prompts.ts - revize
import { CONTENT_CREATOR_SKILL } from "./content-creator-skill";

function buildSystemPrompt(options) {
  return [
    CORE_PERSONA,
    CONTENT_CREATOR_SKILL.persona,
    getHookSystem(options.platform, options.contentType),
    getYKSKnowledge(options.subject),
    getOutputFormat(options.platform),
  ].join("\n\n---\n\n");
}
```

### 3. Dynamic Hook Selection

```typescript
// lib/hook-selector.ts
function selectHook(context) {
  // Web araştırmasından öğrenilen:
  // - Platform preference
  // - Subject analysis
  // - Hook type matching
  // - Success probability
}
```

---

## 📋 Araştırma Checklist

| # | Konu | Durum |
|---|------|-------|
| 1 | awesome-claude-skills repolarını incele | ⏳ |
| 2 | Content creation skill dosyalarını analiz et | ⏳ |
| 3 | TikTok/Instagram/YouTube güncel trendleri | ⏳ |
| 4 | Hook formülasyon framework'leri | ⏳ |
| 5 | Türk sosyal medya marka voice analizi | ⏳ |
| 6 | Oğuz Usta data'sı ile harmanlama | ⏳ |
| 7 | System prompt final taslağı | ⏳ |
| 8 | Implementation planı | ⏳ |

---

## 🔄 Sonraki Adımlar

1. **Web araştırmasını yap** (aracılık: Code mode, search tool)
2. **Bulguları dokümante et** → `plans/research-findings.md`
3. **Oğuz Usta data + Research → Final skill**
4. **Implementasyon için hazır**

---

**Not:** Bu plan, Oğuz Usta'nın gerçek verisi (100 shorts + 123 yatay)
ile web araştırması bulgularını harmanlayacak.
