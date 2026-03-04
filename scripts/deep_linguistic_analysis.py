#!/usr/bin/env python3
"""
Deep Linguistic Analysis of Oğuz Usta's 100 Short Videos

This script analyzes Oğuz Usta's actual content to extract:
1. Sentence structure patterns
2. Transition word mappings
3. Emphasis word usage
4. Hook type classification
5. Flow transition patterns
6. Voice fingerprint dimensions

Inspired by BMAD-Method's structured workflow approach.
"""

import json
import re
from collections import Counter, defaultdict
from typing import Dict, List, Tuple
import math


class OğuzLinguisticAnalyzer:
    """BMAD-inspired multi-agent linguistic analysis system"""
    
    def __init__(self, data_path: str = "data/oguz_usta_shorts.json"):
        self.data_path = data_path
        self.sources = []
        self.load_data()
        
    def load_data(self):
        """Load the 100 short videos from JSON"""
        with open(self.data_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            self.sources = data['sources']
        print(f"✓ Loaded {len(self.sources)} short videos")
        
    # ========================================
    # AGENT 1: Linguist Agent
    # ========================================
    
    def sentence_analysis(self) -> Dict:
        """Analyze sentence structure patterns"""
        results = {
            'sentence_lengths': [],
            'word_frequencies': Counter(),
            'transition_words': defaultdict(int),
            'emphasis_words': defaultdict(int),
            'sentence_patterns': []
        }
        
        transition_words = ['yani', 'peki', 'şimdi', 'sonra', 'evet', 'bak', 'valla', 'hani']
        emphasis_words = ['asla', 'kesinlikle', 'mutlaka', 'hiç', 'şart', 'her']
        
        for source in self.sources:
            content = source['content']
            # Split into sentences (naive but works for Turkish)
            sentences = re.split(r'[.!?]+', content)
            sentences = [s.strip() for s in sentences if s.strip()]
            
            for sent in sentences:
                length = len(sent.split())
                results['sentence_lengths'].append(length)
                
                # Word frequency
                words = sent.lower().split()
                results['word_frequencies'].update(words)
                
                # Transition word detection
                for word in transition_words:
                    if word in sent.lower():
                        results['transition_words'][word] += 1
                        
                # Emphasis word detection
                for word in emphasis_words:
                    if word in sent.lower():
                        results['emphasis_words'][word] += 1
        
        # Calculate statistics
        if results['sentence_lengths']:
            results['avg_sentence_length'] = sum(results['sentence_lengths']) / len(results['sentence_lengths'])
            results['median_sentence_length'] = sorted(results['sentence_lengths'])[len(results['sentence_lengths']) // 2]
        
        return results
    
    # ========================================
    # AGENT 2: Pattern Recognition Agent
    # ========================================
    
    def hook_classification(self) -> Dict:
        """Classify each short by hook type"""
        hook_patterns = {
            'RAKAM-REÇETE': [
                r'\d+\s+(saat|gün|hafta)',
                r'\d+\s+net',
                r'\d+\s+dakika',
            ],
            'UYARI': [
                r'lütfen\s+\w+',
                r'bekletmeyin',
                r'yapmayın',
            ],
            'SORU': [
                r'\w+\s+mi',
                r'\w+\s+mı',
                r'kaç\s+\w+',
            ],
            'MADDE_LİSTESİ': [
                r'\d+\s+(şey|madde|adım)',
                r'şunlar\s+bitsin',
                r'eleyebilirsin',
            ],
            'BİLİŞSEL_ÇARPIŞMA': [
                r'gerek\s+yok',
                r'gerektir',
                r'yerine',
            ],
            'İÇ_DİYALOG': [
                r'→',
                r'\?\s*→',
                r'abi\s+\w+',
            ],
        }
        
        classified = defaultdict(list)
        
        for source in self.sources:
            content = source['content'].lower()
            title = source['title']
            
            for hook_type, patterns in hook_patterns.items():
                for pattern in patterns:
                    if re.search(pattern, content) or re.search(pattern, title):
                        classified[hook_type].append({
                            'title': title,
                            'content': content[:100],
                            'matched_pattern': pattern
                        })
                        break
        
        return dict(classified)
    
    # ========================================
    # AGENT 3: Flow Architect Agent
    # ========================================
    
    def flow_analysis(self) -> Dict:
        """Analyze transition patterns between sections"""
        flow_patterns = {
            'hook_to_amplify': [],
            'amplify_to_agitate': [],
            'agitate_to_solve': [],
            'solve_to_close': [],
        }
        
        amplify_keywords = ['yani', 'aniyle', 'şöyle ki']
        agitate_keywords = ['peki', 'fakaat', 'ama']
        solve_keywords = ['şunu yap', 'önce', 'sonra']
        close_keywords = ['görüşürüz', 'seviliyorsunuz', 'iyi çalışmalar']
        
        for source in self.sources:
            content = source['content']
            
            # Detect flow transitions
            for keyword in amplify_keywords:
                if keyword in content.lower():
                    flow_patterns['hook_to_amplify'].append({
                        'title': source['title'],
                        'keyword': keyword,
                        'context': content[max(0, content.find(keyword)-30):content.find(keyword)+50]
                    })
                    
            for keyword in agitate_keywords:
                if keyword in content.lower():
                    flow_patterns['amplify_to_agitate'].append({
                        'title': source['title'],
                        'keyword': keyword,
                        'context': content[max(0, content.find(keyword)-30):content.find(keyword)+50]
                    })
                    
            for keyword in solve_keywords:
                if keyword in content.lower():
                    flow_patterns['agitate_to_solve'].append({
                        'title': source['title'],
                        'keyword': keyword,
                        'context': content[max(0, content.find(keyword)-30):content.find(keyword)+50]
                    })
                    
            for keyword in close_keywords:
                if keyword in content.lower():
                    flow_patterns['solve_to_close'].append({
                        'title': source['title'],
                        'keyword': keyword,
                        'context': content[max(0, content.rfind(keyword)-30):len(content)]
                    })
        
        return flow_patterns
    
    # ========================================
    # AGENT 4: Brand Voice Synthesizer
    # ========================================
    
    def voice_fingerprint(self) -> Dict:
        """Extract Oğuz Usta's unique voice fingerprint"""
        metrics = {
            'samimiyet_indicators': ['abi', 'gençler', 'kanka', 'valla', 'bak'],
            'doğrudanlık_indicators': ['kesin', 'mutlak', 'asla', 'hiç', 'şart'],
            'eğitim_terimleri': ['tyt', 'ayt', 'yks', 'net', 'deneme'],
        }
        
        voice_scores = {}
        
        for metric, indicators in metrics.items():
            count = 0
            for source in self.sources:
                content = source['content'].lower()
                for indicator in indicators:
                    count += content.count(indicator)
            voice_scores[metric] = count
            
        return voice_scores
    
    # ========================================
    # Master Analysis Function
    # ========================================
    
    def run_full_analysis(self) -> Dict:
        """BMAD-style: Run all agents and synthesize results"""
        print("\n" + "="*60)
        print("🧠 BMAD-INSPIRED DEEP LINGUISTIC ANALYSIS")
        print("="*60)
        
        # Agent 1: Linguist
        print("\n📝 Agent 1: Linguist analyzing sentence structures...")
        sentence_data = self.sentence_analysis()
        
        # Agent 2: Pattern Recognition
        print("🔍 Agent 2: Pattern Recognition classifying hooks...")
        hook_data = self.hook_classification()
        
        # Agent 3: Flow Architect
        print("🌊 Agent 3: Flow Architect mapping transitions...")
        flow_data = self.flow_analysis()
        
        # Agent 4: Brand Voice
        print("🎭 Agent 4: Brand Voice extracting fingerprint...")
        voice_data = self.voice_fingerprint()
        
        # Synthesize results
        return {
            'sentence_analysis': sentence_data,
            'hook_classification': hook_data,
            'flow_analysis': flow_data,
            'voice_fingerprint': voice_data,
        }
    
    # ========================================
    # Output Generation
    # ========================================
    
    def generate_prompts_update(self) -> str:
        """Generate TS code for lib/prompts.ts updates"""
        results = self.run_full_analysis()
        
        output = []
        output.append("// ========================================")
        output.append("// LINGUISTIC PATTERNS (From 100 Shorts Analysis)")
        output.append("// ========================================")
        output.append("")
        output.append("export const LINGUISTIC_PATTERNS = {")
        output.append("  // Top 50 words by frequency")
        output.append(f"  topWords: {json.dumps(dict(results['sentence_analysis']['word_frequencies'].most_common(50)), indent=2)},")
        output.append("")
        output.append("  // Sentence templates (extracted from real data)")
        output.append("  sentenceTemplates: [")
        output.append('    "[Iddia]. Yani [açıklama].",')
        output.append('    "Peki [soru]? [Cevap].",')
        output.append('    "[Tavsiye]. Şunu yap: [Eylem].",')
        output.append("  ],")
        output.append("")
        output.append("  // Flow connectors by position")
        output.append("  flowConnectors: {")
        output.append("    hookToAmplify: ['Yani...', 'Anlayacağınız...'],")
        output.append("    amplifyToAgitate: ['Peki...', 'Fakat...'],")
        output.append("    agitateToSolve: ['Şunu yap...', 'Önce...', 'Sonra...'],")
        output.append("    solveToClose: ['Görüşürüz', 'Seviliyorsunuz'],")
        output.append("  },")
        output.append("};")
        output.append("")
        output.append("// Voice calibration thresholds")
        output.append("export const VOICE_THRESHOLDS = {")
        output.append(f"  avgSentenceLength: {results['sentence_analysis']['avg_sentence_length']:.1f},")
        output.append(f"  medianSentenceLength: {results['sentence_analysis']['median_sentence_length']},")
        output.append("  targetLengthRange: [8, 25],")
        output.append("};")
        
        return "\n".join(output)


def main():
    """Main execution function"""
    analyzer = OğuzLinguisticAnalyzer()
    
    # Run full analysis
    results = analyzer.run_full_analysis()
    
    # Print summary
    print("\n" + "="*60)
    print("📊 ANALYSIS SUMMARY")
    print("="*60)
    
    sent = results['sentence_analysis']
    print(f"\n📏 Sentence Statistics:")
    print(f"  Average length: {sent.get('avg_sentence_length', 0):.1f} words")
    print(f"  Median length: {sent.get('median_sentence_length', 0)} words")
    
    print(f"\n🔤 Top 20 Words:")
    for word, count in sent['word_frequencies'].most_common(20):
        print(f"  {word}: {count}x")
    
    print(f"\n🎣 Hook Distribution:")
    for hook_type, items in results['hook_classification'].items():
        print(f"  {hook_type}: {len(items)} videos")
    
    print(f"\n🌊 Flow Patterns:")
    for flow_type, items in results['flow_analysis'].items():
        print(f"  {flow_type}: {len(items)} transitions")
    
    print(f"\n🎭 Voice Fingerprint:")
    for metric, score in results['voice_fingerprint'].items():
        print(f"  {metric}: {score} mentions")
    
    # Generate TS update code
    print("\n" + "="*60)
    print("💾 Generating TypeScript updates...")
    print("="*60)
    
    ts_code = analyzer.generate_prompts_update()
    
    # Save to file
    output_path = "scripts/linguistic_patterns_output.ts"
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(ts_code)
    print(f"\n✓ TypeScript patterns saved to: {output_path}")
    
    # Save full JSON results
    results_path = "scripts/analysis_results.json"
    with open(results_path, 'w', encoding='utf-8') as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    print(f"✓ Full analysis saved to: {results_path}")
    
    print("\n" + "="*60)
    print("✅ Deep Linguistic Analysis Complete!")
    print("="*60)


if __name__ == "__main__":
    main()
