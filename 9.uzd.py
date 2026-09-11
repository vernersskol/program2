sakums = int(input("Ievadiet pirmo skaitli (mazāko): "))
beigas = int(input("Ievadiet otro skaitli (lielāko): "))

print(f"Pāra skaitļi diapazonā no {sakums} līdz {beigas}:")

for skaitlis in range(sakums, beigas + 1):

    if skaitlis % 2 == 0:
        print(skaitlis, end=" ")