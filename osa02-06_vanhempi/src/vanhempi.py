# Kirjoita ratkaisu tähän
#henkilö 1:
nimi1 = input("Nimi: ")
ika1 = int(input("Ikä: "))

#henkilö 2:
nimi2 = input("Nimi: ")
ika2 = int(input("Ikä: "))

if ika1 > ika2:
    print("Vanhempi on", nimi1)
elif ika1 < ika2:
    print("Vanhempi on", nimi2)
else:
    print(nimi1, "ja", nimi2,"ovat yhtä vanhoja")
