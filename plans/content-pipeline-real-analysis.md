# İçerik Üretim Pipeline - Gerçek Veri Analizi ve Tam Tasarım

## BÖLÜM 1: GERÇEK VERİDEN ÇIKARILAN HOOK PATTERN'LARI

### A. SHORTS Hook Tipleri (100 video analizi)

Gerçek veri incelendiğinde 6 distinct hook pattern:

---

**Tip 1: RAKAM + SÖZ VERİ (Commitment Hook)**
```
Format: "[Rakam] [zaman/birim]de [konu] [fiil]"
Örnekler:
- "20 saatte tyt sosyal bitirebilirsin" (video: 20 SAATTE TYT SOSYAL)
- "matematikte 80'de 80 yapmama ciddi katkısı olan..." (video: BU RUTİNİ DENE)
- "25 dakikada türkçe çözmek" (başlık+içerik)
Psikoloji: Net rakam = güvenilirlik. "Yapabilirim" hissi.
Tetikleyici: Spesifik hedef var, zaman baskısı var.
```

**Tip 2: UYARI + TEHDİT (Warning Hook)**
```
Format: "lütfen [şeyi] [yapma/bekletme]" VEYA "en büyük [kötü şey] [sebep]"
Örnekler:
- "lütfen AYT çalışmalarınızı bekletmeyin" (video: AYT NE ZAMAN?)
- "en büyük mezuna kalma sebebi ayt'ye geç başlamak" (video: AYT'YE NE ZAMAN BAŞLAMALISIN?)
- "bu benim kendi öğrencilik hayatımda... neredeyse dönemediğim bir hata" (video: BU HATADAN KAÇIN)
Psikoloji: Korku + FOMO. "Bunu bilmiyordum" hissi.
Tetikleyici: Yaygın hata var, riskin büyük.
```

**Tip 3: SORU (Curiosity Hook)**
```
Format: Direkt soru başlık = içerik sorusu
Örnekler:
- "1 soruya kaç dakika uğraşılmalı?" (video: 1 SORUYA KAÇ DAKİKA UĞRAŞILMALI?)
- "başarmak için ne lazım?" → "Zeki olmana gerek yok, temelin iyi olmasına gerek yok..." (video: BAŞARMAK İÇİN NE LAZIM?)
- "AYT'ye ne zaman başlamalısın?" (video: AYT'YE NE ZAMAN BAŞLAMALISIN?)
Psikoloji: Cevabı merak. Başlık = soru, içerik = beklenmedik cevap.
Tetikleyici: Öğrencinin kafasındaki somut soru.
```

**Tip 4: MADDE LİSTESİ (List Hook)**
```
Format: "[Konu] için [şunlar] [bitsin/yap/dene]"
Örnekler:
- "AYT feni anlayabilmek için TYT'nin bu konularını mutlaka bil" (video: AYT FENE GEÇMEDEN BUNLAR BİTSİN)
- "bu rutini dene" + içerikte liste (video: BU RUTİNİ DENE)
- "bunları eleyebilirsin" (video: BUNLARI ELEYEBİLİRSİN)
Psikoloji: Tamamlama isteği. "Şu kadar şey yapacağım" hissi.
Tetikleyici: Yapılacak liste isteniyor, net adımlar.
```

**Tip 5: BİLİŞSEL ÇARPIŞMA (Pattern Interrupt Hook)**
```
Format: "[Beklenen şey] değil. [Beklenmeyen gerçek]" veya "[İnanılan şey]... Ama öyle değil"
Örnekler:
- "sınavı kazanmak için zeki olmana gerek yok... temelin iyi olmasına gerek yok... 10 saat çalışmana da gerek yok" (video: BAŞARMAK İÇİN NE LAZIM?)
- "beyniniz dopaminin nereden geldiğini umursamaz, ne kadar geldiğini umursar" (video: BEYNİN BÖYLE ÇALIŞIYOR)
Psikoloji: Beklenmeyen = dikkat çekme. "Neden öyle?" merakı.
Tetikleyici: Yaygın inanç yanlış, gerçek farklı.
```

