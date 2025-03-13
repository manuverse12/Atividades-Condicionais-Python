import os

os.system("cls")

print('''
██╗███╗░░░███╗░█████╗░
██║████╗░████║██╔══██╗
██║██╔████╔██║██║░░╚═╝
██║██║╚██╔╝██║██║░░██╗
██║██║░╚═╝░██║╚█████╔╝
╚═╝╚═╝░░░░░╚═╝░╚════╝░''')

nome = input ("Digite seu nome: ")
altura = float(input("Digite sua altura:  "))
peso = float (input("Digite seu peso:"))


imc = peso/(altura*altura)


if (imc <= 16.9 ):
    print("Você está muito abaixo do peso.")

elif (imc >= 17 and imc <= 18.4): 
    print("Você está abaixo do peso.")

elif (imc >= 18.5 and imc <= 24.9):
    print("Peso normal.")

elif (imc >= 25 and imc <= 29.9):
    print("Você acima do peso.")

elif (imc >= 30 and imc <= 34.9):
    print("Você está na obesidade grau I.")

elif (imc >= 35 and imc <= 40):
    print("Você esta na obesidade grau II.")

elif (imc > 40):
    print("Você esta na obesidade grau III.")


print("Seu IMC é:  ", imc)