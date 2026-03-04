# İçerik Üretim Pipeline - Detaylı Analiz ve Tasarım

## 🔍 ÇIKTI ANALİZİ

### Sorun 1: Zayıf Hook
**Üretilen:** "AYT Tarih'ten 20 yapmanız çok normal"
**Sorun:** Bu hook değil, açıklama
- Hook olmalı: Sayısal iddia, uyarı, soru, madde listesi veya iç diyalog
- Örnek hook: "AYT Tarih'te 20 net almak mümkün — ama yanlış çalışırsan imkansız" (iç diyalog)
- Veya: "AYT Sözel'de tarih 20 sorudan 15-16 net yapmalısın — işte yol haritası" (sayısal + path)

**Sebep:** Prompt'ta hook tipleri tanımlanmış ama LLM seçim yapamıyor. Hook seçimi **dinamik** olmalı.

### Sorun 2: Rastgele Yapı
**Gözlem:** İlk cevap 5 madde, ikinci cevap 2 bölüm (TYT bilgisi + AYT hedefi)
**Sebep:** Yapı şablonu zayıf. "Ana içerik" tanımlaması belirsiz.

**Needed:** Madde sayısı, yapı sırası, her bölümün uzunluğu — **somut olmalı**.

### Sorun 3: YKS Know-How Zayıf Entegrasyonu
**Gözlem:** "Soner Ardıç'ın 7 Günde TYT Tarih kaynağı" bahsedildi ama:
- Neden bu kaynak? Alternatifler neler?
- Kaç saatte bitirilir?
- Hangi konular kapsanıyor?
- Sonrasında ne yapılmalı?

**Sebep:** `YKS_KNOWLEDGE` dosyasında kaynak listesi var ama **kaynak entegrasyonu** değil. 
Yani: "Soner Ardıç'ı kullan" yazıyor ama LLM hangi bağlamda kullanacağını bilmiyor.

### Sorun 4: İçeriğin Hook Bölümü Eksik
**Observation:** 
- Çıktı: Hook + açıklama + maddeler
- Olmalı: Hook → Hook açıklaması → Ana içerik → Yakıt (motivasyon)

İlk çıktı:
```
🦉 AYT Tarih'ten 20 yapmanız çok normal  ← Zayıf hook (açıklama)

Yani sınavda...  ← Hook açıklaması?
```

İyi olmalı:
```
🦉 AYT Tarih'te 15-16 net yapmalısın — işte formülü  ← Hook (iddia + merak)

Neden? Sözel'de 20 soru × 4 puan = 80 puan...  ← Hook açıklaması (why)

Peki nasıl? İşte adımlar...  ← Ana içerik
```

---

## 🏗️ İÇERİK ÜRETİM PIPELINE TASARIMI

### Pipeline Aşamaları

```
Kullanıcı İsteği
    ↓
[1] HOOK SEÇİMİ — Dinamik
    ├─ Konu analizi
    ├─ Hook tipi seçimi (5'den biri)
    └─ Hook metni üretimi
    ↓
[2] YAPI PLANLAMASİ — Template-based
    ├─ Platform (short/yatay)
    ├─ Uzunluk hedefi (karakter/kelime)
    ├─ Madde sayısı
    └─ Bölüm sırası
    ↓
[3] YKS KNOW-HOW ENTEGRASYONU — Context-aware
    ├─ Konu ile ilgili TYT/AYT kuralları
    ├─ Kaynak önerisi (neden bu?)
    ├─ Zaman tahmini
    └─ Avantaj/dezavantaj
    ↓
[4] İÇERİK ÜRETIMI — Full context
    ├─ Hook seçimi
    ├─ Yapı takibi
    ├─ YKS bilgisi entegrasyonu
    ├─ Oğuz Usta stil kalıpları
    └─ Kapanış (motivasyon)
    ↓
[5] ÇIKTI — Tam içerik
```

---

## 🧠 HOOK SEÇİMİ — Dinamik Algoritması

### Hook Tipleri (5'den biri seçilmeli)

