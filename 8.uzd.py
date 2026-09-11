sakums = int(input("Ievadiet sākuma vērtību: "))
beigas = int(input("Ievadiet beigu vērtību: "))
summa = 0



for skaitlis in range(sakums, beigas + 1):
    summa = summa + skaitlis
    print(skaitlis, end=" ")
print(f"Visu skaitlu summa no {sakums} lidz {beigas} ir {summa}")