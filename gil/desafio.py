n1= int(input("Digite o 1º número: "))
n2= int(input("Digite o 2º número: "))
n3= int(input("Digite o 3º número: "))

if n1>n2 and n1>n3:
    print("O número", n1, "é maior")
elif n2>n1 and n2>n3:
    print("O número", n2, "é maior")
else: 
    print("O número", n3, "é maior")

n4= int(input("Digite o 1º número: "))
n5= int(input("Digite o 2º número: "))
n6= int(input("Digite o 3º número: "))

if n4<n5 and n4<n6:
    print("O número", n4, "é menor")
elif n5<n4 and n5<n6:
    print("O número", n5, "é menor")
else: 
    print("O número", n6, "é menor")

