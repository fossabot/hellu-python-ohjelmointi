# Kirjoita ratkaisu tähän
lampo = int(input("lämpötila"))
sade = (input("sataako?"))

print("Pue housut ja t-paita")

if lampo <= 20:
    print("Ota myös pitkähihainen paita")
if lampo <= 10:
    print("Pue päälle takki")
if lampo <= 5:
    print("Suosittelen lämmintä takkia")
    print("Kannattaa ottaa myös hanskat")
if sade == "kyllä":
    print("Muista sateenvarjo!")