# Instagram Reels Transcript Extraction - Complete Analysis

## 🎯 Core Finding

**Kısa Cevap:** Instagram Reels için doğrudan transkript sağlayan GitHub repo YOK.

İki adımlı yaklaşım şart:
1. **Video İndirme** → GitHub araçları ile mümkün
2. **Transkripsiyon** → Speech-to-Text API'ler gerekiyor (ücretsiz tier'ler mevcut)

---

## 📊 GitHub Repositories Analizi

### En İyi 3 Araç (Test Edilmeye Değer)

| Repository | Stars | Kullanım Kolaylığı | Instagram Reels | Dökümantasyon |
|-----------|-------|-----------------|----------------|--------------|
| **InstagramProToolkit** | 48 | ⭐⭐⭐⭐⭐ | ✅ | ⭐⭐⭐⭐⭐ |
| **Insta-Downloader** | 29 | ⭐⭐⭐⭐ | ✅ | ⭐⭐⭐⭐ |
| **ig-dm-reels-autodownload** | 22 | ⭐⭐⭐ | ✅ | ⭐⭐⭐⭐ |

### Detaylı Bilgiler

#### 1. shivamk21-ssk/InstagramProToolkit
- **License:** MIT
- **Python**: `pip install InstagramProToolkit`
- **Özellikler:**
  - Reels indirme (video + metadata)
  - Caption extraction
  - Comment extraction
  - Like/view count
  - Profil scraping
  - Telegram bot entegrasyonlu

```python
from instagram_pro_toolkit import InstagramProToolkit

profile = InstagramProToolkit("username")
posts = profile.get_posts()

for post in posts:
    if post.is_video:
        print(f"Caption: {post.caption}")
        print(f"Video URL: {post.video_url}")
        print(f"Views: {post.view_count}")
        profile.download_reel(post, save_path="./downloads/")
```

#### 2. Masterolic/Insta-Downloader
- **License:** MIT
- **Python**: `pip install insta-downloader`
- **Özellikler:**
  - Reels indirme
  - Post indirme
  - Story indirme
  - Profil fotoğrafı indirme

```python
from instadownloader import InstagramDownload

dl = InstagramDownload()
dl.download_reel(
    url="https://www.instagram.com/reel/xxxxx",
    save_path="./reels/",
    filename="reel1.mp4"
)
```

#### 3. ig-dm-reels-autodownload
- **License:** MIT
- **Python**
- **Özellikler:**
  - DM'den gelen reels otomatik indirme
  - Telegram bot entegrasyonu
  - Multi-threaded indirme

---

## 🔧 Transkripsiyon Seçenekleri

### Seçim 1: OpenAI Whisper API (Önerilen)

**Neden?**
- ✅ Türkçe desteği var
- ✅ Ücretsiz (Python paketi olarak)
- ✅ Bazı vendor GPU sunuyor (ücretsiz)

**Kurulum:**
```bash
pip install openai-whisper
```

**Kullanım:**
```python
import whisper

model = whisper.load_model("base")  # base, small, medium, large
result = model.transcribe("reel1.mp4", language="tr")

with open("transcript.txt", "w", encoding="utf-8") as f:
    f.write(result["text"])
```

**Maliyet:** 
- Local: Ücretsiz (CPU yavaş, GPU hızlı)
- API: $0.006/dakika (OpenAI)

### Seçim 2: Google Cloud Speech-to-Text

**Neden?**
- ✅ Türkçe desteği çok iyi (96%+ accuracy)
- ✅ 60 dakika/ay ücretsiz
- ✅ Otomatik dil detection

**Kurulum:**
```bash
pip install google-cloud-speech
gcloud auth login
```

**Kullanım:**
```python
from google.cloud import speech

client = speech.SpeechClient()
audio = open("reel1.mp4", "rb").read()

config = speech.RecognitionConfig(
    language_code="tr-TR",
    enable_automatic_punctuation=True
)

response = client.recognize(config=config, audio=audio)
print(response.results[0].alternatives[0].transcript)
```

### Seçim 3: Google Colab (Ücretsiz GPU)

**Neden?**
- ✅ Ücretsiz GPU
- ✅ Kurulum yok
- ✅ Jupyter notebook ile

**Kod:**
```python
!pip install git+https://github.com/openai/whisper.git
!pip install yt-dlp

import whisper
model = whisper.load_model("large")

# Google Drive'a yükle veya URL'den indir
result = model.transcribe("reel1.mp4", language="tr")
print(result["text"])
```

