import os

os.system("cls")

print('''
██████╗░██████╗░░█████╗░███████╗███████╗░██████╗░██████╗░█████╗░██████╗░
██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝██╔════╝██╔══██╗██╔══██╗
██████╔╝██████╔╝██║░░██║█████╗░░█████╗░░╚█████╗░╚█████╗░██║░░██║██████╔╝
██╔═══╝░██╔══██╗██║░░██║██╔══╝░░██╔══╝░░░╚═══██╗░╚═══██╗██║░░██║██╔══██╗
██║░░░░░██║░░██║╚█████╔╝██║░░░░░███████╗██████╔╝██████╔╝╚█████╔╝██║░░██║
╚═╝░░░░░╚═╝░░╚═╝░╚════╝░╚═╝░░░░░╚══════╝╚═════╝░╚═════╝░░╚════╝░╚═╝░░╚═╝''')

nome = input ("Digite seu nome: ")
quantidade = int(input("Digite a quantidade de aulas:  "))
nível =  int(input("Digite o seu nivel:  "))

salário = quantidade * nível

Nivel01 = 12.00
Nivel02 = 17.00
Nivel03 = 25.00


if (Nivel01):
    salário = (12.00 * quantidade) * 4
    
elif (Nivel02):
    salário = (17.00 * quantidade) * 4
    
else: (Nivel03)
salário = (25.00 * quantidade) * 4 


print("O resultado do salário é: ", salário)
