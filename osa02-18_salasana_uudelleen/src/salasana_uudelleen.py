# Kirjoita ratkaisu tähän
salasana = input("Salasana: ")
salasana2 = input("Toista salasana: ")
while True:
    if salasana2 == salasana:
        print("Käyttäjätunnus luotu!")
        break
    else:
        print("Ei ollut sama!")
        salasana2 = input("Toista salasana:")
        
        


