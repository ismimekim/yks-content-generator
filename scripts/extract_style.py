#!/usr/bin/env python3
"""
Style Extractor - Derin Kalıp Çıkarımı
Başlık + Transkript'ten Oğuz Usta tarz kalıplarını çıkarır

Kullanım:
    python3 extract_style.py data/oguz_usta_yatay.json oguz_usta_yatay
    python3 extract_style.py data/oguz_usta_shorts.json oguz_usta_shorts
"""
import json
import re
import sys
from pathlib import Path
from collections import Counter
from datetime import datetime
from typing import Dict, List, Any, Tuple


# =============================================================================
# PATTERN EXTRACTION FUNCTIONS
# =============================================================================

def extract_opening_formulas(text: str, max_sentences: int = 3) -> List[str]:
    """Giriş formüllerini çıkar - ilk 1-3 cümle"""
    # Cümle bölmek için
    sentences = re.split(r'[.!?]+\s*', text.strip())
    valid = [s.strip() for s in sentences if len(s.strip()) > 10][:max_sentences]
    return valid


def extract_closing_formulas(text: str, max_sentences: int = 2) -> List[str]:
    """Kapanış formüllerini çıkar - son 1-2 cümle"""
    sentences = re.split(r'[.!?]+\s*', text.strip())
    non_empty = [s.strip() for s in sentences if len(s.strip()) > 3]
    return non_empty[-max_sentences:] if len(non_empty) >= max_sentences else non_empty


def extract_explanation_patterns(text: str) -> List[str]:
    """Açıklama kalıplarını bul - "hani şöyle", "yani", vs."""
    patterns = [
        r'\bhani\s+ş[öo]yle\b',
        r'\byani\b',
        r'\bkastedilen\s+şu\b',
        r'\bdemem\s+o+ ki\b',
        r'\bşöyle\s+düş[üu]n\b',
        r'\baklıyorsan[ıi]z\b',
    ]
    found = []
    for pattern in patterns:
        matches = re.findall(pattern, text, re.IGNORECASE)
        found.extend(matches)
    return list(set([m.lower() for m in found]))


def extract_emphasis_patterns(text: str) -> List[str]:
    """Vurgu kalıplarını bul - "asla", "kesinlikle", vs."""
    patterns = [
        r'\basla\b',
        r'\bkesinlikle\b',
        r'\bmutlaka\b',
        r'\bhi[çc]bir\s+şekilde\b',
        r'\byok\s+h[üu]km[üu]nd[ei]r\b',
        r'\bhi[çc]\b',
        r'\bkatiyen\b',
        r'\bşart\b',
        r'\bzorunlu\b',
        r'\bger[ęe]k\b',
    ]
    found = []
    for pattern in patterns:
        if re.search(pattern, text, re.IGNORECASE):
            found.extend(re.findall(pattern, text, re.IGNORECASE))
    return list(set([m.lower() for m in found]))


def extract_casual_patterns(text: str) -> List[str]:
    """Samimiyet kalıplarını bul - "valla", "abi", vs."""
    patterns = [
        r'\bvalla\b',
        r'\bolm\b',
        r'\bkanka\b',
        r'\babb?\s+?[a-z]?b\b',  # abi, ab
        r'\bkuzen\b',
        r'\bbak\b',
    ]
    found = []
    for pattern in patterns:
        if re.search(pattern, text, re.IGNORECASE):
            found.extend(re.findall(pattern, text, re.IGNORECASE))
    return list(set([m.lower() for m in found]))


def extract_transitions(text: str) -> List[str]:
    """Geçiş kelimelerini bul"""
    patterns = [
        r'\bşimdi\s+gençler?\b',
        r'\bşimdi\s+kadın\b',
        r'\bpeki\b',
        r'\bevet\s+sevgili\b',
        r'\bevet\s+gençler\b',
        r'\bhadı\s+bugün\b',
        r'\bakşam\s+oldu\b',
        r'\bsonra\s+da\b',
        r'\bundansonra\b',
        r'\bdiğer\s+taraf\b',
        r'\bbunu\s+bir\s+kenara\s+koyalım\b',
        r'\bgelelim\b',
    ]
    found = []
    for pattern in patterns:
        matches = re.findall(pattern, text, re.IGNORECASE)
        found.extend(matches)
    return list(set([m.lower() for m in found]))


def extract_address_terms(text: str) -> List[str]:
    """Hitap şekillerini bul"""
    patterns = [
        r'\babiler?\b',
        r'\bgençler\b',
        r'\bcanım\b',
        r'\bkanka\b',
        r'\barkadaşlar?\b',
        r'\bsevgili\s+\d+\s*[\']?l[ae]r?\b',
        r'\bsevgili\s+gençler\b',
        r'\b[ıi]yi\s+dinleyenler\b',
        r'\bd[ıi]kkatle\b',
    ]
    found = []
    for pattern in patterns:
        matches = re.findall(pattern, text, re.IGNORECASE)
        found.extend([m.lower() for m in matches])
    return list(set(found))


