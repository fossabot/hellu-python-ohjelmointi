# Kirjoita ratkaisu tähän
palkka = float(input("palkka?"))
tunnit = int(input("työtunnit?"))
paiva = (input("viikonpäivä?"))

if paiva == "sunnuntai":
    print("Palkka", palkka * tunnit * 2, "euroa")

else:
    print("Palkka", palkka * tunnit, "euroa")
