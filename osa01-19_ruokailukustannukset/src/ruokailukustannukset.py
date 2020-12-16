# Kirjoita ratkaisu tähän
kertaa = int(input("Montako kertaa? "))
hinta = float(input("Paljonko maksaa? "))
ruokaostokset = float(input("kuinka paljon käytät ruokaostoksiin "))


print("Kustannukset keskimäärin:")
print("Päivässä", kertaa * hinta /7 + ruokaostokset /7, "euroa")
print("Viikossa", kertaa * hinta + ruokaostokset, "euroa")
