#Exercício 01
#Crie um programa que imprima "Bom dia!!!" na tela e depois diga que é um prazer te conhecer.
print("Exercício 01")
print("Bom dia!!!")

nome = input("Qual é o seu nome? ")
print("Olá", nome, ". E um prazer te conhecer!!!")


#Exercício 02
#Crie um programa que conte uma história, mas separe por parágrafos e espere o usuário apertar enter para continuar.
print("Exercício 02")
p1 = "Os benefícios do Python incluem:"
p2 = "1. Facilidade de aprendizado"
p3 = "2. Facilidade de leitura"

print(p1)
input()

print(p2)
input()

print(p3)
input()

# ou

input(p1)
input(p2)
input(p3)

#Exercício 03
#Crie um programa que receba um número inteiro e calcule a raiz quadrada desse número e exiba o resultado na tela.
print("Exercício 03")
numero = int(input("Digite um número: "))
#ou numero = input("Digite um número: ")
#numero = int(numero)
raiz = numero ** 0.5 # ou raiz = numero ** (1/2)
raiz = round(raiz, 4) #arredondando para 4 casas decimais
print("A raiz quadrada de", numero, "é", raiz)

#Exercício 04
#Crie um programa que receba um número e calcule o dobro desse número e exiba o resultado na tela.
print("Exercício 04")
#numero = int(input("Digite um número: "))
#ou
numero = input("Digite um número: ")
numero = int(numero)
dobro = numero * 2
print("O dobro de", numero, "é", dobro)