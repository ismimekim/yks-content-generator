# YKS Content Generator - Objektif Değerlendirme ve İyileştirme Planı

## Test Sonuçları Analizi

### Test 1: "Yaptın mı yapmadın mı" konsepti için 6 soru

**Output:**
```
🦉 Baykuş YKS: Yaptın mı, yapmadın mı?

Bu hafta deneme çözdün mü? → Çözdüm ✅ → Çözmedim ❌
Deneme analizine oturdun mu? → Oturdum, hangi branşta kaybettiğimi biliyorum ✅ → Çözdüm ama bakmadım ❌
AYT konularına bu ay dokundun mu? → Dokundum, konu çalıştım ✅ → "Önce TYT bitsin" diyorum ❌
Zayıf branşına bu hafta ekstra zaman ayırdın mı? → Ayırdım ✅ → Güçlü branşımla idare ettim ❌
Çalışma rutinin var mı? → Var, her gün aynı saat aynı ders ✅ → Ne gelse onu çalışıyorum ❌

Kaç tane ❌ var? 0 ❌ → Devam et, yoldasın. 1-2 ❌ → Fark ettin, düzelt. 3+ ❌ → Mart sana beklemiyor.
```

**✅ İyi Olan:**
- Format net ve anlaşılır (✅ / ❌ ikili seçenek)
- 6 soru tamamlandı
- Her sorunun iki alternatifi mevcut
- Son scoring mantığı güçlü (0, 1-2, 3+ ❌)
- Hook var (🦉 Baykuş YKS)
- Kapanış var (Görüşürüz)

**❌ Sorunlar:**
1. **Format hatası:** Listeleme formatına düştü (liste başlığı yok ama soru formatı liste)
2. **PAS framework eksik:** HOOK → AMPLIFY → AGITATE → SOLVE akışı yok
3. **SHORT format değil:** 6 satır soru = yatay video formatı gibi
4. **Engagement yok:** "Bu hafta deneme çözdün mü?" direkt soru, hook değil

**Beklenen format (SHORT için):**
```
🦉 Bu hafta kaç tane ❌ var?

Yani çoğu öğrenci "deneme çözdüm" diyor ama analiz yapmıyor.
Mart'ta analizi atlayan, Nisan'da niye gelişmediğini anlayamıyor.

Peki sen neredesin? Deneme çözdün mü? → ✅ / ❌
Analiz yaptın mı? → ✅ / ❌
[4 soru daha]

3+ ❌ varsa, Mart sana beklemiyor.

Görüşürüz.
```

---

### Test 2: "Yaptın mı yapmadın mı" serisi hakkında fikir

**Output:**
```
🦉 Yaptın mı yapmadın mı serisini genişletebilirsin.

Her hafta aynı format, farklı tema. Öğrenci her Pazartesi sabahı "bu hafta ben neredeyim?" diye kontrol ediyor. Alışkanlık oluşturuyor, kaydet oranı yüksek.

Temalar şöyle gidebilir:
- Deneme haftası → bu hafta deneme çözdün mü?
- Konu haftası → bu hafta AYT'ye dokundun mu?
[...]

Serinin gücü şu: Öğrenci ❌ görünce paylaşmak istiyor, ✅ görünce de. İkisi de engagement. Kaydet + yorum kombinasyonu güçlü.
```

**✅ İyi Olan:**
- Konsept analizi güçlü
- Engagement insight doğru
- Seri yapı önerisi akıllı (haftalık tema)
- Strateji seviyesi yüksek

**❌ Sorunlar:**
1. **Liste formatı kullanıldı** (5 tema liste halinde)
2. **HOOK → AMPLIFY → AGITATE → SOLVE akışı yok**
3. **Agent meta-konuşma yapıyor** ("genişletebilirsin", "gidebilir" → koçluk yerine danışmanlık)
4. **Platform = Instagram Post** ama format = advice/strategy (SHORT format değil)

**Beklenen (META content için):**
Bu bir "content stratejisi sorusu" → Agent'ın role'ü ne olmalı?
- Content creator olarak mı cevap vermeli? (Oğuz Usta voice)
- Consultant olarak mı? (Neutral strategy voice)

