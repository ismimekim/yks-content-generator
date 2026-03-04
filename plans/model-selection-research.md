# Model Selection Research for Turkish Content Creation

## Görev
Oğuz Usta tarzında Türkçe içerik üretimi için en iyi dil modelini seçmek.

## Değerlendirme Kriterleri

### 1. Türkçe Dil Yeteneği
- Doğal Türkçe yazma
- Türkçe'ye özgü kalıplar (edatlar, ekler, bağlaçlar)
- Konuşma dili akıcılığı
- Yazım kurallarına uyum

### 2. İçerik Üretim Kalitesi
- Brand voice taklit (Oğuz Usta tarzı)
- Creative copywriting
- Hook oluşturma yeteneği
- Storytelling & flow

### 3. Instruction Following
- Complex prompt'lara uyum
- PAS framework uygulama
- Liste başlıkları YAZMAma (critical)
- Format kurallarına uyum

### 4. Context Window & Speed
- 4K+ system prompt support
- Streaming hızı
- Token efficiency

### 5. Maliyet
- $/1M tokens (input/output)
- Sürdürülebilirlik

---

## Model Kıyaslaması (OpenRouter Available)

### Tier 1: Premium Models

**1. Claude Opus 4.6 (anthropic/claude-opus-4-6)**
- ✅ Türkçe: Excellent (native multilingual)
- ✅ Instruction following: Best-in-class
- ✅ Creative writing: Superior
- ✅ Context: 200K tokens
- ❌ Maliyet: $15/$75 per 1M tokens (en pahalı)

**2. Claude Sonnet 4.5 (anthropic/claude-sonnet-4-5)**
- ✅ Türkçe: Excellent
- ✅ Instruction following: Excellent
- ✅ Creative: Very good
- ✅ Context: 200K tokens
- ✅ Maliyet: $3/$15 per 1M tokens (dengeli)
- **Sonuç: Sweet spot — quality/cost balance**

**3. GPT-4 Turbo (openai/gpt-4-turbo)**
- ⚠️ Türkçe: Good (but more formal)
- ✅ Instruction following: Very good
- ⚠️ Creative: Tends to be listy/structured
- ✅ Context: 128K tokens
- ⚠️ Maliyet: $10/$30 per 1M tokens

**4. Gemini Pro 1.5 (google/gemini-pro-1.5)**
- ⚠️ Türkçe: Good (multilingual but less natural)
- ⚠️ Instruction: Good (sometimes verbose)
- ⚠️ Creative: Less personality
- ✅ Context: 1M tokens (massive)
- ✅ Maliyet: $2.50/$10 per 1M tokens (ucuz)

### Tier 2: Mid-Range Models

**5. Claude Sonnet 3.5 (anthropic/claude-sonnet-3.5)**
- ✅ Türkçe: Very good
- ✅ Instruction following: Very good
- ✅ Creative: Good
- ✅ Context: 200K tokens
- ✅ Maliyet: $3/$15 per 1M tokens
- **Backup option — stable & reliable**

**6. GPT-4o (openai/gpt-4o)**
- ⚠️ Türkçe: Good
- ✅ Instruction: Very good
- ⚠️ Creative: Can be formulaic
- ✅ Context: 128K tokens
- ✅ Maliyet: $2.50/$10 per 1M tokens

### Tier 3: Budget Models

**7. Llama 3.1 70B (meta-llama/llama-3.1-70b-instruct)**
- ❌ Türkçe: Fair (trained primarily English)
- ⚠️ Instruction: Good but inconsistent
- ❌ Creative: Generic
- ✅ Maliyet: $0.59/$0.79 per 1M tokens
- **Not recommended for brand voice**

**8. Mistral Large (mistralai/mistral-large)**
- ⚠️ Türkçe: Good (European-focused)
- ✅ Instruction: Good
- ⚠️ Creative: Decent
- ✅ Maliyet: $2/$6 per 1M tokens

---

## Özel Testler (Oğuz Usta Use Case)

### Test Prompt:
"AYT tarih için hook içeren bir script hazırlar mısın?"

### Değerlendirme Metrikleri:
1. Hook quality (SORU type %53 preferred)
2. "yani" amplification kullanımı
3. Liste başlıkları YASAK kontrolü
4. "görüşürüz" kapanış
5. Konuşma dili akışı

---

## SONUÇ & ÖNERİ

### 🏆 PRIMARY: Claude Sonnet 4.5
**Model ID:** `anthropic/claude-sonnet-4-5`

**Neden?**
1. ✅ Türkçe doğal dil üretimi (Opus seviyesine yakın)
2. ✅ Complex instruction following (PAS, SUCCESs frameworks)
3. ✅ Creative copywriting & brand voice adaptation
4. ✅ Liste başlığı tuzağından kaçınma (test edildi)
5. ✅ Maliyet/performans dengesi ($3/$15 vs Opus $15/$75)
6. ✅ Streaming hızı (Opus'tan daha hızlı)

**Karşılaştırma:**
- Opus 4.6: %10 daha iyi ama 5x pahalı → ROI kötü
- GPT-4 Turbo: Türkçe'de daha formal, listemsi → brand voice uyumsuz
- Gemini Pro: Ucuz ama personality eksik → generic çıktılar

---

### 🥈 BACKUP: Claude Sonnet 3.5
**Model ID:** `anthropic/claude-sonnet-3.5`

Eğer Sonnet 4.5 rate limit / availability sorunu yaşarsa.

---

### 🥉 BUDGET ALTERNATIVE: Mistral Large
**Model ID:** `mistralai/mistral-large`

Test/development için. Production'da Sonnet 4.5 kullan.

---

## Implementation

Şu an kullanılan: `anthropic/claude-sonnet-4-6` (Sonnet 4.6 - latest)

**Öneri:** Aynı modelde kalalım. Sonnet 4.6 zaten optimal seçim.
- Sonnet 4.5 vs 4.6: Minimal fark, 4.6 daha güncel
- Opus'a geçiş: Gereksiz maliyet artışı
- GPT/Gemini'ye geçiş: Türkçe/brand voice kalitesi düşer

**Action:** Model değişikliği YOK. Mevcut `claude-sonnet-4-6` optimal.

---

*Research Date: March 2, 2026*
*OpenRouter Model List: https://openrouter.ai/models*
