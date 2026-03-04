# İçerik Üretim Sistemi - Detaylı Uygulama Planı

## Kararlar (Kullanıcı Onaylı)
- **Veri Kaynağı**: Başlık + tam transkript (her ikisi beraber)
- **Kategorilendirme**: Otomatik (LLM destekli)
- **Test**: Tüm 223 video ile karşılaştırmalı test

---

## PHASE 1: Style Extractor Script

### Dosya: `scripts/extract_style.py`

**Girdi**: `data/oguz_usta_yatay.json` veya `data/oguz_usta_shorts.json`  
**Çıktı**: `data/style_profiles/oguz_usta_yatay_profile.json`

**Kullanım**:
```bash
python3 scripts/extract_style.py data/oguz_usta_yatay.json oguz_usta_yatay
python3 scripts/extract_style.py data/oguz_usta_shorts.json oguz_usta_shorts
```

**Çıkarılacak Alanlar**:

```python
# Her kaynak için:
{
  "title": str,
  "char_count": int,
  "category": str,               # otomatik sınıflandırma
  "opening_formulas": [str],     # İlk 3 cümle
  "closing_formulas": [str],     # Son 2 cümle
  "transitions": [str],          # Geçiş kelimeleri
  "address_terms": [str],        # Hitap şekilleri
  "emojis": [str],               # Kullanılan emojiler
  "sentence_patterns": {
    "aciklama": [str],            # "hani şöyle...", "yani..."
    "vurgu": [str],               # "asla...", "kesinlikle..."
    "samimiyet": [str],           # "valla...", "abi..."
  }
}
```

**Toplu Profile Yapısı** (çıktı JSON):

```json
{
  "meta": {
    "source": "oguz_usta_yatay",
    "sample_size": 123,
    "total_chars": 2240922,
    "extracted_at": "2026-02-26T..."
  },
  "opening": {
    "formulas": [
      ["Gençler selamlar herkese", 45],
      ["Sevgili 11'ler hoş geldiniz", 12],
      ...
    ],
    "hooks": []
  },
  "body": {
    "sentence_patterns": {
      "aciklama": ["hani şöyle", "yani"],
      "vurgu": ["asla", "kesinlikle"],
      "samimiyet": ["valla", "abi"]
    }
  },
  "closing": {
    "formulas": [
      ["Görüşürüz", 98],
      ["Seviliyorsunuz 💜", 45],
      ...
    ]
  },
  "transitions": ["şimdi gençler", "peki", "evet sevgili", ...],
  "vocabulary": {
    "address_terms": {
      "gençler": 98,
      "abi": 45,
      "canım": 23
    }
  },
  "content_categories": {
    "taktik_rehber": 45,
    "soru_cevap": 30,
    "motivasyon": 20,
    ...
  },
  "style": {
    "emojis": {
      "🦉": 89,
      "💜": 34,
      "⚡": 12
    },
    "number_formats": [
      ["35 net", 23],
      ["120 gün", 15],
      ...
    ]
  }
}
```

**Kategori Sınıflandırma Mantığı** (regex tabanlı):

| Kategori | Tetikleyici Kelimeler |
|----------|----------------------|
| `soru_cevap` | kaç, nasıl, nerede, ne zaman, soruya, `?` |
| `taktik_rehber` | nasıl çalışılır, nasıl çalışmal, rehber, taktik |
| `motivasyon` | motivasyon, disiplin, stres, zihniyet, başarm |
| `deneme` | deneme, analiz, sıra, net art |
| `program` | günde, program, plan, bitir |
| `kaynak_onerisi` | en iyi, öneri, tavsiye, kaynak, soru bankası |
| `seviye_ozel` | 11'ler, 12'ler, mezun, EA, sayısal, sözel |
| `konuk_gorusmesi` | ustacast, konuk, röportaj |
| `genel` | diğer her şey |

---

## PHASE 2: LLM Destekli Derin Analiz

### Dosya: `scripts/analyze_style_llm.py`

**Amacı**: Phase 1'den çıkan ham pattern'ları LLM ile derinleştirme.

**Girdi**: `data/style_profiles/oguz_usta_yatay_profile.json` + orijinal transkriptler  
**Çıktı**: `data/style_profiles/oguz_usta_refined_profile.json`

**LLM Prompt Yapısı**:

```python
ANALYSIS_PROMPT = """
Sen bir içerik analisti ve tarz analistsin.

Aşağıda Oğuz Usta'nın {n} videosundan alınan veri var.
Her video için başlık + içerik metin var.

GÖREV:
1. Giriş formüllerini tespit et (kesin cümleler, tahmin değil)
2. Kapanış formüllerini tespit et
3. Hitap şekillerini listele (hangi kelimeleri kullanıyor)
4. Kaçınılan kelimeleri listele
5. Karakteristik cümle başlangıçlarını listele
6. Her kategori için örnek yapı şeması çıkar

KURAL:
- SADECE veriden çıkanları yaz
- Tahmin yapma
- "muhtemelen" "olabilir" gibi ifade kullanma

VERİ:
{video_samples}
"""
```

**Per-Category Analiz**:

