numeros = []
for i in range(int(input())):
    if (numero := int(input())):
        numeros.append(numero)
    else:
        numeros.pop()
soma = 0
for numero in numeros:
    soma += numero
print(soma)