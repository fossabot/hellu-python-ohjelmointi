# Kirjoita ratkaisu tähän
yritykset = 0

while True:    
    pin = int(input("Pinkoodi:"))
    yritykset += 1
    if pin == 4321 and yritykset == 1:
        print("Oikein, tarvitsit vain yhden yrityksen!")
        break
    
    if pin == 4321:
        print("Oikein, tarvitsit", yritykset,"yritystä")
        break
    
    
    else: 
        print("Väärin")