**Şu anki durum:** Agent consultant moduna düşmüş.

---

### Test 3: "Mart ayında AYT süreci ile ilgili 3 içerik önerir misin?"

**Output:**
```
1. Mart'ta AYT'ye dokunmayan Haziran'da pişman oluyor.

Hook olarak güçlü. Çoğu öğrenci Mart'ı "TYT ayı" zannediyor, AYT'yi yazaya bırakıyor. 
Ama AYT konu yükü yazda tek başına taşınamaz. Bu içerik o yanılgıyı kırar.

2. AYT'de hangi branştan başlamalısın?

Mart'ta AYT'ye girmek isteyen ama nereden başlayacağını bilemeyen öğrenci çok. 
Sayısal, EA, Sözel ayrımı yaparak her profile özel sıralama ver. Kaydet oranı yüksek olur.
```

**✅ İyi Olan:**
- 3 içerik önerisi (2 tanesi gösterildi)
- Hook analizi yapıyor ("Hook olarak güçlü")
- Strateji açıklaması var (neden bu içerik?)
- Engagement insight (kaydet oranı)

**❌ Sorunlar:**
1. **Liste formatı** (1, 2, 3)
2. **İçerik üretilmedi, sadece öneri yapıldı**
3. **Meta-konuşma:** "Bu içerik o yanılgıyı kırar", "Kaydet oranı yüksek olur"
4. **Agent role confusion:** Content creator değil, content strategist gibi davranıyor

---

## Kök Neden Analizi

### 1. Platform + Content Type Ambiguity

**Sorun:** User "Instagram Post" seçiyor ama içerik türü net değil.

| User Input | Platform | Agent'ın Anlaması | Gerçek İhtiyaç |
|------------|----------|-------------------|----------------|
| "6 soru lazım" | Instagram Post | "Liste formatı üreteyim" | Short format script |
| "fikrin var mı?" | Instagram Post | "Strateji önereyim" | Meta content (consultant mode) |
| "3 içerik öner" | Instagram Post | "İçerik listesi vereyim" | 3 SHORT script üret |

**Çözüm:** Platform seçimini netleştir + content type disambiguation ekle

### 2. Agent Role Confusion

**Mevcut durum:**
- Bazen content creator (Oğuz Usta voice)
- Bazen consultant (stratejik öneri)
- Bazen meta-speaker (content hakkında konuşuyor)

**Olması gereken:**
```
USER INTENT DETECTION:
1. "içerik üret" → CREATOR mode (Oğuz Usta voice, SHORT script)
2. "fikrin var mı?" → STRATEGIST mode (neutral, consultant)
3. "öner" → STRATEGIST mode (liste format OK)
```

### 3. Format Enforcement Zayıf

**Sorun:** Prompt'ta "YASAK: Liste formatı" yazıyor ama agent yine de liste üretiyor.

**Neden:**
- User "6 soru" dedi → Agent "liste format gerekli" diye yorumladı
- User "3 içerik öner" dedi → Agent "liste ile sun" dedi

**Çözüm:** Intent detection + format mapping güçlendirilmeli

---

## İyileştirme Planı

### Phase 1: Intent Detection System (Kritik)

**Goal:** User'ın ne istediğini doğru anla

```typescript
enum UserIntent {
  PRODUCE_CONTENT = "content", // "hazırla", "üret", "yaz"
  GET_STRATEGY = "strategy",    // "fikrin var mı?", "öner"
  GET_IDEAS = "ideas",          // "angle ver", "seçenek sun"
}

function detectIntent(userMessage: string): UserIntent {
  const produceSignals = ["hazırla", "üret", "yaz", "lazım"];
  const strategySignals = ["fikrin var mı", "ne düşünüyorsun", "değerlendir"];
  const ideaSignals = ["öner", "angle", "seçenek", "alternatif"];
  
  // Priority: produce > strategy > ideas
}
```

### Phase 2: Mode-Specific Prompts

**Mode 1: CONTENT CREATOR (Oğuz Usta Voice)**
- SHORT format ZORUNLU
- PAS framework ZORUNLU
- Liste formatı YASAK
- Meta-konuşma YASAK