| Tip | Kullanım | Örnek |
|-----|----------|-------|
| **Sayısal Iddia** | Spesifik hedef var | "AYT'den 250+ almak için 50+ AYT gerekli" |
| **Uyarı** | Yaygın hata var | "lütfen AYT çalışmalarını bekletmeyin" |
| **Soru** | Öğrenci kafasında soru | "1 soruya kaç dakika uğraşmalısın?" |
| **Madde Listesi** | Yapılması gerekenler | "AYT fene geçmeden 5 şey bitsin" |
| **İç Diyalog** | Yanılgı vs gerçek | "Abi ben denemeye hazırım → Yanlış, şu gerekli" |

### Hook Seçim Mantığı

```
Konu ∈ {"uyarı", "başlama saati", "zaman yönetimi"} → Uyarı hook
Konu ∈ {"soru sayısı", "süre", "dakika"} → Soru hook
Konu ∈ {"yapılacaklar", "adımlar", "hazırlık"} → Madde listesi hook
Konu ∈ {"başarı", "hedef", "net almak"} → Sayısal iddia hook
Konu ∈ {"düşünce", "yanılgı", "kafada"} → İç diyalog hook
```

**Örnek:**
- Kullanıcı: "AYT tarih için..." → Konu = tarih, context = yol haritası → **Sayısal iddia hook** ("AYT'de 20 net almak mümkün")
- Kullanıcı: "Kaç saat çalışmalı?" → Konu = saat/zaman → **Soru hook** ("Günde kaç saat çalışmalısın?")
- Kullanıcı: "Nasıl başlamalı?" → Konu = başlama → **Madde listesi hook** ("AYT'ye başlamadan 3 şey yap")

---

## 📋 YAPILANDIRMA ŞABLONU

### Instagram Script (Yatay ama Instagram formatında)

**Uzunluk:** 800-1500 kelime (copy-paste kullanılabilir)
**Yapı:**
```
[Hook] — 1 cümle, 5-15 kelime
[Hook Açıklaması] — 2-3 cümle, neden/ne zaman/kimin için
[Bölüm 1] — Sorunun/bağlamın derinlemesine analizi
[Bölüm 2] — Çözüm/yol haritası
[Bölüm 3] — Gerçek örnek veya vaka
[Motivasyon + Kapanış] — İç diyalog veya pekiştirme
[Hitap + Emoji + Görüşürüz]
```

### Örnek Instagram Script (Tarih)

```
🦉 AYT Tarih'te 15-16 Net Almak Mümkün — İşte Formülü

Gençler, sözel'de 20 tarih sorusu var. 15-16 yapmazsan fark kaybı devasa. Ama bunu biliyorsunuz. Sıkıntı ne? Çoğunuz hala yanlış çalışıyor.

NE YAPIYORSUNUZ YANLIŞ?

Hani şöyle, tarih sadece ezber deyip düşünüyorsunuz. Ama tarih yapılı bir şey. Sebep-sonuç var, kronoloji var, olaylar birbiriyle bağlantılı.

Mesela, Osmanlı'nın çöküşünü anlamadan sadece tarihler ezberlersem, sınav da işte o tuzağa düşüyorum. "Neden 1453'te İstanbul düştü?" diye soruyorlar, ben de "çünkü 1453'te düştü" diyorum. Net gelmez.

PEKI DOĞRU NASIL?

Adım 1: TYT Tarih'i Bitir
Soner Ardıç'ın 7 Günde TYT Tarih kaynağını alıyorsun. Neden? Hızlı, sistematik, kronolojik. 7 günde tüm TYT tarihini organize edersin. 120 dakikalık video + 50 soru. Bu yeterli.

Adım 2: AYT Tarih — Sebep-Sonuç Haritası
Osmanlı İmparatorluğu → Çöküş → Kurtuluş Savaşı → Lozan
Hani şöyle, her bölümde şu sorulara cevap veriyorsun:
- Ne oldu?
- Neden oldu?
- Kimin için avantaj/dezavantaj?
- Sonra ne oldu?

Adım 3: ÖSYM Soru Mantığı
ÖSYM'nin favori soruları: sebep-sonuç, karşılaştırma, kronoloji, neden-niçin.
Deneme çözüyorsun, bunu görüyorsün. Yanlış sorulara bak: "Neden yanlış yaptım? Kronoloji mi karıştı, sebep-sonuç mu?"

Adım 4: Yanlış Defteri
Tarih'te yanlış yaptığın sorular. Satır satır: olay-ne bilmedin-doğrusu. Sınav sabahı okursun.

15-16 net almak için bunlar yeterli. Asla 20 yapamayacaksın dersen haklı olabilirsin ama 16 mümkün.

3 ayın var daha. Panik yapma, sistemli çalış.

Görüşürüz, seviliyorsunuz 💜
```

