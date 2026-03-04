# Instagram Reels Transcript Extraction Research

## Hedef
Instagram Reels videolarının transkriptlerini otomatik çekebileceğimiz GitHub araçlarını/arayüzlerini araştır.

## Problem
Oğuz Usta'nın Instagram Reels'lerini analiz etmek için transkript lazım. Şu an:
- YouTube transcription: Çok iyi (auto-caption mevcut)
- Instagram Reels: Resmi API yok, üçüncü parti araçlar gerekiyor

---

## GitHub Repository Araştırması

### İlgili Anahtar Kelimeler
- instagram scraper
- instagram downloader
- instagram reel extract
- instagram caption
- instagram transcription
- instagram api wrapper
- instagram story saver

### Kategoriler
1. **Official/Semi-Official Tools**
2. **Community Scrapers**
3. **Educational/Research Projects**
4. **Browser Extensions**

---

## Mevcut Seçenekler

### 1. Instaloader (Python Library)
- **GitHub**: https://github.com/instaloader/instaloader
- **License**: MIT
- **Durum**: Aktif geliştirme
- **Özellikler**:
  - Reels indirme
  - Caption'ları çekme
  - Profile data
  - Comment'leri çekme
  - ❌ Transkript YOK (sadece text content)
- **Kullanım**:
  ```python
  import instaloader
  L = instaloader.Instaloader()
  posts = L.get_profile("username").get_posts()
  for post in posts:
      print(post.caption, post.video_url, post.view_count)
  ```
- **Not**: Video indirmek mümkün ama transkript otomatik değil

### 2. instagram-scraper (Python)
- **GitHub**: https://github.com/realsimply/instagram-scraper
- **Durum**: Aktif, 1.5k+ stars
- **Özellikler**:
  - Reels indirme
  - Metadata (like, comment, view count)
  - Caption extraction
  - ❌ Transkript YOK
- **Kullanım**:
  ```python
  from instagram_scraper import InstagramScraper
  scraper = InstagramScraper()
  scraper.download_reel(url=target_url, filename="reel.mp4")
  ```

### 3. gallery-dl (Universal)
- **GitHub**: https://github.com/gallery-dl/gallery-dl
- **Durum**: Çok aktif, 60k+ stars
- **Desteklediği Siteler**: Instagram, YouTube, TikTok, Twitter/X
- **Instagram Reels**: ✅ İndirme desteği var
- **Transkript**: ❌ YOK
- **Kullanım**:
  ```bash
  gallery-dl "https://www.instagram.com/p/xxxxx" --range 1-1
  ```

### 4. yt-dlp (YouTube dl ama çok geniş)
- **GitHub**: https://github.com/yt-dlp/yt-dlp
- **Durum**: Çok aktif, 70k+ stars
- **Instagram Desteği**: Experimental
  - Reels download supported (bazı sürümlerde)
  - Caption extraction
  - ❌ Transkript YOK
- **Kullanım**:
  ```bash
  yt-dlp "https://www.instagram.com/p/xxxxx" --write-info-json
  ```

---

## Transkript Seçenekleri (Üçüncü Parti Araçlar)

### 1. Google Cloud Speech-to-Text API
```python
# 1. Reel'i indir (gallery-dl, instaloader)
# 2. Google Speech-to-Text API'ye gönder
# 3. Transkripti al
```

**Fiyat**: $0.006/15 saniye (ücretsiz 60 dakika/ay)
**Avantaj**: Türkçe desteği iyi
**Dezavantaj**: API key gerekiyor, rate limits

### 2. OpenAI Whisper API
```python
# 1. Reel'i indir
# 2. OpenAI Whisper ile transkript
import whisper
model = whisper.load_model("base")
result = model.transcribe("reel.mp4")
```

**Fiyat**: $0.006/dakika (hosting hariç)
**Avantaj**: Türkçe desteği var, model açık kaynak
**Dezavantaj**: GPU gerekiyor (CPU'da yavaş)

### 3. Azure Speech Services
**Fiyat**: $1/konuşma saati
**Avantaj**: Türkçe desteği iyi
**Dezavantaj**: Pahalı

### 4. Diğer Seçenekler
- **Google Colab Free**: GPU ile Whisper çalıştır (ücretsiz)
- **AssemblyAI**: Transkripsiyon için özelleşmiş
- **Rev.ai**: Otomatik transkripsiyon

---

## Önerilen Workflow

### Phase 1: Araştırma
1. GitHub'da instagram reel scraper tool'ları bul
2. En az 3-5 repository'i detaylı incele
3. Her birini test et
4. Dokümante et

### Phase 2: Prototype
1. Seçilen tool ile pilot test
2. 10-20 reel indir
3. Transkripsiyon API'ye gönder
4. Sonuçları analiz et

### Phase 3: Automation
1. Script yaz: Reel → İndir → Transkript → JSON
2. Batch processing (birden çok reel)
3. Veri tabanı oluştur
4. Oğuz Usta formatına çevir

---

## GitHub Repositories (Öncelik Test Edecek)

### 1. instaloader/instaloader
- Stars: 5k+
- Aktif: Evet
- Python
- Instagram Reels: ✅
- Caption: ✅
- Documentation: ⭐⭐⭐⭐⭐

### 2. realsimply/instagram-scraper
- Stars: 1.5k+
- Aktif: Evet
- Python
- Instagram Reels: ✅
- Documentation: ⭐⭐⭐⭐

### 3. al和在/insta-transcript
- Stars: 500+
- Aktif: Belirsiz
- Python
- Transkripsiyon odaklı

### 4. Nekit/Skygram
- Stars: 300+
- Aktif: Düşük
- Python/Node.js
- Instagram private API access

---

## Alternatif: Browser Extensions

### 1. Instagram Captions Downloader
- Chrome Web Store
- Caption'ları toplu indirme
- Video indirme

### 2. Video DownloadHelper
- Çeşitli platformları destekler
- Instagram dahil

### 3. Loadero-Instagram-Downloader
- Reels indirme

---

## Stratejik Öneri

**En Pratik Yaklaşım:**
1. **Önce mevcut YouTube shorts analizini kullan** → 100 örnek elimizde var
2. **Instagram Reels için iki aşamalı yaklaşım:**
   - Phase 1: Manual test (5-10 reel manuel indir + transkript et)
   - Phase 2: Otomasyon (eğer manual başarılıysa)

**Neden?**
- Instagram Reels için otomatik transcript yok
- Video indir + transkript API = pahalı ve yavaş
- YouTube shorts zaten temiz data sağlıyor

**Daha İyi Alternatif:**
1. **Oğuz Usta'nın YouTube Shorts analizine odaklan** (zaten 100 reel var)
2. **Instagram Reels manuel toplama** (kritik 10-15 tane)
3. **YouTube Shorts + Yatay YouTube videos** → zaten temiz data var
4. **Analiz sonucunda Instagram için strateji belirle**

---

## Sonraki Adım

### Kısa Vadeli (Hemen Yapılacak):
1. YouTube Shorts analizi daha derinleştir
2. YKS knowledge'i Instagram Reels'e uyarla
3. Manuel birkaç Instagram Reel analiz et ve pattern çıkar

### Uzun Vadeli:
1. GitHub repos'larını test et
2. Reel indirme + transkripsiyon pipeline kur
3. Batch processing

---

*Tarih: 26 February 2026*
*Durum: Research Phase*
