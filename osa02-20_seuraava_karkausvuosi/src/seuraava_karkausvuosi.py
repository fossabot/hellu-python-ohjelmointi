# Kirjoita ratkaisu tähän
vuosi = int(input('Vuosi:'))
alk_vuosi = vuosi
while True:
    if vuosi % 4 == 0:
        karkausvuosi = vuosi + 4
        if karkausvuosi % 100 == 0:
            karkausvuosi2 = karkausvuosi +4
            print ('Vuotta',alk_vuosi,'seuraava karkausvuosi on',karkausvuosi2)
        else:
            print ('Vuotta',alk_vuosi,'seuraava karkausvuosi on',karkausvuosi)
        break
    else:
        vuosi += 1
        if vuosi % 4 == 0:
            if vuosi % 400 == 0:
                print ('Vuotta',alk_vuosi,'seuraava karkausvuosi on', vuosi)
            elif vuosi % 100 == 0:
                vuosi1 = vuosi + 4
                print ('Vuotta',alk_vuosi,'seuraava karkausvuosi on', vuosi1)
            else:
                print ('Vuotta',alk_vuosi,'seuraava karkausvuosi on', vuosi)
            break