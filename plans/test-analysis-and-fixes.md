# Test Analysis & Prompt Fixes

## Test Output (AYT Tarih Script)

```
🦉 AYT Tarihte 20 soruyu çözmek için tarih bilmen gerekmiyor.

Yani çoğu öğrenci AYT Tarihe oturuyor, ezber yapıyor, ama sınavda o soruları göremiyorlar. Çünkü AYT Tarih ezber dersi değil, bağlantı kurma dersi.

Şunlara bak:
- 20 sorunun büyük çoğunluğu kronoloji değil, neden-sonuç ilişkisi soruyor
- Soner Ardıç'la önce olayların mantığını kur, sonra tarihleri öğren
- Her konu bittiğinde "Bu olay neden oldu, ne değiştirdi?" diye sor kendine
- Bilgi Sarmal ile konuları detaylı çalış ama Soner Ardıç olmadan girme
- Deneme analizinde yanlışlarına bak — ezbersiz mi yanlış yaptın, bağlantısız mı?

Görüşürüz.
```

---

## Objective Problem Analysis

| Problem | Severity | Evidence |
|---------|----------|----------|
| **1. "Şunlara bak:" breaks flow** | CRITICAL | Transitions from hook → list header feels unnatural. Oğuz's real scripts flow: hook → explanation → naturally embedded tactics, not hook → "here's a list". |
| **2. Named person references** | HIGH | "Soner Ardıç'la" and "Soner Ardıç olmadan" — Oğuz mentions resource names (books, platforms) but rarely individual teacher names in shorts. |
| **3. Body doesn't amplify hook** | CRITICAL | Hook says "tarih bilmen gerekmiyor" (counterintuitive), but body just gives study tips. Should explain WHY you don't need to "know history" (because it's about logic, not memorization). |
| **4. Missing PAS agitation** | HIGH | Goes straight from problem → solution. Missing the "feel the pain" middle step that creates urgency. |
| **5. Too listy, not speakable** | MEDIUM | Feels like a checklist, not a script someone would naturally speak in a 60-second video. |

---

## Root Cause Analysis

The current SHORT prompt has:
- ✅ Good hook frameworks (6 types, SUCCESs)
- ✅ PAS framework mentioned
- ❌ **Missing**: How to write the body AFTER the hook
- ❌ **Missing**: Flow structure (hook → amplify → agitate → solve → close)
- ❌ **Missing**: "No list headers" rule
- ❌ **Missing**: "Speak naturally, not write bullets" instruction

---

## Fix Strategy

### 1. Add FLOW STRUCTURE to SHORT

```
HOOK (1 cümle)
  ↓
AMPLIFY HOOK (2-3 cümle — hook'u açıkla, neden şaşırtıcı?)
  ↓
AGITATE (1-2 cümle — yanlış yaptığında ne olur?)
  ↓
SOLVE (3-4 taktik — "Yani şunu yap:", maddeler değil akış halinde)
  ↓
CLOSE ("Görüşürüz")
```

### 2. Add "NO LIST HEADERS" Rule

```
YASAK:
- "Şunlara bak:", "Bunları yap:", "İşte liste:"
- Bullet point header'ları
- "1. 2. 3." numaralandırma

ZORUNLU:
- Doğal akış: "Yani şunu yap. Sonra şunu. En önemlisi şu."
- Konuşma dili, yazı dili değil
```

### 3. Add "RESOURCE vs PERSON" Rule

```
KAYNAK KULLANIMI:
✅ Kaynak adı: "Bilgi Sarmal", "CK Haritalar", "Baykuş Deneme"
❌ Kişi adı: "Soner Hoca", "Emektaş Hoca"

Neden? Short formatda kişiye odak vermek yerine kaynağa odak ver.
```

### 4. Improve PAS Application

Current PAS is too theoretical. Make it concrete:

```
## PAS FRAMEWORK (SHORT İÇİN — SOMUT)

**HOOK** = Problem'in şaşırtıcı versiyonu
"AYT Tarihte 20 soruyu çözmek için tarih bilmen gerekmiyor."

**AMPLIFY** = Hook'u aç, neden şaşırtıcı?
"Yani çoğu öğrenci ezber yapıyor ama sınavda çözemiyorlar. 
Çünkü AYT Tarih ezber dersi değil, mantık dersi."

**AGITATE** = Yanlış yapınca ne oluyor? (Acıyı hissettir)
"Tarih konusu ezberledikten sonra sınavda 'bu neydi' diyorsun. 
Çünkü soruların mantığını bilmiyorsun."

**SOLVE** = Şimdi ne yapmalı? (Akış halinde, liste değil)
"Yani şunu yap: Konuyu okurken 'bu neden oldu' diye sor. 
Sonra soru çöz ama tarihi değil mantığı ara. 
En önemlisi, deneme analizinde mantık hatalarını bul."

**CLOSE** = Kapanış
"Görüşürüz."
```

---

## Expected Fixed Output

```
🦉 AYT Tarihte 20 soruyu çözmek için tarih bilmen gerekmiyor.

Yani çoğu öğrenci oturuyor, tüm konuları ezberliyor ama sınavda 
çözemiyorlar. Çünkü AYT Tarih ezber dersi değil, mantık dersi. 
Sorular tarihleri değil olayların nedenini soruyor.

Peki yanlış çalışınca ne oluyor? Şunu yaşıyorsun: Konuyu 
ezberliyorsun, sınava giriyorsun, soruya bakıyorsun "bu neydi" 
diyorsun. Çünkü mantığı bilmiyorsun.

Yani şunu yap: Her konu bittiğinde "bu olay neden oldu, ne 
değiştirdi" diye sor. Sonra soru çözerken tarihi değil mantığı 
ara. En önemlisi deneme analizinde mantık hatalarını bul, ezber 
hatalarını değil.

Görüşürüz.
```

**What's fixed:**
- ✅ No "Şunlara bak:" list header
- ✅ Flows naturally: hook → amplify → agitate → solve → close
- ✅ No person names, just concepts
- ✅ Sounds like speech, not bullets
- ✅ Hook is amplified (explains WHY it's surprising)
- ✅ Agitation phase (feel the pain of wrong study)
- ✅ Solution is embedded in flow ("Yani şunu yap:", "Sonra", "En önemlisi")

---

## Implementation Plan

1. Update `OGUZ_USTA_SHORT` in lib/prompts.ts
2. Add FLOW STRUCTURE section
3. Add NO LIST HEADERS rule
4. Add RESOURCE vs PERSON rule
5. Update PAS FRAMEWORK to be concrete, not theoretical
6. Add EXAMPLE of good flow vs bad flow

---

*Analysis completed: 26 February 2026*