---

## 🔗 YKS KNOW-HOW ENTEGRASYONU

### Sorun: Kaynak "Suggestion" Kalıyor, "Integration" Değil

**Şu anda:** `YKS_KNOWLEDGE`'da liste
```
Tarih: Soner Ardıç (7 Günde TYT Tarih)
```

**Olması gereken:** İçeriğe bağlı suggestion
```
Tarih:
- TYT için: Soner Ardıç (neden: hızlı, kronolojik, 7 gün)
- AYT için: Bilgi Sarmal (neden: derinlikli, sebep-sonuç, ÖSYM logic)
- Deneme: Paraf, Apotemi (neden: soru kalitesi, analiz detayı)

Zaman:
- TYT Tarih: 7 gün (Soner Ardıç) + 3 gün review = 10 gün
- AYT Tarih: 4 hafta (Bilgi Sarmal) + 2 hafta deneme = 6 hafta
```

### Çözüm: Context-Aware Resource Module

```typescript
// lib/yks-resources.ts
interface ResourceContext {
  subject: "tarih" | "coğrafya" | "edebiyat" | ...;
  exam: "tyt" | "ayt";
  purpose: "learning" | "review" | "deneme";
  timeFrame: "1week" | "2weeks" | "month";
}

function getOptimalResource(context: ResourceContext): {
  source: string;
  why: string;
  duration: string;
  nextStep: string;
}

// Örnek:
getOptimalResource({
  subject: "tarih",
  exam: "tyt",
  purpose: "learning",
  timeFrame: "1week"
})
// Return:
// {
//   source: "Soner Ardıç - 7 Günde TYT Tarih",
//   why: "Kronolojik yapı, hızlı bitme, ÖSYM soru tipine hazırlık",
//   duration: "7 gün (120 dakika video + 50 soru)",
//   nextStep: "AYT Tarih'e başla - Bilgi Sarmal"
// }
```

---

## 🛠️ PROMPT YAPISI (Güncellenmiş)

### Current vs Needed

**Şu anda:**
```
CORE_PERSONA
+ STYLE_BLOCK (SHORT/YATAY)
+ YKS_KNOWLEDGE (Liste)
+ DIRECT_PRODUCTION
+ CONTEXT
```

**Olması gereken:**
```
CORE_PERSONA
+ STYLE_BLOCK (SHORT/YATAY)
+ [HOOK SELECTION STRATEGY]
+ [STRUCTURE TEMPLATE]
+ YKS_KNOWLEDGE (Liste)
+ [YKS RESOURCE INTEGRATION]
+ DIRECT_PRODUCTION
+ CONTEXT
```

---

## 📊 İŞ AKIŞI

### Sıradaki Milyonuncu Adımlar

1. **Hook Selection Module** → `lib/hook-selector.ts`
   - 5 hook tipi tanımı
   - Konu-hook mapping
   - Hook üretimi

2. **Structure Templates** → `lib/content-structure.ts`
   - Platform × ContentType × Uzunluk kombinasyonları
   - Her kombinasyon için madde sayısı, bölüm sırası, hedef kelime sayısı

3. **Resource Context** → `lib/yks-resources.ts`
   - Subject × Exam × Purpose × TimeFrame kombinasyonları
   - Her için optimal kaynak + neden + süre + next step

4. **Prompt Refactoring** → `lib/prompts.ts`
   - Hook selector entegrasyonu
   - Structure template entegrasyonu
   - Resource context entegrasyonu

5. **Test Scenarios** → `scripts/test_content_pipeline.py`
   - Çeşitli konu + format kombinasyonlarını test et
   - Hook, yapı, resource entegrasyonunu validate et

---

## 📈 Başarı Ölçüsü

| Metrik | Şu | Hedef |
|--------|-----|-------|
| Hook Kalitesi | Açıklama | 5 tipten biri, merak uyandıran |
| Yapı Tutarlılığı | Rastgele | Template takip, madde sayısı sabit |
| YKS Integration | Liste | Konu-specific kaynak + neden + next |
| Content Depth | Sığ | Oğuz Usta'nın gerçek videolarına yakın |
| Format Uyması | Zayıf | Copy-paste kullanılabilir |
