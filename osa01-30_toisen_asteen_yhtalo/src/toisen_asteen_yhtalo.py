# Kirjoita ratkaisu tähän
# Otetaan käyttöön neliöjuuri math-moduulista
from math import sqrt

a = float(input("paljonko on a"))
b = float(input("paljonko on b"))
c = float(input("paljonko on c"))

juuri1 = (-b + sqrt((b ** 2) -4 * a * c))/(2*a)
juuri2 = (-b - sqrt((b ** 2) -4 * a * c))/(2*a)

print("Juuret ovat", juuri2, "ja", juuri1)


# Huomaa, että neliöjuuren voi laskea myös potenssin avulla:
# sqrt(9) on sama asia kuin 9 ** 0.5

