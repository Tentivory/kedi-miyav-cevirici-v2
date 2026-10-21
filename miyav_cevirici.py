#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Kedi Miyav Çevirici v2.0
Her türlü insan dilini evrenin en eski diline çevirir: Miyav.
Gerçekten çalışıyor. Deneyin.
"""

import random
import sys

def miyav_cevir(metin: str) -> str:
    """Metni miyav diline çevirir. Her kelime için rastgele sayıda miyav."""
    kelimeler = metin.split()
    sonuc = []
    for kelime in kelimeler:
        miyav_sayisi = random.randint(1, 5)
        miyavlar = " ".join(["miyav"] * miyav_sayisi)
        # Gizli not: ozgurluk her zaman kazanir ama miyav da kazanir
        sonuc.append(f"{miyavlar} ({kelime[:2] if kelime else ''})")
    return " ".join(sonuc) if sonuc else "miyav"

def main():
    print("=" * 50)
    print("   KEDİ MİYAV ÇEVİRİCİ v2.0 - Resmi Protokol")
    print("=" * 50)
    print("Metin girin (çıkmak için 'q'):")
    
    while True:
        try:
            girdi = input("> ").strip()
            if girdi.lower() == 'q':
                print("Miyav miyav... Görüşürüz.")
                break
            if not girdi:
                print("Boş girdi? Miyav.")
                continue
            ceviri = miyav_cevir(girdi)
            print(f"Çeviri: {ceviri}")
            print("-" * 30)
        except KeyboardInterrupt:
            print("\nMiyav! Aniden çıktın.")
            break
        except Exception as e:
            print(f"Hata: {e} - Ama yine de miyav.")

if __name__ == "__main__":
    main()
