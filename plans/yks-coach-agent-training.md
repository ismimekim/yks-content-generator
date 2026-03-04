# YKS Coach Agent Eğitim Planı

## Mevcut Durum

**Başarılar:**
- ✅ Format doğrulandı (Hook → Yani → Peki → Taktik → Görüşürüz)
- ✅ Context disambiguation (Mart ayı = YKS stratejisi, konu değil)
- ✅ 233 video transkripti (~700K kelime)
- ✅ YKS domain knowledge extraction

**Eksiklik:**
- ❌ İçerik derinliği sığ (2-3 taktik)
- ❌ 5+ senelik koçu deneyimi yok
- ❌ YKS spesifik nuance eksik

---

## 3 Yaklaşım Karşılaştırması

### 1. Fine-Tuning (Kendi Modelini Eğit)

**Nasıl Çalışır:**
- Oğuz Usta transkriptleri ile modeli fine-tune et
- Model Oğuz Usta'nın "düşünme tarzını" öğrenir

**Artıları:**
- En doğal sonuç
- Oğuz Usta voice'unu yakalar

**Eksileri:**
- GPU gerekli (pahalı)
- Zaman alıcı (saatlar/günler)
- Model update'i zor

**Maliyet:** $$-$$$ (GPU + zaman)

### 2. RAG (Retrieval-Augmented Generation)

**Nasıl Çalışır:**
- 233 video transkriptini vektör veritabanına yükle
- Her soruda ilgili transkript parçalarını çeker
- LLM ilgili context ile cevap verir

**Artıları:**
- Hızlı implementasyon
- Her zaman yeni data ekleyebilirsin
- Kaynak gösterebilir (transkript linki)

**Eksileri:**
- Vektör DB gerekli (Pinecone, Weaviate)
- Ek latency

**Maliyet:** $ (Vektör DB + API calls)

### 3. Prompt Engineering (Mevcut Yaklaşım)

**Nasıl Çalışır:**
- YKS knowledge'ı prompt'a göm
- Few-shot examples ekle
- Chain-of-thought reasoning

**Artıları:**
- En hızlı
- Ek maliyet yok
- Anında update edilebilir

**Eksileri:**
- Context window limiti
- Model knowledge cutoff

**Maliyet:** - (Zaten yapılıyor)

---

## Hybrid Yaklaşım (Önerilen)

### Phase 1: Prompt Engineering (Şimdi)
✅ Zaten yapılıyor
✅ YKS_KNOWLEDGE ekli
✅ Context disambiguation eklendi

### Phase 2: RAG Entegrasyonu (Sonraki)
**Vektör DB:** Weaviate veya Pinecone
**Data:** 233 video transkripti chunk'lara böl
**Retrieval:** Semantic search ile ilgili parçaları getir

**Prompt:**
```
KULLANICI: "Mart ayı için YKS stratejisi"

RETRIEVED CONTEXT (RAG):
[Oğuz Usta - Mart ayı çalışma planı video]
"Mart ayı kritiktir çünkü..."
[Oğuz Usta - AYT hazırlık]
"AYT'ye erken başlamalısın..."
[Baykuş Mentörlük - Çalışma düzeni]
"Rutin oluşturmanın 3 adımı..."

Şimdi bu context kullanarak script üret.
```

### Phase 3: Fine-Tuning (Opsiyonel)
- QLoRA ile 4-bit fine-tuning
- Single GPU ile mümkün
- Oğuz Usta voice'unu yakalar

---

## En Hızlı Çözüm: Enhanced RAG-lite

**Vektör DB olmadan, simple chunk retrieval:**

1. **233 video transkriptini chunk'lara böl** (her chunk 500 kelime)
2. **Semantic search** (OpenAI embeddings veya local)
3. **Top 3 chunk'ı prompt'a ekle**

