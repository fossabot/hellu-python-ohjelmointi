opiskelijoita = int(input("Montako opiskelijaa? "))
ryhmakoko = int(input("Ryhmän koko: "))

ryhmia = opiskelijoita // ryhmakoko
if opiskelijoita / ryhmakoko > ryhmia:
    ryhmia += 1

print("Ryhmien määrä:", ryhmia)
