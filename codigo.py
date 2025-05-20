 def soma(numeroA, numeroB):
 resultado = numeroA + numeroB
 print(f"resultado da soma: {resultado}")
def subtracao(numeroA, numeroB):
 resultado = numeroA - numeroB
 print(f"resultado da subtração: {resultado} ")
def divisao(numeroA, numeroB):
 resultado = numeroA / numeroB
 print(f"resultado da divisão: {resultado}")
def multiplicacao(numeroA, numeroB):
 resultado = numeroA * numeroB
 print(f"resultado da multiplicação: {resultado}") 
def raiz(numeroA):
  resultado = numeroA ** 0.5
  print(f"resultado da raiz: {resultado}")

opcao = int(input("para fazer sua conta contendo apenas números, escolha a fórmula."))

if (opcao == 1):
  numeroA = float(input("digite o 1° número"))
  numeroB = float(input("digite o 2° número"))
  soma(numeroA, numeroB)

if (opcao == 2):
  numeroA = float(input("digite o 1° número"))
  numeroB = float(input("digite o 2° número"))
  subtracao(numeroA, numeroB)

if (opcao == 3):
  numeroA = float(input("digite o 1° número"))
  numeroB = float(input("digite o 2° número"))
  divisao(numeroA, numeroB)

if (opcao == 4):
  numeroA = float(input("digite o 1° número"))
  numeroB = float(input("digite o 2° número"))
  multiplicacao(numeroA, numeroB)

if (opcao == 5):
  numeroA = float(input("digite o 1° número"))
  numeroB = float(input("digite o 2° número"))
  raiz(numeroA)
  