---

## 🚀 Önerilen Pipeline

### Stage 1: Test (Şimdi)
**Amaç:** 10-20 Instagram Reel'i manuel analiz et

1. **Manuel İndirme:**
   - Instagram profilinize git
   - Reels'i screen recording ile kaydet
   - veya IG:DM bot'a gönder

2. **Transkripsiyon:**
   - Google Colab aç
   - Whisper model yükle
   - Videoları yükle
   - Transkripti al

3. **Analiz:**
   - Transkriptleri incele
   - YKS konuşma tarzında mı?
   - Sık kullanılan kelimeler?
   - Hook pattern'ler?

**Sonuç:** Analiz sonucuna göre Instagram için ayrı bir SHORT variant oluşturmak

### Stage 2: Otomasyon (Eğer Stage 1 başarılıysa)

**Script Yaz:**
```python
# scripts/download_instagram_reels.py

import os
from instagram_pro_toolkit import InstagramProToolkit
import whisper

def download_reels(username, count=10):
    toolkit = InstagramProToolkit(username)
    posts = toolkit.get_posts()[:count]
    
    for i, post in enumerate(posts, 1):
        if post.is_video:
            # Download video
            filename = toolkit.download_reel(
                post, 
                save_path=f"./data/instagram_reels/{username}/"
            )
            
            # Transcribe
            model = whisper.load_model("base")
            result = model.transcribe(
                f"./data/instagram_reels/{username}/{filename}",
                language="tr"
            )
            
            # Save transcript
            with open(f"./data/instagram_reels/{username}/{i}.txt", "w") as f:
                f.write(f"# {post.caption}\n\n")
                f.write(result["text"])
    
    print(f"✅ {count} reels downloaded and transcribed")

# Kullanım
download_reels("oguzusta", count=20)
```

### Stage 3: Analiz ve Entegrasyon

1. Transkriptleri [`lib/yks-knowledge.ts`](lib/yks-knowledge.ts)'e ekle
2. Instagram için ayrı bir `OGUZ_USTA_INSTAGRAM` prompt variantı oluştur
3. Instagram-spasifik hook pattern'lerini analiz et
4. Model'i güncelle

---

## 💡 Stratejik Öneri

### Seçenek A: YouTube Shorts'a Odaklan (ÖNERİLEN)

**Neden?**
- ✅ 100 YouTube Short zaten elimizde (temiz transkriptler)
- ✅ Auto-caption (YouTube Studio'dan)
- ✅ Oğuz'un Instagram'ı da YouTube Shorts'a yüklüyor olabilir
- ✅ Instagram Reels farklı formatta olabilir (15-60s, daha trend odaklı)

**Action Plan:**
1. Mevcut 100 short analizini derinleştir
2. Instagram için variant'ı mevcut SHORT prompt'tan türet
3. Farkları sadece minor:
   - Instagram = Daha trend odaklı, emoji kullanımı
   - YouTube Shorts = YKS odaklı, eğitim odaklı
4. Test et ve düzelt

### Seçenek B: Instagram Reels Manuel Toplama

**Neden?**
- ✅ Küçük örnek (10-20 reel)
- �izden geçmiş Instagram'da test etme şansın
- ✅ Transkript kalitesini kontrol edebilirsin

**Action Plan:**
1. Oğuz Usta'nın Instagram profilinden 10 reel manuel topla
2. Google Colab'da transkript et
3. Analiz et
4. Prompt'a ekle

### Seçenek C: Full Otomasyon (Sonraki Adım)

**Neden?**
- ✅ Scalable (100+ reel)
- ✅ Sürekli güncellenebilir
- ✅ Mevcut YouTube pipeline'a benzer

**Action Plan:**
1. InstagramProToolkit + Whisper pipeline kur
2. 100 reel indir + transkript et
3. Analiz et ve data ekle
4. Prompt'u güncelle

---

## 🎯 Sonuç

**Kısa Vadeli (Şu an yapılabilir):**
1. YouTube Shorts'a odaklan (zaten 100 temiz veri)
2. Instagram için variant türet (daha trend odaklı, emoji kullanımı)
3. Manuel 5-10 Instagram Reel test et

**Uzun Vadeli:**
1. InstagramProToolkit kurulumu
2. Whisper + Google Colab pipeline
3. Batch processing
4. 100+ Instagram Reel veritabanı

---

*Research Date: March 2, 2026*
*Status: Ready for Stage 1 (YouTube Shorts focus)*
