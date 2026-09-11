sakums = int(input("Ievadiet pirmo skaitli (mazāko): "))
beigas = int(input("Ievadiet otro skaitli (lielāko): "))

print(f"skaitļi iznemot tos kas dalas ar 5 {sakums} līdz {beigas}:")

for skaitlis in range(sakums, beigas + 1):

    if skaitlis % 5 != 0:
        print(skaitlis, end=" ")