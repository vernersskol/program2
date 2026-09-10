sekundes = int(input("Ievadi sekundes: "))

stundas = sekundes // 3600
sekundes = sekundes % 3600

minutes = sekundes // 60
sekundes = sekundes % 60

print(stundas, "h", minutes, "min", sekundes, "sek")
