sekundes = int(input("Ievadi sekundes: "))

stundas = sekundes // 3600
minutes = (sekundes % 3600) // 60
sek = sekundes % 60

print(f"{stundas:02d}:{minutes:02d}:{sek:02d}")
print(f"{stundas} h {minutes} min")
