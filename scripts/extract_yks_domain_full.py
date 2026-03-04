#!/usr/bin/env python3
"""
YKS Domain Knowledge Extraction from Multiple Sources

Extract YKS-specific terminology from:
1. Oğuz Usta (oguz_usta_yatay.json) - 123 videos
2. Baykus Mentörlük (baykus-complete.json) - 50 videos  
3. Competitors (competitor-transcripts.json) - 60 videos

Total: ~700K words of YKS content
"""

import json
from collections import Counter
from typing import Dict, List


class MultiSourceYKSExtractor:
    """Extract YKS domain knowledge from multiple sources"""
    
    def __init__(self):
        self.all_transcripts = []
        
    def load_sources(self):
        """Load all YKS transcript sources"""
        
        # 1. Oğuz Usta (already in data/)
        print("Loading Oğuz Usta transcripts...")
        with open('data/oguz_usta_yatay.json') as f:
            oguz = json.load(f)
            for source in oguz['sources']:
                self.all_transcripts.append({
                    'channel': 'Oğuz Usta',
                    'title': source.get('title', ''),
                    'content': source.get('content', ''),
                    'kind': source.get('kind', '')
                })
        print(f"  ✓ {len(oguz['sources'])} videos")
        
        # 2. Baykus Mentörlük
        print("\nLoading Baykus Mentörlük transcripts...")
        with open('data/baykus-complete.json') as f:
            baykus = json.load(f)
            for video in baykus.get('videos', []):
                self.all_transcripts.append({
                    'channel': 'Baykus Mentörlük',
                    'title': video.get('title', ''),
                    'content': video.get('transcript', ''),
                    'kind': 'baykus'
                })
        print(f"  ✓ {len(baykus.get('videos', []))} videos")
        
        # 3. Competitors
        print("\nLoading competitor transcripts...")
        with open('data/competitor-transcripts.json') as f:
            comp = json.load(f)
            
            # Get all videos
            all_videos = comp.get('allVideos', [])
            for video in all_videos:
                self.all_transcripts.append({
                    'channel': video.get('channelName', 'Competitor'),
                    'title': video.get('title', ''),
                    'content': video.get('transcript', ''),
                    'kind': 'competitor'
                })
        print(f"  ✓ {len(all_videos)} videos")
        
        print(f"\n📊 TOTAL: {len(self.all_transcripts)} transcripts loaded")
        
    def extract_yks_terminology(self) -> Dict[str, int]:
        """Extract YKS-specific terminology with frequency"""
        
        # YKS-specific terms
        yks_terms = [
            # Sınav terimleri
            "tyt", "ayt", "yks", "net", "sıralama", "başarı sırası", "obp",
            "mezun", "hazırlık", "deneme", "konu", "tarama", "çalışma",
            
            # Branşlar
            "matematik", "türkçe", "edebiyat", "tarih", "coğrafya", "felsefe",
            "fizik", "kimya", "biyoloji", "paragraf", "dil bilgisi",
            
            # Kaynaklar (erken ortaya çıkanlar)
            "bilgi sarmal", "ck haritalar", "baykuş", "deneme", "fasikül",
            "barış hoca", "özcan hoca", "altı hoca", "emektaş", "emek hoca",
            "soner hoca", "paraf", "kolay net", "345", "apotemi",
            
            # Stratejiler
            "deneme analizi", "soru çözümü", "konu bitirme", "tarama",
            "çalışma planı", "net arttırma", "puan hesaplama",
            
            # Teknikler
            "active recall", "pomodoro", "kalıc", "süreklilik", "rutin",
            
            # Öğrenci türleri
            "erken başlayan", "geç başlayan", "hazırlıksız", "sıfırdan",
        ]
        
        counts = Counter()
        
        for transcript in self.all_transcripts:
            content = transcript['content'].lower()
            for term in yks_terms:
                if term in content:
                    counts[term] += content.count(term)
        
        return dict(counts.most_common(100))
    
    def extract_hoca_names(self) -> Dict[str, int]:
        """Extract hoca names and their frequency"""
        
        # Hoca name patterns
        hoca_patterns = [
            "barış hoca", "barış hocaa", "barış",
            "özcan hoca", "özcan",
            "altı hoca", "altı",
            "emek hoca", "emektaş", "emektaş hoca",
            "soner hoca", "soner",
            "emre hoca", "emre",
            "eyip hoca", "eyip",
            "rüştü hoca", "rüştü",
        ]
        
        counts = Counter()
        
        for transcript in self.all_transcripts:
            content = transcript['content'].lower()
            for pattern in hoca_patterns:
                if pattern in content:
                    counts[pattern] += content.count(pattern)
        
        return dict(counts.most_common(30))
    
    def extract_resource_names(self) -> Dict[str, int]:
        """Extract resource/book names"""
        
        resources = [
            "bilgi sarmal", "ck haritalar", "ck coğrafya", "ck 9 günde",
            "baykuş deneme", "baykuş", "345", "paraf", "apotemi",
            "kolay net", "benim dershanem", "3d", "acil", "mikro",
            "barış matematik", "yayınları",
        ]
        
        counts = Counter()
        
        for transcript in self.all_transcripts:
            content = transcript['content'].lower()
            for resource in resources:
                if resource in content:
                    counts[resource] += content.count(resource)
        
        return dict(counts.most_common(30))
    
    def extract_phrases(self) -> List[str]:
        """Extract common YKS phrases"""
        
        phrases = []
        seen = set()
        
        # Look for recommendation patterns
        for transcript in self.all_transcripts:
            content = transcript['content'].lower()
            
            # Resource recommendations
            if "öneriyorum" in content:
                phrases.append(f"{transcript['channel']}: öneriyorum pattern")
            if "kaynak" in content:
                phrases.append(f"{transcript['channel']}: kaynak mention")
            if "deneme" in content:
                phrases.append(f"{transcript['channel']}: deneme mention")
        
        return phrases[:20]
    
    def run_extraction(self) -> Dict:
        """Run full extraction and return results"""
        
        print("\n" + "="*60)
        print("YKS DOMAIN KNOWLEDGE EXTRACTION")
        print("="*60)
        
        self.load_sources()
        
        print("\nExtracting terminology...")
        terminology = self.extract_yks_terminology()
        
        print("Extracting hoca names...")
        hoca_names = self.extract_hoca_names()
        
        print("Extracting resource names...")
        resources = self.extract_resource_names()
        
        results = {
            'total_transcripts': len(self.all_transcripts),
            'total_videos': len(self.all_transcripts),  # Same
            'yks_terminology': terminology,
            'hoca_names': hoca_names,
            'resources': resources,
            'channels': list(set(t['channel'] for t in self.all_transcripts)),
        }
        
        # Save results
        output_path = 'data/yks_domain_knowledge_full.json'
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(results, f, ensure_ascii=False, indent=2)
        
        print(f"\n✅ Results saved to: {output_path}")
        
        # Print summary
        print("\n📊 SUMMARY")
        print(f"Channels: {', '.join(results['channels'])}")
        print(f"\nTop 10 YKS Terms:")
        for term, count in list(results['yks_terminology'].items())[:10]:
            print(f"  {term}: {count}x")
        
        return results


def main():
    extractor = MultiSourceYKSExtractor()
    results = extractor.run_extraction()


if __name__ == "__main__":
    main()
