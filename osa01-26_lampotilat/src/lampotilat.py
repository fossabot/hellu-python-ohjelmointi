# Kirjoita ratkaisu tähän
lampotila = int(input("lämpötila?"))

celcius = ((lampotila - 32) / (9/5))
print(lampotila, "fahrenheit-astetta on", celcius,"celcius-astetta")


if celcius < 0:
    print("Paleltaa!")


