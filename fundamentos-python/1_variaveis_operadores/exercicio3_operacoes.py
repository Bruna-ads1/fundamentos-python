# Exercício 3: Operações básicas 
#Soma de dois números

#Peça dois números e mostre a soma.

#Subtração de dois números

#Peça dois números e mostre a subtração do primeiro menos o segundo.

#Multiplicação de dois números

#Peça dois números e mostre o produto.

#Divisão de dois números

#Peça dois números e mostre o quociente.

print('Olá, vamos praticar operadores básicos começando pela soma?')
n1=int(input('Digite o primeiro número: '))
n2= int(input('Digite o segundo número: '))
total= n1 + n2
print(f'A soma dos números {n1} + {n2} é igual a {total}.')  
print('-------------------------------------------------------------------------------')
print('Perfeito! Agora vamos para subtração.')
v1=int(input('Digite um número: '))
v2=int(input('Digite outro número: '))
sub= v1 - v2
print(f'A subtração dos números {v1} - {v2} é igual a {sub}.')
print("---------------------------------------------------------------------------------------------")
print('Muito bom! Agora vamos complicar mais um puco?')
print('Crie um algoritmo que leia um número e mostre na tela o seu dobro, triplo e raiz quadrada')

número = int(input('Digite um número: '))
dobro = número *2
triplo = número *3
raiz = número ** 0.5
print(f'O dobro do número {número} é igual a {dobro}')
print(f'O triplo do número {número} é igual a {triplo}')
print(f'A raiz quadrada do número {número} é igual a {raiz}')
