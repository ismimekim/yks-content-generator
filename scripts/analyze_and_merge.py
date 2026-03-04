#!/usr/bin/env python3
"""
Oğuz Usta Veri Analizi ve Birleştirme
SHORTS ve YATAY videoları analiz edip birleştirir
"""
import json
from pathlib import Path
from collections import Counter
import re


def clean_text(text: str, max_chars: int = 500) -> str:
    """Metni temizle ve kısalt"""
    text = re.sub(r'\s+', ' ', text)
    return text[:max_chars].strip()


def analyze_file(filepath: Path):
    """JSON dosyasını analiz et"""
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    sources = data.get('sources', [])
    
    total_chars = sum(s.get('char_count', 0) for s in sources)
    
    # Başlık analizi
    titles = [s['title'] for s in sources]
    title_words = []
    for title in titles:
        words = re.findall(r'\b[A-ZÇĞÖŞÜİ]{3,}\b', title, re.IGNORECASE)
        title_words.extend([w.upper() for w in words])
    
    # İçerik parçaları oluştur (prompt için)
    content_samples = []
    for s in sources[:50]:  # İlk 50 kaynak
        content_samples.append({
            'title': s['title'],
            'content': clean_text(s.get('content', ''))
        })
    
    return {
        'name': filepath.stem,
        'count': len(sources),
        'total_chars': total_chars,
        'title_words': Counter(title_words),
        'content_samples': content_samples
    }


def merge_for_prompt(shorts_data: dict, yatay_data: dict) -> dict:
    """Prompt için birleştirilmiş veri oluştur"""
    
    merged = {
        'stats': {
            'shorts_count': shorts_data['count'],
            'yatay_count': yatay_data['count'],
            'total_sources': shorts_data['count'] + yatay_data['count'],
            'total_chars': shorts_data['total_chars'] + yatay_data['total_chars']
        },
        'style_patterns': {
            'common_words': [],
            'topics': [],
            'phrases': []
        },
        'content_examples': {
            'shorts': shorts_data['content_samples'][:30],
            'yatay': yatay_data['content_samples'][:30]
        }
    }
    
    # Ortak kelimeler
    short_words = set(shorts_data['title_words'])
    yatay_words = set(yatay_data['title_words'])
    common = short_words & yatay_words
    merged['style_patterns']['common_words'] = sorted(
        common, 
        key=lambda w: shorts_data['title_words'][w] + yatay_data['title_words'][w],
        reverse=True
    )[:50]
    
    return merged


def main():
    data_dir = Path("data")
    
    # Dosyaları oku
    shorts_file = data_dir / "oguz_usta_shorts.json"
    yatay_file = data_dir / "oguz_usta_yatay.json"
    
    print("=" * 60)
    print("OĞUZ USTA VERİ ANALİZİ")
    print("=" * 60)
    
    # SHORTS analizi
    print("\n📱 SHORTS analiz ediliyor...")
    shorts = analyze_file(shorts_file)
    print(f"   Kaynak: {shorts['count']}")
    print(f"   Karakter: {shorts['total_chars']:,}")
    print(f"   En yaygın kelimeler: {shorts['title_words'].most_common(10)}")
    
    # YATAY analizi
    print("\n📺 YATAY analiz ediliyor...")
    yatay = analyze_file(yatay_file)
    print(f"   Kaynak: {yatay['count']}")
    print(f"   Karakter: {yatay['total_chars']:,}")
    print(f"   En yaygın kelimeler: {yatay['title_words'].most_common(10)}")
    
    # Birleştir
    print("\n🔗 Veriler birleştiriliyor...")
    merged = merge_for_prompt(shorts, yatay)
    
    # Kaydet
    output = data_dir / "oguz_usta_merged.json"
    with open(output, 'w', encoding='utf-8') as f:
        json.dump(merged, f, ensure_ascii=False, indent=2)
    
    print(f"\n{'='*60}")
    print("✅ ÖZET")
    print(f"{'='*60}")
    print(f"📊 TOPLAM KAYNAK: {merged['stats']['total_sources']}")
    print(f"   - SHORTS: {merged['stats']['shorts_count']}")
    print(f"   - YATAY: {merged['stats']['yatay_count']}")
    print(f"📏 TOPLAM KARAKTER: {merged['stats']['total_chars']:,}")
    print(f"🎯 ORTAK KELİMELER: {len(merged['style_patterns']['common_words'])}")
    print(f"   {', '.join(merged['style_patterns']['common_words'][:20])}")
    print(f"\n💾 Kaydedildi: {output}")


if __name__ == "__main__":
    main()
