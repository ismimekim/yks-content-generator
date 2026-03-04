# Sistem Yükseltme Planı - 4 Değişiklik

## 1. SHORT vs YATAY AYRIMI

### Sorun
Şu anda `platform` değişkeni var (YouTube, TikTok, Instagram) ve `contentType` var (script, reel, short).
Ama prompt sistemi ikisi için aynı stil kullanıyor.

### Çözüm: contentType'a göre stil seç

**Short Video Karakteristikleri** (100 örnek analizi):
```
- Selamlama YOK
- Karakter sayısı: 50-750
- Yapı: Hook → Kompakt açıklama → "Görüşürüz"
- Hook tipleri:
  - Sayısal iddia: "20 saatte TYT sosyal bitirebilirsin"
  - Soru: "1 soruya kaç dakika uğraşmalıyım?"
  - Uyarı: "lütfen AYT çalışmalarınızı bekletmeyin"
  - Madde madde: "AYT'ye geçmeden şunları bitir:"
- Hiç geçiş kelimesi yok
- Madde sayısı: 3-5
- Bitiriş: "görüşürüz" (tek cümle)
```

**Yatay Video Karakteristikleri** (123 örnek analizi):
```
- Selamlama: "Gençler selamlar herkese", "Gençler hoş geldiniz"
- Karakter sayısı: 5000-25000
- Yapı:
  - Selamlama
  - Video konusu tanıtım (1-2 cümle)
  - İçindekiler / akış tanıtımı (opsiyonel)
  - Ana içerik (çok madde, her biri derin)
  - Empati ve gerçek örnek
  - Kapanış motivasyonu
  - "Görüşürüz" / "Seviliyorsunuz"
- Geçiş kelimeleri bol: "Peki...", "Şimdi gençler...", "Gelelim..."
```

### prompts.ts'de Yapı

```typescript
// lib/prompts.ts içinde

const isShortContent = (contentType: string) =>
  ["short", "reel", "tiktok"].includes(contentType.toLowerCase());

function buildSystemPrompt(options) {
  const shortMode = isShortContent(options.contentType);
  const styleBlock = shortMode ? OGUZ_USTA_SHORT : OGUZ_USTA_YATAY;
  // ...
}
```

---

## 2. SHORT VIDEO HOOK TEKNİKLERİ

### Short Hook Kategorileri (Gerçek Oğuz Verisi)

**Tip 1: Sayısal İddia**
```
"20 saatte TYT sosyal bitirebilirsin"
"AYT'yi 3 ayda bitirmenin yolu şu"
"Bu 5 konuyu bilmeden AYT fene başlama"
```

**Tip 2: Uyarı / Tehdit**
```
"lütfen AYT çalışmalarınızı bekletmeyin"
"en büyük mezuna kalma sebebi şu"
"bu hatadan kaçın"
```

**Tip 3: Soru**
```
"1 soruya kaç dakika uğraşmalı?"
"AYT'ye ne zaman başlamalısın?"
"Kaç saat uyumalısın?"
```

**Tip 4: Madde Listesi**
```
"AYT fene geçmeden bunlar bitsin:"
"EA'cı TYT fen çalışmalı mı?"
"Bunları eleyebilirsin"
```

**Tip 5: İç Diyalog**
```
"Abi ben denemeye hazır değilim → Yanlış düşünüyorsun"
"Başarmak için zeki olmak gerekmez"
```

### Prompt'a Eklenecek:

```
## SHORT HOOK KURALLARI
1. İlk cümle = hook (selamlama yok)
2. Hook tipleri: sayısal iddia, uyarı, soru, madde listesi, iç diyalog
3. Hook 1 cümle, maksimum 10 kelime
4. Hook'tan sonra direkt açıklamaya gir
5. Toplam: 150-400 kelime
```

---

## 3. YKS DERİN KNOW-HOW KATMANI

### Eklenmesi Gereken Bilgiler

**Sınav Yapısı:**
```
TYT (Temel Yeterlilik Testi):
- 120 dakika
- Türkçe: 40 soru (% 40 ağırlık)
- Matematik: 40 soru
- Fen (Fizik, Kimya, Biyoloji): 20 soru
- Sosyal (Tarih, Coğrafya, Felsefe): 20 soru

AYT (Alan Yeterlilik Testi):
- 180 dakika
- Sayısal: Mat 40 + Fizik 14 + Kimya 13 + Bio 13 = 80 soru
- Eşit Ağırlık (EA): Mat 40 + Türk Dili 24 + Tarih 10 + Coğrafya 6 = 80 soru
- Sözel: Türk Dili 40 + Tarih 20 + Coğrafya 12 + Felsefe 8 = 80 soru

Puan Hesabı:
- TYT puanı hem lisans hem ön lisans için geçerli
- AYT puanı lisans için ek puan (sayısal, EA, sözel)
- Mezun öğrencilerde OBP katsayısı farklı
```