**Tip 6: İÇ DİYALOG (Objection Hook)**
```
Format: "Abi [öğrenci şikayeti/itirazı]... → [Oğuz'un cevabı/tespiti]"
Örnekler:
- "Abi bu zamanlar kaç saat çalışıyordun dershanem yoktu o yüzden 8-9..." (video: BİR SORU CEVAP KLASİĞİ)
- "abi 90'lara tavsiyen ne → obp'yi sallamayin matematiği sağlam tutun" 
Psikoloji: Tanıma hissi. "Bu benim durumum" algısı.
Tetikleyici: Öğrencinin itirazı var, soru var.
```

---

### B. YATAY Video Hook Tipleri (123 video analizi)

Yatay videolarda "hook" farklı işler: İlk 2-3 cümle dinlemeye devam ettirir.

**Selamlama + Konuyu Bir Cümlede Koy:**
```
"gençler Selamlar herkese [konu] videosuyla beraberiz"
"gençler hoş geldiniz [konu] konuşacağız"
Örnek: "gençler Selamlar herkese 20 saatte tyt sosyal bitirme videosu ile beraberiz"
```

**Selamlama + Neden İzlemeliyim Sorusu:**
```
Güvenilirlik kur → "biliyorum aşırı clickbait gibi duran bir başlık ama..."
"Bu videoyu neden izlemeliyim?" sorusunu hemen cevapla
Örnek (25 DAKİKADA TÜRKÇE): "clickbait falan değil... ben de 60-65-70 dakikalarda çözüyordum"
```

**Selamlama + Güncel Bağlam:**
```
"evet gençler selamlar bu video yayınlandığında..."
Öğrencinin kafasındaki güncel konuyu yakala
```

---

## BÖLÜM 2: İÇERİK YAPISI ANALİZİ

### SHORTS Yapısı (Gerçek veriden çıkarıldı)

**Yapı tipi A: RAKAM-REÇETE**
```
1. Hook: Sayısal iddia (1 cümle)
2. Neden bu rakam mümkün? (2-3 cümle)
3. Reçete: Ders + süreler (madde madde)
4. "Görüşürüz"

Örnek (20 SAATTE TYT SOSYAL):
Hook: "20 saatte tyt sosyal bitirebilirsin"
Reçete: "önce videoları veriyorum süreler..."
     CK Haritalar Kampı: 226 dk
     CK TYT Coğrafya: 290 dk
     Soner Ardıç TYT Tarih: 120 dk
     ...
     Toplam: 15 saat
Sonra: Soru kitabı önerisi
Kapanış: "netlerin hayırlı olsun görüşürüz"
```

**Yapı tipi B: UYARI-ÇÖZÜM**
```
1. Hook: Uyarı
2. Neden ciddi?
3. Ne yapmalısın?
4. "Görüşürüz"

Örnek (AYT NE ZAMAN?):
Hook: "lütfen AYT çalışmalarınızı bekletmeyin"
Neden: "çok daha fazla puan var... rakipleriniz buradan patlayacak"
Çözüm: "ayt'ye erken başlamak... sizin için çok büyük avantaj"
```

**Yapı tipi C: BİLİŞSEL ÇARPIŞMA**
```
1. Hook: Beklenmeyen gerçek
2. Mekanizma: Neden böyle?
3. Sonuç: Ne yapmalısın?
4. "Görüşürüz" yok, bazen direkt biter

Örnek (BEYNİN BÖYLE ÇALIŞIYOR):
Hook: "beyniniz dopaminin nereden geldiğini umursamaz"
Mekanizma: "önünüzde iki seçenek var: TikTok vs ders çalışmak..."
           "beyniniz hiçbir zaman kendiliğinden ders çalışmayı seçmez"
Sonuç: "sırtınızı motivasyona dayarsan... hiçbir alanda başaramazsın"
```

---

### YATAY Yapısı (Gerçek veriden çıkarıldı)

