print("Digite 3 números diferentes: ")
num1 = float(input("Número 1: "))
num2 = float(input("Número 2: "))
num3 = float(input("Número 3: "))

if (num1 == num2) or (num1 == num3) or (num2 == num3):
    print("Por que não me obedece?")
else:
    if num1<num2<num3:
        print(f"O número {num3} é o maior e o {num1} é o menor número.")
    elif num1<num3<num2:
        print(f"O número {num2} é o maior e o {num1} é o menor número.")
    elif num2<num1<num3:
        print(f"O número {num3} é o maior e o {num2} é o menor número.")
    elif num2<num3<num1:
        print(f"O número {num1} é o maior e o {num2} é o menor número.")
    elif num3<num1<num2:
        print(f"O número {num2} é o maior e o {num3} é o menor número.")
    else:
        print(f"O número {num1} é o maior e o {num3} é o menor número.")