# YKS Content Creator Skill - Implementation Plan

## Marketingskills Repo Analizi

**Repo:** coreyhaines31/marketingskills
- 10,510 stars
- "Marketing skills for Claude Code and AI agents"
- 30+ skills: copywriting, social-content, SEO, CRO, etc.

**Structure:**
```
skills/
├── skill-name/
│   ├── SKILL.md (metadata + frameworks)
│   └── references/
│       ├── platforms.md
│       ├── post-templates.md
│       └── reverse-engineering.md
```

## YKS Content Creator Skill Plan

### Phase 1: Skill Structure Kurulumu

**Klasör Yapısı:**
```
skills/yks-content-creator/
├── SKILL.md (metadata + frameworks)
└── references/
    ├── yks-terminology.md (233 video analizinden)
    ├── hook-formulas.md (6 hook tipi)
    ├── platform-strategies.md (Instagram, TikTok, YouTube)
    ├── content-pillars.md (3-5 pillar)
    └── few-shot-examples.md (DOĞRU + YANLIŞ)
```

### Phase 2: SKILL.md İçeriği

**Metadata:**
```yaml
---
name: yks-content-creator
description: "When the user wants to create YKS-focused social media content for Instagram Reels, TikTok, YouTube Shorts, or YouTube videos. Also use when the user mentions 'YKS script', 'soru çözümü', 'deneme analizi', 'AYT hazırlık', 'YKS koçluk', or 'öğrenci motivasyonu'. This skill covers content creation, hook writing, and YKS-specific terminology."
metadata:
  version: 1.0.0
  sources: 233 videos (Oğuz Usta 123 + Baykus 50 + Competitors 60)
  total_words: ~700K
---
```

**Context Gathering:**
1. **Goals** (Brand awareness, öğrenci kazanımı, topluluk)
2. **Audience** (11. sınıf, 12. sınıf, mezun, EA/Sayısal/Sözel)
3. **Platform** (Instagram Reel, TikTok, YouTube Shorts, Yatay)
4. **Topic** (TYT, AYT, deneme analizi, motivasyon)

**YKS Terminology (233 Video Analizi):**
- deneme: 4426x (KRİTİK)
- konu: 4172x
- TYT: 2276x
- çalışma: 2213x
- net: 1992x
- AYT: 1877x
- matematik: 1360x
- ... (top 100)

### Phase 3: Hook Frameworks

**6 Hook Tipi (Oğuz Usta'nın 100 shorts analizinden):**

1. **SORU Hook** (%53 dominant)
   - "AYT Tarihte 20 soruyu çözmek için tarih bilmen gerekmiyor."
   
2. **ŞAŞIRTICI İDDİA Hook**
   - "Yüzde dokuzu aynı hatayı yapıyor: Ezberliyor, sınavda çözemiyor."
   
3. **SAYI + SONUÇ Hook**
   - "100 saatte AYT sözelinin tamamını bitirebilirsin."
   
4. **KARŞITLIK Hook**
   - "Sınav kazanmak istiyorsan, sınav çalışmayacaksın."
   
5. **HİKAYE Hook**
   - "3 sene önce YKS'yi 300 kaçırdım, şimdi neden %5lik dilimi alıyorum."
   
6. **UYARI Hook**
   - "15 tatilde deneme çözme, konu çalış. Yanlış yapma."

**PAS Framework (Problem-Agitate-Solve):**
- **HOOK**: Problem'in şaşırtıcı versiyonu
- **AMPLIFY**: Hook'u aç, neden şaşırtıcı?
- **AGITATE**: Yanlış yapınca ne olur?
- **SOLVE**: Taktik ver (liste değil, konuşma dili)
- **CLOSE**: "Görüşürüz"

### Phase 4: Content Pillars (YKS için)

**5 Pillar Framework:**

| Pillar | % of Content | Topics |
|--------|--------------|--------|
| YKS Stratejisi | 30% | Deneme analizi, çalışma planı, net arttırma |
| Branş Taktikleri | 25% | TYT/AYT için matematik, tarih, coğrafya |
| Motivasyon | 20% | Disiplin, rutin, amaç |
| Kaynak Önerileri | 15% | Bilgi Sarmal, CK Haritalar, Baykuş |
| Soru Çözümü | 10% | Deneme analizi, mantık, neden-sonuç |

### Phase 5: Platform Strategies

**Instagram Reel (SHORT - 15-60s):**
- Selamlama YOK
- Hook → İçerik → Görüşürüz
- Doğal konuşma dili
- "Yani...", "Peki...", "Sonra..." bağlaçlar

**TikTok (SHORT - 15-60s):**
- Selamlama YOK
- Hook + hızlı içerik
- Trend odaklı
- Emoji kullanımı

**YouTube Shorts (SHORT - 60s):**
- Selamlama YOK
- Hook → Solve → Görüşürüz
- Bilgi odaklı

**YouTube Yatay (LONG - 10-20dk):**
- Selamlama var
- Derin içerik
- Örnekler, açıklamalar
- Q&A bölümü

### Phase 6: Few-Shot Examples

**DOĞRU ÖRNEK:**
```
🦉 AYT Tarihte 20 soruyu çözmek için tarih bilmen gerekmiyor.

Yani çoğu öğrenci ezber yapıyor ama sınavda çözemiyor...
Görüşürüz.
```

**YANLIŞ ÖRNEK (ASLA YAPMA):**
```
Gençler selamlar! AYT Tarihte şunlar yapmalısın:
1. Ezber yap
2. Soru çöz
```

### Phase 7: Implementation

**Action Items:**

1. **Create skill structure**
   ```bash
   mkdir -p skills/yks-content-creator/references
   ```

2. **Create SKILL.md**
   - Metadata (233 video, ~700K kelime)
   - Context gathering
   - YKS terminology integration
   - Hook frameworks
   - Content pillars
   - Platform strategies

3. **Create references:**
   - yks-terminology.md (deneme: 4426x, konu: 4172x, etc.)
   - hook-formulas.md (6 hook tipi + PAS framework)
   - platform-strategies.md (Instagram, TikTok, YouTube)
   - content-pillars.md (5 pillar framework)
   - few-shot-examples.md (DOĞRU + YANLIŞ)

4. **Integration with existing system**
   - lib/yks-knowledge.ts → already updated with 233 video data
   - lib/prompts.ts → OGUZ_USTA_SHORT already has HOOK_EXAMPLES
   - New: skills/yks-content-creator/SKILL.md (Claude Code skill format)

---

*Status: Ready for Implementation*
*Next: Create skill structure and SKILL.md*
