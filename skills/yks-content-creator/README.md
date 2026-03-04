# YKS Content Creator Skill

Claude Code skill for creating YKS-focused social media content based on 233 video transcripts (~700K words) from Oğuz Usta, Baykus Mentörlük, and competitor channels.

## Overview

This skill helps create authentic YKS (Yükseköğretim Kurumları Sınavı) content for:
- Instagram Reels (SHORT, 15-60s)
- TikTok (SHORT, 15-60s)
- YouTube Shorts (SHORT, 60s)
- YouTube Yatay (LONG, 10-20dk)

## Data Sources

- **Oğuz Usta**: 123 videos
- **Baykus Mentörlük**: 50 videos
- **Competitors**: 60 videos
- **Total**: 233 transcripts (~700K words)

## Key Features

### 6 Hook Types (Oğuz Usta Style)
1. **SORU Hook** (%53 dominant)
2. **ŞAŞIRTICI İDDİA Hook**
3. **SAYI + SONUÇ Hook**
4. **KARŞITLIK Hook**
5. **HİKAYE Hook**
6. **UYARI Hook**

### PAS Framework
- **Problem** (HOOK)
- **Amplify** (YANI)
- **Agitate** (PEKİ)
- **Solve** (YANI ŞUNU YAP)

### 5 Content Pillars
1. YKS Stratejisi (30%)
2. Branş Taktikleri (25%)
3. Motivasyon (20%)
4. Kaynak Önerileri (15%)
5. Soru Çözümü (10%)

## Files

- **[SKILL.md](SKILL.md)** — Main skill definition with frameworks
- **[references/yks-terminology.md](references/yks-terminology.md)** — Top 20 YKS terms
- **[references/hook-formulas.md](references/hook-formulas.md)** — 6 hook types + PAS framework
- **[references/platform-strategies.md](references/platform-strategies.md)** — Platform-specific strategies
- **[references/content-pillars.md](references/content-pillars.md)** — 5 pillar framework

## Top YKS Terms (233 Video Analysis)

| Terim | Frekans | Kullanım Alanı |
|-------|---------|----------------|
| deneme | 4426x | Her derste, analiz şart (KRİTİK) |
| konu | 4172x | Konu çalışması |
| TYT | 2276x | Temel yeterlilik |
| çalışma | 2213x | Çalışma stratejisi |
| net | 1992x | Puan hesaplama |
| AYT | 1877x | Alan yeterlilik |
| matematik | 1360x | Matematik branşı |

## Installation

For Claude Code, add this skill to your `.claude/skills/` directory.

## Usage

When creating YKS content:
1. Specify platform (Instagram Reel, TikTok, YouTube Shorts, YouTube Yatay)
2. Provide topic (TYT, AYT, deneme analizi, motivasyon)
3. Mention audience (11. sınıf, 12. sınıf, mezun, EA/Sayısal/Sözel)

## License

MIT

## Credits

Based on marketingskills repo (10,510 stars) structure and Oğuz Usta's content style.

---

**Status:** Ready for use with Claude Code
**Last Updated:** March 2026
**Version:** 1.0.0
