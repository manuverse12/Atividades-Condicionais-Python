import os

os.system("cls")

print ('''
█▀▄▀█ █▀▀ █▀█ █▀▀ ▄▀█ █▀▄ █▀█
█░▀░█ ██▄ █▀▄ █▄▄ █▀█ █▄▀ █▄█''')

produto = input("Digite o nome do produto:  ")
quantidade = int(input("Digite a quantidade de produtos que deseja:  "))
preço = float(input("Digite o valor únitario:  "))
desconto2 = input ("Digite o valor do desconto:  ")
desconto3 = input ("Digite o valor do desconto:  ")
desconto5 = input ("Digite o valor do desconto:  ")

total = quantidade * preço

desconto2 = 2 / 100
desconto3 = 3 / 100
desconto5 = 5 / 100

if (quantidade <= 5): 
    desconto = preço * 0.02
    print("O desconto será de 2%")

elif (quantidade >5 and quantidade <= 10):
    desconto = preço * 0.03
    print("O desconto será de 3%")

else: (quantidade >10 )
desconto = preço * 0.05
print("O desconto será de 5%")

print ("Total a pagar: ", preço - desconto)


 