**Süreler ve Takvim:**
```
YKS sınav tarihi: Her yıl Haziran ayı (genellikle ilk iki hafta)
TYT 1. gün, AYT 2. gün
Başvuru: Şubat/Mart
Sonuçlar: Temmuz
Tercih: Ağustos
```

**Net Hesabı:**
```
Yanlış ceza: 4 yanlış = 1 net düşer (klasik)
Doğru: +1 net
Boş: 0
```

**Ders Ağırlıkları (Öncelik Sırası):**
```
Sayısal: Mat > Fizik > Kimya > Bio > TYT fen > TYT türkçe
EA: Mat > Geo (AYT) > Türk Dili > Tarih/Coğ > TYT türkçe
Sözel: Edebiyat > Tarih > Coğ > Felsefe > TYT türkçe
```

**Kaynak Önerileri (Oğuz Usta'nın sıkça bahsettikleri):**
```
Matematik/Geometri:
- Barış Serisi, 345, Paraf, Bilgi Sarmal, 3D, Apotemi, Mikro Orijinal, Acil, Orijinal

Türkçe/Edebiyat:
- Emektaş, Rüştü Hoca, Bilgi Sarmal, 3D

Fen:
- YayınCı bazlı (Paraf, Bilgi Sarmal)

Sosyal:
- CK (coğrafya/harita), Soner Ardıç (tarih), Felsefe Atölyesi (felsefe)

Deneme:
- 345 All Star, Baykuş Deneme Kulübü, Paraf, Apotemi
```

### lib/yks-knowledge.ts Dosyası

```typescript
// lib/yks-knowledge.ts (yeni dosya)
export const YKS_KNOWLEDGE = `
## YKS SINAV BİLGİSİ

### SINAV YAPISI
TYT: 40 Türkçe + 40 Mat + 20 Fen + 20 Sosyal = 120 soru / 135 dk
AYT Sayısal: 40 Mat + 14 Fizik + 13 Kimya + 13 Bio = 80 soru / 180 dk
AYT EA: 40 Mat + 24 Edebiyat + 10 Tarih + 6 Coğ = 80 soru / 180 dk
AYT Sözel: 40 Edebiyat + 20 Tarih + 12 Coğ + 8 Felsefe = 80 soru / 180 dk

### PUAN HESABI
Yanlış ceza: 4 yanlış = 1 eksik net
Net = Doğru - (Yanlış / 4)

### ÖNCELİK SIRASI (Ders Ağırlığı)
Sayısal: Matematik ilk, sonra fen, sonra TYT
EA: Matematik ilk, sonra edebiyat
Sözel: Edebiyat ilk, sonra sosyal

### KAYNAKLAR (Oğuz Usta'nın sıkça önerdiği)
Matematik: Barış, 345, Paraf, Bilgi Sarmal, Apotemi, 3D, Mikro
Geometri: Orijinal, Barış, 345
Türkçe: Emektaş, Rüştü Hoca, 3D
Coğrafya: CK
Tarih: Soner Ardıç
Felsefe: Felsefe Atölyesi
Deneme: Baykuş Deneme Kulübü, 345 All Star, Paraf, Apotemi
`;
```

---

## 4. API MODEL GÜNCELLEMESİ

### Dosya: `app/api/chat/route.ts`

```typescript
// Mevcut:
model: "claude-sonnet-4-5-20250929",

// Yeni:
model: "claude-sonnet-4-6",
```

---

## İMPLEMENTASYON SIRASI (Code Mode)

1. `app/api/chat/route.ts`: model adını güncelle (5 dakika)
2. `lib/yks-knowledge.ts`: YKS bilgi katmanı dosyası oluştur (15 dakika)
3. `lib/prompts.ts`:
   - `OGUZ_USTA_SHORT` ve `OGUZ_USTA_YATAY` ayrı konstantlar
   - `isShortContent()` helper fonksiyonu
   - `buildSystemPrompt()`'a YKS knowledge ekle
   - `buildSystemPrompt()`'ta short/yatay seçimi
4. Test et

---

## PROMPT ŞEMASI (Tamamlandığında)

```
buildSystemPrompt() OUTPUT:
├── CORE_PERSONA (kim olduğu)
├── OGUZ_USTA_SHORT veya OGUZ_USTA_YATAY (stil)
├── YKS_KNOWLEDGE (alan bilgisi)
├── DIRECT_PRODUCTION (üretim kuralları)
├── LANGUAGE (Türkçe)
└── CONTEXT (platform, format, kullanıcı isteği)
```