Her kategori için ayrı bir LLM çağrısı:
- `taktik_rehber` kategorisindeki 45 videonun yapısı nedir?
- `motivasyon` kategorisindeki başlangıç-gelişme-kapanış yapısı nedir?
- `soru_cevap` formatında hangi kalıplar tekrar ediyor?

---

## PHASE 3: TypeScript Entegrasyonu

### 3a. `lib/types.ts` Güncellemesi

Eklenecek interface:

```typescript
export interface StyleProfile {
  meta: {
    source: string;
    sampleSize: number;
    totalChars: number;
    extractedAt: string;
  };
  opening: {
    formulas: [string, number][];   // [metin, frekans]
    hooks: [string, number][];
  };
  body: {
    sentencePatterns: {
      aciklama: string[];
      vurgu: string[];
      samimiyet: string[];
    };
  };
  closing: {
    formulas: [string, number][];
  };
  transitions: string[];
  vocabulary: {
    addressTerms: Record<string, number>;
  };
  contentCategories: Record<string, number>;
  style: {
    emojis: Record<string, number>;
    numberFormats: [string, number][];
  };
}
```

### 3b. `lib/style-loader.ts` Yeni Dosyası

```typescript
import oguzUstaProfile from "../data/style_profiles/oguz_usta_refined_profile.json";
import type { StyleProfile } from "./types";

const profiles: Record<StyleSource, StyleProfile | null> = {
  oguz_usta: oguzUstaProfile as StyleProfile,
  baykus: null,
  // ... diğerleri null
};

export function getStyleProfile(source: StyleSource): StyleProfile | null {
  return profiles[source] ?? null;
}

export function buildStyleBlock(profile: StyleProfile | null): string {
  if (!profile) return "Samimi, öğretici, motivasyonlu içerik tarzı";

  const topOpenings = profile.opening.formulas.slice(0, 3).map(([text]) => `- "${text}"`).join("\n");
  const topClosings = profile.closing.formulas.slice(0, 2).map(([text]) => `- "${text}"`).join("\n");
  const topEmojis = Object.keys(profile.style.emojis).slice(0, 5).join(" ");
  const addressTerms = Object.keys(profile.vocabulary.addressTerms).slice(0, 5).join(", ");

  return `
# STYLE: ${profile.meta.source}
(${profile.meta.sampleSize} video analizi)

**GİRİŞ:**
${topOpenings}

**KAPANIŞ:**
${topClosings}

**HİTAP:**
${addressTerms}

**EMOJİ:**
${topEmojis}

**KAÇIN:**
- Veride olmayan kelimeler kullanma
- Tahmin üzeri kalıp ekleme
`.trim();
}
```

### 3c. `lib/prompts.ts` Güncelleme

`buildSystemPrompt()` fonksiyonu içinde:

```typescript
import { getStyleProfile, buildStyleBlock } from "./style-loader";

// ...
const profile = getStyleProfile(styleSource);
const styleBlock = buildStyleBlock(profile);
```

---

## PHASE 4: Test Planı

### Test Kriterleri

| Kriter | Hedef |
|--------|-------|
| Doğru hitap kelimesi | `%100` - veride olanlar |
| Kapanış formülü | `%90` - görüşürüz veya sevgilerle |
| Yanlış kelime | `%0` - "kanka" gibi olmayan kelimeler |
| İçerik kategorisi tahmini | `%80` doğruluk |

### Test Scripti: `scripts/test_style.py`

```python
# Her video için:
# 1. Orijinal video içeriğini al
# 2. Aynı konuda içerik ürettir
# 3. Karşılaştır:
#    - Giriş formülü eşleşiyor mu?
#    - Kapanış formülü eşleşiyor mu?
#    - Sahte kelimeler var mı?
```

---

## DOSYA YAPISI (Tamamlandığında)

```
data/
  oguz_usta_yatay.json          ✅ mevcut
  oguz_usta_shorts.json         ✅ mevcut
  oguz_usta_merged.json         ✅ mevcut
  style_profiles/
    oguz_usta_yatay_profile.json    ← Phase 1 çıktısı
    oguz_usta_shorts_profile.json   ← Phase 1 çıktısı
    oguz_usta_refined_profile.json  ← Phase 2 çıktısı

scripts/
  extract_sources.py            ✅ mevcut
  extract_style.py              ← Phase 1 (yazılacak)
  analyze_style_llm.py          ← Phase 2 (yazılacak)
  test_style.py                 ← Phase 4 (yazılacak)

lib/
  types.ts                      ← StyleProfile interface eklenecek
  style-loader.ts               ← Yeni dosya
  prompts.ts                    ← style-loader kullanacak şekilde güncelle
```

---

## UYGULAMA SIRASI

```
Code Mode'a geçince:

1. scripts/extract_style.py yaz
2. Çalıştır: python3 scripts/extract_style.py data/oguz_usta_yatay.json oguz_usta_yatay
3. Çalıştır: python3 scripts/extract_style.py data/oguz_usta_shorts.json oguz_usta_shorts
4. scripts/analyze_style_llm.py yaz (Anthropic API ile)
5. Çalıştır ve refined profile oluştur
6. lib/types.ts'ye StyleProfile ekle
7. lib/style-loader.ts oluştur
8. lib/prompts.ts güncelle
9. scripts/test_style.py ile test et
```