**Implementasyon:**
```typescript
// lib/yks-rag.ts
interface YKSChunk {
  source: string;  // "oguz_usta", "baykus", etc.
  videoId: string;
  content: string;
  keywords: string[];  // "mart", "ayt", "deneme analizi"
}

async function retrieveYKSContext(query: string): Promise<YKSChunk[]> {
  // Simple keyword + semantic search
  // Return top 3 relevant chunks
}
```

---

## Karar Matrisi

| Yaklaşım | Hız | Maliyet | Kalite | Öncelik |
|----------|-----|--------|--------|---------|
| Prompt Engineering | ⚡⚡⚡ | - | 7/10 | Şimdi |
| RAG-lite (simple) | ⚡⚡ | $ | 8/10 | Sonraki |
| Full RAG (vektör) | ⚡ | $$ | 9/10 | Opsiyonel |
| Fine-tuning | 💤 | $$$ | 10/10 | Long-term |

**Öneri:** Önce Prompt Engineering'i maksimize et, sonra RAG-lite ekle.

---

## Prompt Engineering İyileştirmeleri (Hemen Yapılabilir)

### 1. YKS Takvimi Knowledge Ekle

```
## YKS TAKVİMİ (5+ Senelik Koçu Bilgisi)

**Kritik Dönemler:**
- **Eylül-Ekim**: 11. sınıf AYT konuları başlar
- **Kasım-Aralık**: TYT + AYT dengesi
- **Ocak-Şubat**: Mezunlar için geri sayım
- **Mart**: GEÇİŞ AYI (kritik!) - AYT konu bitirme
- **Nisan**: Son düzeltme, deneme analizi
- **Mayıs**: Sınav ayı, az çalışma, stres yönetimi

**Mart Ayı Stratejisi:**
- Mart = "Haziran'a sayılı ay"
- AYT konu bitirme için son şans
- TYT rutini sabitleme zamanı
- Deneme analizi + plan güncelleme

**Nisan-Mayıs Stratejisi:**
- Konu değil, soru çözümü
- Deneme analizi + eksik kapama
- Rutin koruma (disiplin kritik)
```

### 2. Deneme Analizi Framework

```
## DENEME ANALİZİ (Koçu Level)

**3 Adım Analiz:**
1. **Net Hesapla:** Her branşta net
2. **Branş Karşılaştır:** Hangi branş sorun?
3. **Konu Tespiti:** Yanlış soruların konuları

**Yanlış Türleri:**
- **Bilgi Eksikliği:** Konuyu bilmiyorsun → Konu çalış
- **Mantık Hatası:** Konuyu biliyorsun ama çözemiyorsun → Soru çözümü
- **İhmal:** Çok saat ama net artışı yok → Strateji değiştir

**Mart Ayı Deneme Stratejisi:**
- Haftada 1 deneme (Salı veya Çarşamba)
- Analizi aynı gün (gecelik kaybı olmasın)
- Nisan planını analizden çıkar
```

### 3. Mezun vs 12. Sınıf Stratejisi

```
## MEZUN STRATEJİSİ

**Avantaj:**
- Tüm konuları görmüşsün
- Daha fazla zamanın var

**Dezavantaj:**
- OBP katsayısı düşük
- Disiplin kopması riski

**Mart Ayı Mezun Planı:**
- 8-10 saat çalışma (sabah erken başla)
- Zayıf branşa odaklan
- Her gün deneme + analiz
- Akşam eksik konu çalışması
```

---

## Implementasyon Planı

### Phase 1: Prompt Enhancement (Şimdi - 1 saat)
- YKS Takvimi knowledge ekle
- Deneme Analizi framework ekle
- Mezun vs 12. sınıf stratejisi ekle
- Daha spesifik few-shot examples

### Phase 2: RAG-lite Implementation (1-2 gün)
- 233 video transkriptini chunk'lara böl
- Simple retrieval function
- Prompt'a context ekleme

### Phase 3: Test ve Iterate (Sürekli)
- Her test sonucunu analyze et
- Prompt'u güncelle
- YKS knowledge'u genişlet

---

**Sonraki Adım:** Hangi phase'den başlamak istersin?