**Yapı tipi A: SORU CEVAP / REHBER**
```
1. Selamlama + konu tanıtımı (2-3 cümle)
2. İçindekiler: "Bu videoda X, Y, Z konuşacağız" (liste)
3. Madde 1: Ana konu → detay + örnek
4. Madde 2: Devam → detay + örnek
...
N. Kapanış: Özet + motivasyon
N+1. "Görüşürüz, seviliyorsunuz"
```

**Yapı tipi B: ANALİZ / STRATEJI**
```
1. Selamlama + neden bu videoyu çekiyorum
2. Genel bağlam (neden önemli)
3. Detaylı analiz (madde madde veya akış)
4. Somut tavsiye
5. "Uzun lafın kısası..." özet
6. Kapanış
```

---

## BÖLÜM 3: PROMPT SİSTEMİ YENİ MİMARİSİ

### Sorun: LLM Hook Üretemiyor

Mevcut promptta:
```
## HOOK TİPLERİ (Gerçek örneklerden)
**Sayısal İddia:** "20 saatte TYT sosyal bitirebilirsin"
...
## HOOK KURALLARI
- İlk cümle = hook, selamlama yok
- 1 cümle, maksimum 10 kelime
```

Bu yeterli değil çünkü:
1. LLM hangi tipi seçeceğini bilmiyor
2. Hook'u nasıl konu ile bağlayacağını bilmiyor
3. Hook → açıklama → içerik geçişi öğretilmemiş

### Çözüm: İçerik Üretimi Adım Adım

**System prompt'a eklenecek SHORT üretim talimatı:**

```
## SHORT ÜRETİM AKIŞI

ADIM 1: KONU ANALİZİ
Kullanıcı ne istiyor?
- Öğrencinin kafasındaki soru var mı? → TİP 3 (SORU)
- Yaygın hata/yanılgı var mı? → TİP 2 (UYARI) veya TİP 5 (ÇARPIŞMA)
- Yapılacaklar listesi mi? → TİP 4 (MADDE)
- Zaman/rakam verilebilir mi? → TİP 1 (RAKAM-REÇETE)
- İtiraz/soru-cevap var mı? → TİP 6 (İÇ DİYALOG)

ADIM 2: HOOK YAZ
Seçilen tipe göre:
- TİP 1: "[rakam] [birim]de [konu] [fiil]"
- TİP 2: "lütfen [şeyi] bekletmeyin" VEYA "[kötü şey]in sebebi [sebep]"
- TİP 3: İçeriğin en önemli sorusu + cümle formunda yaz
- TİP 4: "[konu] için [sayı] şey [yap/bil/bitir]"
- TİP 5: "[İnanılan şey] → Beklenmedik gerçek"
- TİP 6: "Abi [itiraz] → [cevap öncesi durum]"

ADIM 3: HOOK AÇIKLAMASI (2-3 cümle)
- Neden bu iddia doğru?
- Öğrencinin durumu ne?
- Ne yapmalı?

ADIM 4: REÇETE/ÇÖZÜM (3-5 madde)
- Her madde 1 cümle
- Somut, uygulanabilir, net
- Eğer rakam verilmişse: tarih/saat/kaynak spesifik

ADIM 5: KAPANIS
"Görüşürüz" veya "netlerin hayırlı olsun, görüşürüz"
```

**System prompt'a eklenecek YATAY üretim talimatı:**

```
## YATAY ÜRETİM AKIŞI

ADIM 1: SELAMLAMA (2 cümle)
"Gençler selamlar herkese." + "[Konu] videosuyla beraberiz."

ADIM 2: BAĞLAM KUR (1-2 cümle)
Neden bu konuyu konuşuyoruz?
Neden önemli?

ADIM 3: İÇİNDEKİLER (opsiyonel ama uzun videolarda güçlü)
"Bu videoda X, Y, Z konuşacağız"

ADIM 4: ANA İÇERİK
Her madde için:
- Soru veya başlık
- Oğuz Usta'nın cevabı
- Neden? Örnek.
- Somut tavsiye
- "Yani..." ile özetle

ADIM 5: KAPANIS
"Uzun lafın kısası..." + özet 1-2 cümle
"Görüşürüz, seviliyorsunuz."
```

