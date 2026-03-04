# Deep Analysis + BMAD-Inspired Workflow

## Hedef
Oğuz Usta'nın 100 gerçek short videosunu derinlemesine analiz edip, dil ve anlatım tarzını tam olarak yakalamak. BMAD-Method'un yapılandırılmış yaklaşımını adapte ederek süreç oluşturmak.

---

## BMAD-Method'dan Alacağımız Prensipler

**BMAD'ın Core Değerleri (Adapte Edilebilir):**
1. **Scale-Adaptive Intelligence** → İçerik uzunluğuna göre derinlik ayarı (SHORT vs YATAY)
2. **Structured Workflows** → Analiz → Plan → Execute → Refine döngüsü
3. **Specialized Agents** → Farklı roller: Linguist, Copywriter, YKS Expert, Brand Voice Analyst
4. **Party Mode** → Çoklu perspektiften içerik değerlendirme
5. **Iterative Refinement** → Test → Feedback → Improve

---

## 🎯 Workflow: Oğuz Usta Deep Linguistic Analysis

### Phase 1: DATA MINING (Veri Madenciliği)
**Hedef:** 100 short'u linguistik pattern'ler için analiz et

**Agent Roles:**
- **Linguist Agent** → Cümle yapıları, bağlaçlar, vurgu kelimeleri
- **Emotion Analyst** → Tonalite, enerji seviyeleri, empati anları
- **Flow Architect** → Hook → Body → Close geçiş kalıpları

**Deliverables:**
```
1. Cümle Uzunluk Dağılımı (karakter bazında)
2. En Sık 100 Kelime (frekans sırası)
3. Bağlaç/Geçiş Kelime Haritası ("yani", "peki", "şimdi")
4. Vurgu Kelime Envanteri ("asla", "kesinlikle", "mutlaka")
5. Hook Pattern Matrix (6 tip × gerçek örnekler)
6. Close Pattern Library ("görüşürüz" varyasyonları)
```

**Script:**
```python
# scripts/deep_linguistic_analysis.py
- Sentence tokenization
- Word frequency analysis  
- Transition word mapping
- Emphasis word extraction
- Hook type classification
- Emotional tonality scoring
```

---

### Phase 2: PATTERN SYNTHESIS (Pattern Sentezi)
**Hedef:** Analiz sonuçlarını actionable pattern'lere dönüştür

**Agent Roles:**
- **Pattern Recognition Agent** → Recurring structures
- **Brand Voice Synthesizer** → Tonality dimensions
- **Copywriting Framework Mapper** → PAS, SUCCESs uygulamaları

**Deliverables:**
```
1. Oğuz Usta Sentence Templates (20 adet)
   Örn: "[Iddia]. Yani [açıklama]. Çünkü [neden]."
   
2. Flow Transition Map
   Hook → Amplify: "Yani..." ile başla
   Amplify → Agitate: "Peki... " veya direkt geçiş
   Agitate → Solve: "Yani şunu yap..."
   
3. Emotional Arc Patterns
   Başlangıç: Şaşırtıcı/Merak
   Orta: Empati/Anlaşılma
   Son: Eyleme geçirme/Motivasyon
   
4. Voice Fingerprint
   - Samimilik skoru: 9/10
   - Doğrudanlık: 9/10
   - Enerji seviyesi: 8/10
   - Empati derinliği: 7/10
```

---

### Phase 3: PROMPT ENGINEERING (Prompt İyileştirme)
**Hedef:** Bulguları lib/prompts.ts'e entegre et

**Agent Roles:**
- **Prompt Architect** → System prompt tasarımı
- **Example Curator** → Gerçek örneklerden en iyilerini seç
- **Quality Assurance** → Test senaryoları oluştur

**Deliverables:**
```
1. OGUZ_USTA_SHORT v2.0
   - Gerçek sentence template'leri
   - Tonality scoring system
   - Flow transition rules (veri bazlı)
   
2. LINGUISTIC_PATTERNS constant
   {
     sentenceStructures: [20 template],
     transitionWords: {hook_to_amplify: [...], ...},
     emphasisWords: {strong: [...], medium: [...]}
   }
   
3. VOICE_CALIBRATION system
   - Her üretilen içeriği Oğuz'un voice fingerprint'ine göre skora
   - Threshold altındaysa uyarı ver
```

---

### Phase 4: BMAD-INSPIRED TESTING (Test Süreci)
**Hedef:** Iterative improvement döngüsü kur