def extract_emojis(text: str) -> List[str]:
    """Emojileri çıkar"""
    emoji_pattern = re.compile(
        "["
        "\U0001F600-\U0001F64F"
        "\U0001F300-\U0001F5FF"
        "\U0001F680-\U0001F6FF"
        "\U0001F1E0-\U0001F1FF"
        "\U00002702-\U000027B0"
        "\U000024C2-\U0001F251"
        "\U0001F900-\U0001F9FF"
        "]+"
    )
    return list(set(emoji_pattern.findall(text)))


def extract_number_formats(text: str) -> List[Tuple[str, int]]:
    """Sayı formatlarını bul (örn: "35 net", "120 gün")"""
    # Sayı + kelime patternleri
    pattern = r'\b(\d+)\s+(net|gün|saat|hafta|ay|soru|dk|dakika|video|deneme|puan|defa|kez|ay|sene|yıl)\b'
    matches = re.findall(pattern, text, re.IGNORECASE)
    formatted = [f"{num} {unit}" for num, unit in matches]
    return Counter(formatted).most_common(30)


def categorize_content(title: str, content: str) -> str:
    """İçeriği kategoriize et"""
    title_lower = title.lower()

    # Konuk görüşmesi
    if re.search(r'ustacast|konuk|r[öo]portaj|sohbet|podcast', title_lower):
        return "konuk_gorusmesi"

    # Soru-cevap (soru işareti + soru kelimeleri)
    if re.search(r'kaç|nasıl|nerede|ne zaman|kim|hangi', title_lower):
        if '?' in title or 'soruya' in title_lower or 'sorusuna' in title_lower:
            return "soru_cevap"

    # Taktik/Rehber
    if re.search(r'nasıl\s+çalışılır|nasıl\s+çalışmal|nasıl\s+bitsin|nasıl\s+gelir|rehber|taktik|strateji|metod', title_lower):
        return "taktik_rehber"

    # Motivasyon/Zihniyet
    if re.search(r'motivasyon|disiplin|stres|zihniyet|güzel|başarm|i̇stiyorsun|istiyorum|korku|endişe|kayg|panik', title_lower):
        return "motivasyon"

    # Deneme/Analiz
    if re.search(r'deneme|analiz|sıra|sınav|net\s+art|puan', title_lower):
        return "deneme"

    # Program/Plan
    if re.search(r'günde|program|plan|gün\s+bitir|hafta\s+bitir|ay\s+bitir|takvim|yol\s+haritas', title_lower):
        return "program"

    # Kaynak önerisi
    if re.search(r'en\s+i̇yi|en\s+iyisi|öneri|tavsiye|kaynak|soru\s+bankas|hangis', title_lower):
        return "kaynak_onerisi"

    # Seviye özel
    if re.search(r"'?le?\s+özel|11'?|12'?|mezun|ea|sayısal|sözel|eşit\s+ağırlık|mf", title_lower):
        return "seviye_ozel"

    # Ders özel
    if re.search(r'türkçe|matematik|fizik|kimya|biyoloji|tarih|coğrafya|felsefe|edebiyat|dil\s+bilgisi|geom', title_lower):
        return "ders_ozel"

    return "genel"


def analyze_source(source: Dict[str, Any]) -> Dict[str, Any]:
    """Tek kaynak analizi"""
    title = source.get('title', '')
    content = source.get('content', '')
    char_count = source.get('char_count', 0)

    # Çok kısa içerikleri atla
    if not content or char_count < 50:
        return None

    full_text = title + " " + content

    return {
        "title": title,
        "char_count": char_count,
        "category": categorize_content(title, content),
        "opening_formulas": extract_opening_formulas(content),
        "closing_formulas": extract_closing_formulas(content),
        "transitions": extract_transitions(content),
        "address_terms": extract_address_terms(content),
        "emojis": extract_emojis(full_text),
        "patterns": {
            "aciklama": extract_explanation_patterns(content),
            "vurgu": extract_emphasis_patterns(content),
            "samimiyet": extract_casual_patterns(content),
        }
    }


# =============================================================================
# MAIN
# =============================================================================

