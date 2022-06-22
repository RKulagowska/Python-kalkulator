def dodaj(x,y):
    return x + y 

def odejmin(x,y):
    return x - y

def pomnoz(x,y):
    return x * y 

def podziel(x,y):
    return x / y

print("    Wybierz numer operacji z podanych poniżej:")
print("1.Dodawanie   2.Odejmowanie   3.Dzielenie   4.Mnożenie ")

choice = input("Którą operację wybierasz? Wybierz 1, 2, 3 lub 4:")

num1 = float(input("Podaj pierwszą wartość: "))
num2 = float(input("Podaj drugą wartość: "))
       
if choice == '1':
    print(num1, "+", num2, "=", dodaj(num1,num2))
elif choice == '2':
    print(num1, "-", num2, "=", odejmin(num1,num2))
elif choice == '3':
    print(num1, "*", num2, "=", pomnoz(num1,num2))
elif choice == '4':
    print(num1, "/", num2, "=", podziel(num1,num2))

else:
    print("Podałeś nieobsługiwaną opcję. Wybierz jeszcze raz.")   