**BMAD Test Flow:**
```
1. GENERATE
   → Prompt'tan 10 farklı script üret

2. SCORE  
   → Her script için:
     - Linguistic similarity (0-100)
     - Voice authenticity (0-100)
     - Flow smoothness (0-100)
     - Hook strength (0-100)
     
3. ANALYZE
   → En yüksek skorlu 3 script'i al
   → En düşük skorluyla karşılaştır
   → Farkları tespit et
   
4. REFINE
   → Prompt'u güncelle
   → Yeni generation yap
   → Tekrar score et
   
5. ITERATE
   → Target: Ortalama skor >85
   → Döngü sayısı: Max 5
```

**Agent Roles:**
- **Generator Agent** → Content creation
- **Scorer Agent** → Similarity metrics
- **Analyzer Agent** → Pattern differences
- **Refiner Agent** → Prompt updates

---

### Phase 5: PRODUCTION DEPLOYMENT
**Hedef:** Sürdürülebilir production pipeline

**BMAD Production Principles:**
```
1. VERSION CONTROL
   - Her prompt update'i git commit
   - Semantic versioning (v2.0.0, v2.1.0)
   
2. A/B TESTING
   - Eski prompt vs yeni prompt
   - Gerçek kullanıcı testleri
   - Skor karşılaştırmaları
   
3. MONITORING
   - Generation quality metrics
   - User feedback loop
   - Continuous refinement
   
4. DOCUMENTATION
   - Her değişikliğin "why"'ını dokümante et
   - Pattern discovery log'u tut
   - Best practices guide
```

---

## 📊 Analysis Scope

### 100 Short Video Analizi Kapsamı

**Quantitative Analysis:**
- Sentence count distribution
- Word frequency (top 500)
- Character count per sentence
- Transition word usage
- Emphasis word placement
- Emoji usage patterns

**Qualitative Analysis:**
- Hook effectiveness (1-5 scale)
- Emotional resonance
- Flow naturalness
- Brand voice consistency
- Call-to-action strength

**Structural Analysis:**
- Hook types (6 kategoriye dağılım)
- PAS framework adoption
- Flow structure variants
- Close formula patterns

---

## 🚀 Implementation Roadmap

### Week 1: Data Mining
- [ ] Script deep_linguistic_analysis.py oluştur
- [ ] 100 short'u process et
- [ ] Pattern database oluştur
- [ ] Initial findings raporu

### Week 2: Pattern Synthesis
- [ ] Sentence template library
- [ ] Flow transition map
- [ ] Voice fingerprint definition
- [ ] Pattern synthesis raporu

### Week 3: Prompt Engineering
- [ ] lib/prompts.ts v2.0 güncellemesi
- [ ] LINGUISTIC_PATTERNS constant ekleme
- [ ] VOICE_CALIBRATION system
- [ ] Integration testing

### Week 4: BMAD Testing Loop
- [ ] Test framework kurulumu
- [ ] 5 iterasyon döngüsü
- [ ] Skor improvement tracking
- [ ] Final optimization

### Week 5: Production
- [ ] Version tagging
- [ ] Documentation completion
- [ ] A/B test setup
- [ ] Monitoring dashboard

---

## 💡 BMAD-Inspired Process Innovations

### 1. Agent Party Mode (Multi-Perspective Review)
Her üretilen içerik için:
- Linguist: "Dil yapısı Oğuz'a uygun mu?"
- Copywriter: "Hook + Flow + CTA çalışıyor mu?"
- YKS Expert: "Bilgi doğru ve işe yarar mı?"
- Student Persona: "Ben bu içeriği anlar/beğenir miyim?"

### 2. Scale-Adaptive Depth
- SHORT (50-750 kar): Yoğun, direkt, hook ağırlıklı
- YATAY (5000-25000 kar): Derinlemesine, empati ağırlıklı, geçişli

### 3. Continuous Learning Loop
```
User Feedback → Pattern Update → Prompt Refine → New Generation → User Feedback
```

### 4. Quality Gates
Her content generation:
- Gate 1: Linguistic similarity >80
- Gate 2: Voice authenticity >85
- Gate 3: Flow smoothness >80
- Gate 4: YKS accuracy 100%

---

## 🔧 Technical Stack

**Analysis:**
- Python 3.11+
- spaCy (Turkish NLP)
- pandas (data analysis)
- matplotlib (visualization)

**Testing:**
- Jest (unit tests)
- Custom scoring framework
- A/B test infrastructure

**Monitoring:**
- Metrics dashboard
- User feedback system
- Version comparison

---

## 📈 Success Metrics

**Quantitative:**
- Linguistic similarity: >85
- Voice authenticity: >90
- User satisfaction: >4.5/5
- Generation speed: <3s

**Qualitative:**
- "Bu Oğuz'un kendisi yazmış gibi"
- Doğal flow
- Kullanılabilir output (copy-paste ready)

---

*Plan created: 26 February 2026*
*Inspired by: BMAD-Method structured workflows*
*Next: Create deep_linguistic_analysis.py script*