def main():
    if len(sys.argv) < 3:
        print("Kullanım: python3 extract_style.py <input_json> <output_name>")
        print("Örnek: python3 extract_style.py data/oguz_usta_yatay.json oguz_usta_yatay")
        sys.exit(1)

    input_file = Path(sys.argv[1])
    output_name = sys.argv[2]

    with open(input_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    sources = data.get('sources', [])
    print(f"\n{'='*60}")
    print(f"📊 Style Extraction: {len(sources)} kaynak analiz ediliyor...")
    print(f"{'='*60}\n")

    # Tüm kaynakları analiz et
    analyses = []
    for i, source in enumerate(sources, 1):
        result = analyze_source(source)
        if result:
            analyses.append(result)
        if i % 20 == 0:
            print(f"  İşlenen: {i}/{len(sources)}")

    # Profile oluştur
    profile = {
        "meta": {
            "source": input_file.stem,
            "sample_size": len(analyses),
            "total_chars": sum(a['char_count'] for a in analyses),
            "extracted_at": datetime.now().isoformat(),
        },
        "patterns": {
            "opening_formulas": Counter(),
            "closing_formulas": Counter(),
            "transitions": Counter(),
            "address_terms": Counter(),
            "aciklama": Counter(),
            "vurgu": Counter(),
            "samimiyet": Counter(),
        },
        "emojis": Counter(),
        "categories": Counter(),
    }

    # Toplulaştır
    for a in analyses:
        # Kategori
        profile["categories"][a['category']] += 1

        # Giriş formülleri
        for f in a['opening_formulas']:
            if len(f) > 5:
                profile["patterns"]["opening_formulas"][f] += 1

        # Kapanış formülleri
        for f in a['closing_formulas']:
            if len(f) > 3:
                profile["patterns"]["closing_formulas"][f] += 1

        # Geçişler
        for t in a['transitions']:
            profile["patterns"]["transitions"][t] += 1

        # Hitap kelimeleri
        for t in a['address_terms']:
            profile["patterns"]["address_terms"][t] += 1

        # Kalıplar
        for p in a['patterns']['aciklama']:
            profile["patterns"]["aciklama"][p] += 1
        for p in a['patterns']['vurgu']:
            profile["patterns"]["vurgu"][p] += 1
        for p in a['patterns']['samimiyet']:
            profile["patterns"]["samimiyet"][p] += 1

        # Emojiler
        for e in a['emojis']:
            profile["emojis"][e] += 1

    # Counters'ı listeye çevir (top 20)
    for key in profile["patterns"]:
        if isinstance(profile["patterns"][key], Counter):
            profile["patterns"][key] = [
                {"text": text, "count": count}
                for text, count in profile["patterns"][key].most_common(20)
            ]

    profile["emojis"] = dict(profile["emojis"].most_common(15))
    profile["categories"] = dict(profile["categories"].most_common())

    # Sayı formatları (separate pass - tüm content birleştir)
    all_content = " ".join([s.get('content', '') for s in sources])
    number_formats = extract_number_formats(all_content)
    profile["number_formats"] = [
        {"text": text, "count": count}
        for text, count in number_formats
    ]

    # Kaydet
    output_path = Path("data/style_profiles") / f"{output_name}_profile.json"
    output_path.parent.mkdir(exist_ok=True)

    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(profile, f, ensure_ascii=False, indent=2)

    # Özet yazdır
    print(f"\n{'='*60}")
    print(f"✅ Style profile kaydedildi: {output_path}")
    print(f"{'='*60}")
    print(f"📊 Sample size: {profile['meta']['sample_size']}")
    print(f"📁 Kategoriler:")
    for cat, count in list(profile['categories'].items())[:8]:
        print(f"   - {cat}: {count}")
    print(f"\n🔤 Giriş Formülleri (Top 5):")
    for item in profile['patterns']['opening_formulas'][:5]:
        print(f"   - \"{item['text']}\" ({item['count']})")
    print(f"\n👋 Kapanış Formülleri (Top 5):")
    for item in profile['patterns']['closing_formulas'][:5]:
        print(f"   - \"{item['text']}\" ({item['count']})")
    print(f"\n💬 Hitap Kelimeleri:")
    for item in profile['patterns']['address_terms']:
        print(f"   - {item['text']} ({item['count']})")
    print(f"\n🔄 Geçiş Kelimeleri:")
    transitions = [t['text'] for t in profile['patterns']['transitions']]
    print(f"   - {', '.join(transitions[:10])}")
    print(f"\n📝 Kalıplar:")
    print(f"   - Açıklama: {[p['text'] for p in profile['patterns']['aciklama']]}")
    print(f"   - Vurgu: {[p['text'] for p in profile['patterns']['vurgu']]}")
    print(f"   - Samimiyet: {[p['text'] for p in profile['patterns']['samimiyet']]}")
    print(f"\n😊 Emojiler: {' '.join(profile['emojis'].keys())}")
    print()


if __name__ == "__main__":
    main()
