# Odaklan SM - Sosyal Medya İçerik Üreticisi

Sosyal medya içerik üretim aracı. Chat arayüzü üzerinden platform seçerek içerik üretir.

## Teknik Altyapı
- **Frontend:** Next.js 16 (App Router), React 19, Tailwind 4, shadcn/ui
- **API:** Anthropic uyumlu endpoint (Yuxor)
- **Streaming:** SSE (Server-Sent Events)

## Çalıştırma
```bash
npm install
cp .env.example .env.local  # API key'leri düzenle
PORT=3002 npm run dev
```

## Yapı
```
app/           → Next.js pages + API routes
components/    → UI bileşenleri (chat, config, sidebar, theme)
hooks/         → React hooks (useChat, useChatHistory)
lib/           → Prompt sistemi, types, utils
```

## Arşiv
Önceki veri/analiz dosyaları `../odaklan-sm-archive/` klasöründe.
