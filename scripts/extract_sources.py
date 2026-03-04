#!/usr/bin/env python3
"""
NotebookLM Source Extractor v5
Kullanım: python3 extract_sources.py <notebook_id> <output_name>
Örnek: python3 extract_sources.py 894072ef oguz_usta_yatay.json
"""
import asyncio
import json
import sys
from pathlib import Path
from datetime import datetime
from notebooklm import NotebookLMClient


async def main():
    if len(sys.argv) < 3:
        print("Kullanım: python3 extract_sources.py <notebook_id> <output_name>")
        print("Örnek: python3 extract_sources.py 894072ef-... oguz_usta_yatay.json")
        sys.exit(1)
    
    notebook_id = sys.argv[1]
    output_name = sys.argv[2]
    
    async with await NotebookLMClient.from_storage() as client:
        print(f"\n📚 Notebook ID: {notebook_id}")
        print(f"📁 Output: data/{output_name}")
        
        sources = await client.sources.list(notebook_id)
        print(f"📄 Toplam source: {len(sources)}")
        
        all_data = {
            "notebook_id": notebook_id,
            "extracted_at": datetime.now().isoformat(),
            "sources": []
        }
        
        seen_titles = set()
        skipped = 0
        errors = 0
        
        for i, source in enumerate(sources, 1):
            title = source.title
            sid = source.id
            
            # Duplicate kontrol
            if title in seen_titles:
                skipped += 1
                continue
            seen_titles.add(title)
            
            print(f"[{i}/{len(sources)}] {title[:65]}...", end=" ", flush=True)
            
            try:
                ft = await client.sources.get_fulltext(notebook_id, sid)
                
                source_data = {
                    "id": sid,
                    "title": title,
                    "kind": str(ft.kind),
                    "content": ft.content,
                    "char_count": ft.char_count
                }
                
                all_data["sources"].append(source_data)
                print(f"✅ {ft.char_count:,} chars")
                
            except Exception as e:
                errors += 1
                print(f"❌ {e}")
                continue
        
        # JSON olarak kaydet
        output_path = Path("data") / output_name
        output_path.parent.mkdir(exist_ok=True)
        
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(all_data, f, ensure_ascii=False, indent=2)
        
        total_chars = sum(s.get('char_count', 0) for s in all_data['sources'])
        print(f"\n{'='*60}")
        print(f"✅ Kaydedildi: {output_path}")
        print(f"📊 Unique source: {len(all_data['sources'])}")
        print(f"⏭️  Atlanmış (duplicate): {skipped}")
        print(f"❌ Hatalar: {errors}")
        print(f"📏 Toplam: {total_chars:,} karakter ({total_chars/1000:.0f}K)")


if __name__ == "__main__":
    asyncio.run(main())
