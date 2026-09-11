a= int(input("ievadi skaitli"))
def checkNumber(a):
    if(a%2)==0:
        print(f"{a} ir pāra skaitlis")
    else:
        print(f"{a} nav para skaitlis")
checkNumber(a)