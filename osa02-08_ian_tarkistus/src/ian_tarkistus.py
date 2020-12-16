# Kirjoita ratkaisu tähän
ika = int(input("kerro ikäsi? "))

if ika >= 5:
    print("Ok, olet siis", str(ika) + "-vuotias")
elif ika <5 and ika >=0:
    print("En usko, että osaat kirjoittaa...")
else:
    print("Taitaa olla virhe")