**Mode 2: CONTENT STRATEGIST (Consultant)**
- Liste format İZİNLİ
- Meta-konuşma İZİNLİ
- Stratejik analiz İZİNLİ

### Phase 3: Format Validation

```typescript
function validateOutput(output: string, mode: UserIntent): boolean {
  if (mode === UserIntent.PRODUCE_CONTENT) {
    // Liste formatı kontrolü
    if (output.match(/^[\d\-\*]\./m)) return false;
    
    // PAS kontrolü
    if (!output.includes("🦉")) return false;
    if (!output.includes("Görüşürüz")) return false;
    
    // Meta-konuşma kontrolü
    if (output.includes("olarak güçlü") || output.includes("oranı yüksek")) return false;
  }
  
  return true;
}
```

### Phase 4: Few-Shot Examples Enhancement

**Şu anki durum:** Sadece 1 few-shot example (tarih örneği)

**Yeni examples:**
1. **Soru listesi üretme** (Test 1 senaryosu)
2. **Seri fikir verme** (Test 2 senaryosu)
3. **Çoklu içerik üretme** (Test 3 senaryosu)

---

## Implementation Workflow

### Sprint 1: Intent Detection (1-2 gün)

**Todolist:**
- [ ] `lib/intent-detector.ts` oluştur
- [ ] User message'dan intent çıkar
- [ ] Intent'e göre prompt mode seç
- [ ] Test: 10 farklı user input

**Success Criteria:**
- "6 soru lazım" → PRODUCE_CONTENT
- "fikrin var mı?" → GET_STRATEGY
- "3 içerik öner" → Belirsiz (hem strategy hem produce olabilir)

### Sprint 2: Dual-Mode Prompts (1 gün)

**Todolist:**
- [ ] `CREATOR_PROMPT` vs `STRATEGIST_PROMPT` ayrımı
- [ ] Her mode için ayrı few-shot examples
- [ ] buildSystemPrompt'u mode-aware yap

**Success Criteria:**
- CREATOR mode: SHORT format, PAS framework
- STRATEGIST mode: Liste OK, meta-konuşma OK

### Sprint 3: Output Validation (1 gün)

**Todolist:**
- [ ] `lib/output-validator.ts` oluştur
- [ ] Format kontrolü (liste, emoji, PAS)
- [ ] Invalid output → retry with stronger prompt

**Success Criteria:**
- CREATOR mode output'unda liste formatı yok
- PAS framework tüm elemanlara sahip

### Sprint 4: A/B Testing (1 hafta)

**Todolist:**
- [ ] Test 1 (soru listesi) → yeni sistem
- [ ] Test 2 (seri fikir) → yeni sistem
- [ ] Test 3 (çoklu içerik) → yeni sistem
- [ ] Sonuçları karşılaştır

**Success Metrics:**
- PAS framework completeness: >90%
- Liste formatı oranı: <10%
- User satisfaction (manuel değerlendirme)

---

## Risk Assessment

### Risk 1: Over-Engineering
**Risk:** Intent detection çok karmaşık olabilir
**Mitigation:** Basit keyword-based başla, sonra ML

### Risk 2: User Confusion
**Risk:** User hangi mode'dayı bilmeyebilir
**Mitigation:** Mode selection UI ekle (optional)

### Risk 3: Ambiguous Requests
**Risk:** "3 içerik öner" → strategy mi, produce mı?
**Mitigation:** Clarifying question sor

---

## Success Metrics (3 Ay)

| Metric | Baseline | Target (3M) |
|--------|----------|-------------|
| PAS Framework Completeness | 60% | 95% |
| Liste Formatı Kullanımı | 40% | <5% |
| Meta-konuşma Oranı | 30% | <10% |
| User Retry Rate | 25% | <10% |
| Content Creator Voice Consistency | 70% | 90% |

---

## Sonuç

**Temel Sorun:** Agent role'ünü ve user intent'ini tam anlayamıyor.

**En Kritik Fix:** Intent Detection System (Sprint 1)

**Quick Win:** Mode-specific few-shot examples (Sprint 2)

**Long-term:** RAG-lite ile daha fazla gerçek örnek (Phase 3)
