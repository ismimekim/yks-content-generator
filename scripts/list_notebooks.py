#!/usr/bin/env python3
"""
NotebookLM Notebook Listesi
"""
import asyncio
from notebooklm import NotebookLMClient


async def main():
    async with await NotebookLMClient.from_storage() as client:
        notebooks = await client.notebooks.list()
        print(f"📚 Toplam notebook: {len(notebooks)}\n")
        for n in notebooks:
            print(f"ID: {n.id}")
            print(f"   Başlık: {n.title}")
            print(f"   Kaynak sayısı: {n.source_count}")
            print()


if __name__ == "__main__":
    asyncio.run(main())
