# Kirjoita ratkaisu tähän
lahja = int(input("Lahjan suuruus? "))

if lahja >= 5000 and lahja <= 25000:
    print("Vero:", 100 + (lahja - 5000) * 0.08)
elif lahja >= 25000 and lahja <= 55000:
    print("Vero:", 1700 + (lahja - 25000) * 0.10)
elif lahja >= 55000 and lahja <= 200000:
    print("Vero:", 4700 + (lahja - 55000) * 0.12)
elif lahja >= 200000 and lahja <= 1000000:
    print("Vero:", 22100 + (lahja - 200000) * 0.15)
elif lahja > 1000000:
    print("Vero:", 142100 + (lahja - 1000000) * 0.17)
else:
    print("Ei veroa!")