#Exercício Python 13: Faça um programa que leia três números e
# mostre qual é o maior e qual é o menor.
n1 = float(input("Insira o primeiro número: "))
n2 = float(input("Insira o segundo número: "))
n3 = float(input("Insira o terceiro número: "))
maior = n1
if n2 > n1 and n2 > n3:
   maior = n2
if n3 > n1 and n3 > n2:
   maior = n3
menor = n1
if n2 < n3 and n2 < n1:
   menor = n2
if n3 < n2 and n3 < n1:
   menor = n3
print(f"O menor número inserido foi {menor}")
print(f"O maior número inserdo foi {maior}")