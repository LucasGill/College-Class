#ex 1 
N1= float(input('Entre com sua nota: '))
N2= float(input('Entre com sua nota: '))
N3= float(input('Entre com sua nota: '))
ME= N1 + N2 + N3 / 3
MA = (N1 + N2*2 + N3*3 + ME)/7

if MA >= 9:
    print('nota A')
elif MA >= 4:
    print ('nota C')
else:
    print('nota B')

#ex 2
nome= str(input('Qual seu nome? '))
end= str(input('Qual seu endereço? '))
CEP= str(input('Qual seu CEP? '))
tel= str(input('Qual seu telefone? '))

print('/nOlá,', nome, '\n')
print('morador do endereço,', end, '\n')
print('com CEP,', CEP, '\n')
print('de telefone,', tel, '\n')

#ex 3 
print('XXXXX')
print('X   X')
print('X   X')
print('X   X')
print('XXXXX')

#ex 4
nome= str(input('Diga o nome do(a) aluno(a): '))
nota= float(input('digite a nota: '))

print(' Nome    Nota \n', '=======   ===== \n', nome,'   ',nota)

#ex 4
end= ('0- end')
add= ('1- Join in')
update= ('2- Update')
delete= ('3- Delete')
check= ('4- Check')

print('Welcome to the Customer Registration')
print(end)
print(add)
print(update)
print(delete)
print(check)

customerChoice= int(input('Please, choose an option (Just the number): \n'))

if customerChoice == 0:
    print('BYE BYE!')

elif customerChoice == 1:
    print('Hello, welcome! Let\'t\'s start?')

elif customerChoice == 2:
    print('We are on the uptade menu. Be free to change your data.') 

elif customerChoice == 3:
    print('Are you sure you want to delete every data you had  archive here?') 

elif customerChoice == 4:
    print('Le\'t\'s check your information.') 

else:
    print('Error! Try to select a valid option.')

#ex 5

print('       X')
print('      XXX')
print('     XXXXX')
print('    XXXXXXX')
print('   XXXXXXXXX')
print('  XXXXXXXXXXX')
print(' XXXXXXXXXXXXX')
print('XXXXXXXXXXXXXXX')
print('      XX')
print('      XX')
print('     XXXX')

#ex 6


x = 17
y= 3.2

a= x / 4 + y 
b= x * y ** 6
c= (x % 4) , ((int(y) * 10) //4)
d= (x / 6 // x / 3) + 4

print(a)
print(b)
print(c)
print(d)

#ex 7

numOfTerms= float(input('Enter with the number of the terms: \n'))
initialValue= float(input('Enter with the initial value: \n'))
finalValue= float(input('Enter with the final value: \n'))

S = numOfTerms*(initialValue + finalValue)/2

print('The result is: ', S)

#ex 8

initialValue=float(input('Enter with the initial value: \n'))
numberOfTerms= float(input('Enter with the number of the terms: \n'))
ratio= float(input('Enter with the ratio: \n'))
    

if ratio < 2:
    print('ERROR! Try to enter a ratio bigger than or equal to 2.')

else:
   print(initialValue*(ratio**numberOfTerms -1) / (ratio-1))

#ex9
birthYear=int(input('Enter with the year you were born: \n'))

if birthYear <= 2007:
    print('You can vote!')

else:
    print("You can't vote this year! ")

#ex 10

passcode=int(input('Hi! Please type the passcode!\n' ))

if passcode == 8765:
    print('Access Allowed.')

else:
    print('Access Denied.')

#ex 11

height= float(input('Hello! Please, type your height: \n'))
sex= int(input('Now, your sex (Type the number): \n 1-Female \n  2- Male \n' ))
 
male = (72.7 * height) - 58
female= (62.1 * height) - 44.7

if sex == 1:
    print('Your ideal weight is:', female)

elif sex == 2:
    print('Your ideal weight is:', male)

else:
    print('ERROR! Try to type a valid option (1-2) in sex.')

#ex 12


polygon= int(input('Type how many side numbers did your polygon have? \n'))

if polygon < 3: 
    print("Not a polygon.")

elif polygon == 3:
   print("I'ts a triangle! And your area is: A = b*h/2")

elif polygon == 4:
    print("It's a square! And your area is: A= a **2")

elif polygon == 5:
    print("It's a pentagon! And your area is: A= p * a/2")

else:
    print("Polygon not identified.")

polygon= int(input('Type how many side numbers did your polygon have? \n'))

if polygon < 3:
    print("It's not a polygon.")

elif polygon == 3:
    print("I'ts a triangle! And the formula of area is: A = b*h/2. Should we calculate?")
    print('')
    base= float(input('Enter with the value of the base: \n'))
    height= float(input('Enter with the value of the height: \n'))
    area= base * height / 2
    print('The triangle area is:', area )
    

elif polygon == 4:
    print("It's a square! And your area is: A= a **2. Should we calculate?")
    print('')
    side= float(input("Enter with the value of the side: \n" ))
    area = side ** 2
    print("The square area is:", area)


elif polygon == 5:
    print("It's a pentagon! And your area is: A= p * a/2. Should we calculate?")
    print("")
    perimeter = float(input("Enter with the value of the perimeter: \n"))
    apothem= float(input("Enter with the value of the apothem: \n"))
    area = perimeter * apothem / 2 
    print("The pentagon area is:", area)


else:
    print("Polygon not identified.")