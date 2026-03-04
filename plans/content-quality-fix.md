# Content Quality Fix Plan

## Tespit Edilen Sorunlar

**Gerçek kullanıcı çıktısı:**
```
Gençler, AYT Tarih'te yüzde doksanı aynı hatayı yapıyor.
...
Konu bazlı: Osmanlı ıslahat...
```

### Sorun 1: SHORT Formatında Selamlama Var
**Beklenen:** Hook → direkt içerik
**Olan:** "Gençler, AYT Tarih'te..."

**Neden:** `OGUZ_USTA_YATAY` prompt'unda selamlama var, SHORT'da yok
- Platform detection: `tiktok` = SHORT
- Ama "selamlama YASAK" kuralı sadece SHORT prompt'un sonunda
- YATAY prompt'unda selamlama var ve kullanılıyor

### Sorun 2: Liste Başlığı Hala Var
**Beklenen:** Doğal akış
**Olan:** "Konu bazlı:"

**Neden:** 
1. "KRİTİK KURALLAR" section'ı var ama uygulanmıyor
2. Prompt içinde "liste başlıkları YASAK" diyoruz ama model yine de yapıyor
3. Daha güçlü bir yaklaşım şart

### Sorun 3: Format Detection
**Kullanıcı:** Instagram Post
**Beklenen:** SHORT (selamlamasız)
**Olan:** YATAY (selamlamalı)

---

## Çözüm Stratejisi

### 1. SHORT Formatına ÖZEL Prompt
YATAY prompt'u ayır, tam SHORT-specific prompt oluştur:

```typescript
const OGUZ_USTA_SHORT_ONLY = `# OĞUZ USTA SHORT ONLY (SELAMLAMASIZ)

## KURALLAR:
1. İlk satır = HOOK (selamlama YOK, "Gençler" YOK)
2. Hook'tan sonra direkt içerik
3. "Yani...", "Peki..." gibi bağlaçlarla akış
4. "Görüşürüz" ile bitir

## YASAKLAR:
❌ "Gençler selamlar"
❌ "Merhaba herkese"
❌ "Şunlara bak:"
❌ "Konu bazlı:", "Bunlar şunlar:"
❌ "1. 2. 3." numaralandırma

## ZORUNLULAR:
✅ İlk satır = Hook (şaşırtıcı iddia)
✅ "yani" ile açıklama
✅ "görüşürüz 🦉" ile kapanış
✅ Doğal konuşma dili
`;
```

### 2. Prompt İyileştirme Taktiği

**Şu anki sorun:**
- Prompt çok büyük (8000+ chars)
- Model bazı kuralları uyguluyor bazılarını yapmıyor
- "YASAK" demek yerine "ZORUNLU" daha etkili

**Daha etkili yaklaşım:**
1. Short prompt'u AYRI bir dosyaya
2. Gerçek örnekler ekle (few-shot learning)
3. Negatif örnekler de ekle (yanlış örnekler)
4. Model output'unu kendini değerlendirmesini iste

### 3. Example-Based Learning

```
## DOĞRU ÖRNEK:
🦉 AYT Tarihte 20 soruyu çözmek için tarih bilmen gerekmiyor.

Yani çoğu öğrenci ezber yapıyor ama çözemiyorlar. Çünkü AYT Tarih ezber değil, 
bağlantı dersi. Sorular "ne zaman" değil "neden" soruyor.

Peki ne yapmalısın?
Yani şunu yap: Her konuyu okurken "bu olay neden oldu" diye sor. Sonra soru çöz.
En önemlisi deneme analizinde bağlantı hatalarını bul.

Görüşürüz.

## YANLIŞ ÖRNEK (ASLA BU):
Gençler selamlar! AYT Tarihte şunlar yapmalısın:
1. Ezber yap
2. Soru çöz
3. Deneme çöz
```

---

## Implementation Plan

1. **lib/prompts.ts'i modülerize et**
   - CORE: Ortak kurallar
   - SHORT_ONLY: Selamlamasız, hook-first
   - YATAY_ONLY: Selamlamalı, akışlı

2. **Few-shot examples ekle**
   - 3 doğru örnek
   - 2 yanlış örnek (ne YAPILMAMASI gerektiğini göster)

3. **Output validation ekle**
   - Sonuç çıktısını kontrol et
   - Selamlama var mı? Liste başlığı var mı?
   - Yanlışsa düzelt ve retry et

---

*Status: Planning*
*Next: Implementation*
