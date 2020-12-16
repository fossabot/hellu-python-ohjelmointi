from math import sqrt
# Kirjoita ratkaisu tähän
from math import sqrt
# Kirjoita ratkaisu tähän
luku = float(input("Syötä luku: "))
while True:
    if 0 < luku:
        print(sqrt(luku))
        luku = float(input("Syötä luku: "))
    if luku < 0:
        print("Epäkelpo luku")
        luku = float(input("Syötä luku: "))
    if luku == 0:
        print("Lopetetaan...")
        break
    