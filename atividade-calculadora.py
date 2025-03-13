import os

os.system("cls")

print('''
░█████╗░░█████╗░██╗░░░░░░█████╗░██╗░░░██╗██╗░░░░░░█████╗░██████╗░░█████╗░██████╗░░█████╗░
██╔══██╗██╔══██╗██║░░░░░██╔══██╗██║░░░██║██║░░░░░██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔══██╗
██║░░╚═╝███████║██║░░░░░██║░░╚═╝██║░░░██║██║░░░░░███████║██║░░██║██║░░██║██████╔╝███████║
██║░░██╗██╔══██║██║░░░░░██║░░██╗██║░░░██║██║░░░░░██╔══██║██║░░██║██║░░██║██╔══██╗██╔══██║
╚█████╔╝██║░░██║███████╗╚█████╔╝╚██████╔╝███████╗██║░░██║██████╔╝╚█████╔╝██║░░██║██║░░██║
░╚════╝░╚═╝░░╚═╝╚══════╝░╚════╝░░╚═════╝░╚══════╝╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝''')

valor01 = int (input("Digite o primeiro número: "))
valor02 = int (input("Digite o segundo número: "))
operação = input("Digite a operação:  ")

if (operação == "+"):
   resultado = valor01 + valor02
   print("Será feita a soma de dois valores")

elif (operação == "-"):
   resultado = valor01 - valor02
   print("Será feita a subtração de dois valores")

elif (operação == "/"):
   resultado = valor01 / valor02
   print("Será feita a divisão de dois valores")

elif (operação == "*"):
    resultado = valor01 * valor02
    print("Será feita a multiplicação de dois valores")


print("O resultado foi: " , resultado) 


