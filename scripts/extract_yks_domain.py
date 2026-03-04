#!/usr/bin/env python3
"""
YKS Domain Knowledge Extraction from Oğuz Usta Transcripts

Extract YKS-specific terminology, resources, techniques, and concepts
from the 123 yatay video transcripts to create a domain knowledge base.
"""

import json
import re
from collections import Counter, defaultdict
from typing import Dict, List, Set

class YKSDomainExtractor:
    """Extract YKS domain knowledge from Oğuz Usta transcripts"""
    
    def __init__(self, data_path: str = "data/oguz_usta_yatay.json"):
        with open(data_path, 'r', encoding='utf-8') as f:
            self.data = json.load(f)
        self.sources = self.data['sources']
        
    def extract_resource_names(self) -> Dict[str, int]:
        """Extract resource/hoca names and their frequency"""
        resources = [
            # Kitaplar
            "bilgi sarmal", "ck haritalar", "baykuş deneme", "paraf", 
            "kolay net", "1 deneme", "benim dershanem", "3d sarmal",
            "yayınları", "eski sorular", "barış matematik",
            "ağırlıklı soru bankası", "çözüm odaklı sorular",
            
            # Hocalar
            "barış hocaa", "özcan hoca", "altı hoca", "emektaş hoca",
            "soner hoca", "emre hoca", "emektaş", "bilgi sarmal",
            "eyip hocaa", "paraf eğitimi", "kuaför hoca", "cılcı hoca",
            
            # Platformlar
            "pofu", "kuaf", "tus", "baykuş", "bilgi sarmal",
            
            # Diğer
            "deneme", "kitap", "fasikül", "konu anlatımı",
        ]
        
        counts = Counter()
        for source in self.sources:
            content = source['content'].lower()
            for resource in resources:
                if resource in content:
                    counts[resource] += content.count(resource)
        
        return dict(counts.most_common(50))
    
    def extract_yks_terms(self) -> Dict[str, int]:
        """Extract YKS-specific terminology"""
        terms = [
            # Sınav terimleri
            "tyt", "ayt", "yks", "net", "puan", "sıralama", "başarı sırası",
            "mezun", "hazırlık", "deneme", "konu", "tarama", "çalışma",
            
            # Branşlar
            "matematik", "türk��e", "edebiyat", "tarih", "coğrafya", "felsefe",
            "fizik", "kimya", "biyoloji", "paragraf", "dil bilgisi",
            
            # Stratejiler
            "deneme analizi", "soru çözümü", "konu bitirme", "tarama",
            "çalışma planı", "çalışma programı", "net arttırma", "puan hesaplama",
            
            # Teknikler
            "active recall", "spaced repetition", "pomodoro", "kalıc",
            "süreklilik", "rutin", "disiplin", "motivasyon", "odaklanma",
            
            # Öğrenci türleri
            "erken başlayan", "geç başlayan", "hazırlıksız", "sıfırdan başlayan",
        ]
        
        counts = Counter()
        for source in self.sources:
            content = source['content'].lower()
            for term in terms:
                counts[term] += content.count(term)
        
        return dict(counts.most_common(50))
    
    def extract_phrases(self) -> List[str]:
        """Extract common YKS phrases and patterns"""
        phrases = []
        
        # Look for specific patterns
        for source in self.sources:
            content = source['content']
            
            # Find resource recommendations
            for match in re.finditer(r'([a-zA-ZğüşıöçĞÜŞİÖÇ]+[ ]+hocaa?| [a-zA-ZğüşıöçĞÜŞİÖÇ]+[ ]+öneriyorum|Bilgi Sarmal|CK Haritalar|Baykuş Deneme|Paraf)', content):
                phrase = match.group(1) if match.groups() else match.group(0)
                if phrase not in phrases:
                    phrases.append(phrase)
        
        return phrases[:50]
    
    def extract_techniques(self) -> List[str]:
        """Extract specific YKS study techniques mentioned"""
        techniques = []
        
        technique_keywords = [
            "çalışma", "çözüm", "analiz", "plan", "program", "strateji",
            "teknik", "yöntem", "taktik", "öneri", "tavsiye", "rehber",
        ]
        
        for source in self.sources:
            content = source['content'].lower()
            
            # Look for technique descriptions
            sentences = re.split(r'[.!?]+', content)
            for sent in sentences:
                if any(kw in sent for kw in technique_keywords):
                    if len(sent.split()) > 10:  # Only longer, meaningful phrases
                        techniques.append(sent.strip())
        
        return techniques[:100]
    
    def run_extraction(self) -> Dict:
        """Run all extractions and return comprehensive results"""
        print("Extracting YKS Domain Knowledge from 123 videos...")
        
        results = {
            'resource_names': self.extract_resource_names(),
            'yks_terms': self.extract_yks_terms(),
            'phrases': self.extract_phrases(),
            'techniques': self.extract_techniques(),
            'total_videos': len(self.sources),
        }
        
        return results


def main():
    extractor = YKSDomainExtractor()
    results = extractor.run_extraction()
    
    print(f"\n📊 EXTRACTION RESULTS")
    print(f"Videos analyzed: {results['total_videos']}")
    print(f"\n🏢 Top Resource Names:")
    for resource, count in list(results['resource_names'].items())[:15]:
        print(f"  {resource}: {count}x")
    
    print(f"\n📚 Top YKS Terms:")
    for term, count in list(results['yks_terms'].items())[:15]:
        print(f"  {term}: {count}x")
    
    print(f"\n💬 Sample Phrases:")
    for phrase in results['phrases'][:10]:
        print(f"  {phrase}")
    
    # Save to JSON
    with open('data/yks_domain_knowledge.json', 'w', encoding='utf-8') as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    
    print(f"\n✅ Saved to: data/yks_domain_knowledge.json")


if __name__ == "__main__":
    main()
