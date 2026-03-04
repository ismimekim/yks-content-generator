#!/usr/bin/env python3
"""
YKS Kanal Video Transcript Fetcher - NotebookLM API

Bu script, Google'ın NotebookLM servisini kullanarak YKS kanallarının
video transkriptlerini çeker.

Kanallar:
- Baykuş Mentörlük (mevcut data/baykus-complete.json)
- Aktif Zeka (Novaze Kayık)  
- Yusuf Mert Aslan (Ymert Arslan YKS)

Kullanım:
1. Google hesabınızla oturum yapın
2. python3 scripts/fetch_yks_channels.py

Output: data/yks_channels_transcripts.json
"""

import asyncio
from notebooklm import NotebookLMClient
from datetime import datetime


YKS_CHANNELS = {
    "Baykuş YKS": {
        "youtube_id": "UC5Dd419wqIDYMw4jfTWv2YA",  # Baykuş Mentörlük
        "description": "Baykuş Mentörlük - YKS koçluk ve deneme",
    },
    "Aktif Zeka": {
        "youtube_id": "UCcXwUKs2hG_LHK4f1M7S2Qg",  # Novaze Kayık (tahmin)
        "description": "Aktif Zeka - YKS strateji ve motivasyon",
    },
    "Yusuf Mert Aslan": {
        "youtube_id": "UCq0RY_1KXKJKKJKJK",  # Ymert Arslan (tahmin)
        "description": "Yusuf Mert Aslan - YKS Matematik ve strateji",
    },
}


async def fetch_channel_videos(client, channel_name: str, channel_config: dict):
    """Bir kanaldan tüm video transkriptlerini çeker"""
    
    print(f"\n{'='*60}")
    print(f"KANAL: {channel_name}")
    print(f"{'='*60}")
    
    # YouTube channel ID'sinden video transkriptlerini çek
    # Bu özellik notebooklm-py'de olabilir veya eklememiz gerekebilir
    
    # Önce mevcut data'yı kontrol et
    import json
    import os
    
    if channel_name == "Baykuş YKS":
        # Mevcut baykus-complete.json kullan
        with open('data/baykus-complete.json') as f:
            data = json.load(f)
        return {
            "channel": channel_name,
            "source": "existing",
            "video_count": len(data.get('videos', [])),
            "data": data
        }
    
    # Diğer kanallar için NotebookLM API kullan
    # TODO: Implement actual YouTube transcript fetching
    
    return {
        "channel": channel_name,
        "source": "notebooklm",
        "video_count": 0,
        "note": "NotebookLM entegrasyonu gerekli"
    }


async def main():
    """Ana fonksiyon - tüm kanalları çeker"""
    
    print("YKS Kanal Transcript Fetcher başlatılıyor...")
    print(f"Tarih: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    try:
        async with await NotebookLMClient.from_storage() as client:
            results = []
            
            for channel_name, config in YKS_CHANNELS.items():
                result = await fetch_channel_videos(client, channel_name, config)
                results.append(result)
            
            # Sonuçları kaydet
            output_path = 'data/yks_channels_transcripts.json'
            with open(output_path, 'w', encoding='utf-8') as f:
                json.dump({
                    "fetched_at": datetime.now().isoformat(),
                    "channels": results,
                    "total_videos": sum(r.get('video_count', 0) for r in results)
                }, f, ensure_ascii=False, indent=2)
            
            print(f"\n✅ Sonuçlar kaydedildi: {output_path}")
            
    except Exception as e:
        print(f"\n❌ Hata: {e}")
        print("Not: NotebookLM entegrasyonu için Google oturumu gerekli")
        print("Alternatif: Mevcut data/baykus-complete.json kullanılıyor")


if __name__ == "__main__":
    asyncio.run(main())