---

## BÖLÜM 4: UYGULAMA PLANI

### Tek Dosya Yaklaşımı: prompts.ts Güncelle

Tüm mantığı `lib/prompts.ts` içine entegre et — ayrı modül dosyaları yazmak yerine prompt string'lerini zenginleştir.

**Ne değişecek:**

```
MEVCUT prompts.ts:
- OGUZ_USTA_SHORT (basit kurallar)
- OGUZ_USTA_YATAY (basit kurallar)

YENİ prompts.ts:
- OGUZ_USTA_SHORT (gerçek hook tipleri + üretim adımları)
- OGUZ_USTA_YATAY (gerçek yapı adımları + içindekiler)
- HOOK_EXAMPLES (gerçek Oğuz örnekleri)
```

**Dosya yapısı:**

```typescript
// lib/prompts.ts

// Gerçek veriden çıkarılan hook örnekleri
const HOOK_EXAMPLES_SHORT = `...`

// SHORT üretim sistemi
const OGUZ_USTA_SHORT = `...`

// YATAY üretim sistemi
const OGUZ_USTA_YATAY = `...`

// YKS know-how (mevcut)
import { YKS_KNOWLEDGE } from "./yks-knowledge"
```

---

## BÖLÜM 5: SONUÇ KARŞILAŞTIRMASI

### Mevcut Çıktı (Sorunlu):
```
🦉 AYT Tarih'ten 20 yapmanız çok normal

Yani sınavda karşınıza hiç bilmediğiniz olaylar çıkabilir...
- Milletime kesinlikle ağırlık verin
- Osmanlı dönemini parçalara bölün
...
Görüşürüz
```

**Sorunlar:** Hook yok (açıklama gibi), maddeler soyut, YKS bilgisi yok, Oğuz'un gerçek tarzı değil

### Beklenen Çıktı (Gerçek Oğuz Tarzı):
```
🦉 AYT Tarih'te 20 net almak mümkün — rakibinin %80'i bunu bilmiyor

Sözelciysen 20 tarih sorusu var. Bunları boş bırakırsan 80 puanlık kayıp. 
EA'cıysan 10 soru, ama o 10 soruyu yapmayan her sene mezuna kalıyor.

İşte adım adım reçete:
1. TYT Tarih'i önce bitir — Soner Ardıç 7 Günde TYT Tarih (120 dakika)
2. AYT'de kronoloji değil sebep-sonuç öğren
3. Her olay için: Ne oldu → Neden → Sonucu ne?
4. ÖSYM soru tipi: Karşılaştırma + sebep-sonuç (ezber değil mantık)
5. Yanlış defteri: Her yanlış → Neden yanlış? → Doğrusu nedir?

Yanlış tarih çalışmak = ezberlemeye çalışmak = sınav da yıkılmak.

Görüşürüz 💜
```

**Fark:** Spesifik rakam, Oğuz'un gerçek kaynağı (Soner Ardıç), sebep-sonuç açıklaması, "yanlış yaygın inanç → doğru" kontrast

---

## ÖZET: YAPILACAKLAR

| # | Dosya | Değişiklik |
|---|-------|------------|
| 1 | `lib/prompts.ts` | `OGUZ_USTA_SHORT` → 6 hook tipi + üretim adımları + gerçek örnekler |
| 2 | `lib/prompts.ts` | `OGUZ_USTA_YATAY` → selamlama + içindekiler + akış + kapanış |
| 3 | `lib/prompts.ts` | `HOOK_EXAMPLES` constant ekle (gerçek örnekler) |
| 4 | `lib/yks-knowledge.ts` | Kaynak açıklamalarına "neden bu kaynak" ekle |
| 5 | Test | Instagram script + TikTok video test |
