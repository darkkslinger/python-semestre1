import random
lista=[]
for i in range(0,20):
    lista.append(random.randint(40,350))
    print(f'El número elegido al azar es: {lista[i]}')
buscar=int(input('Ingrese un número para conocer su cantidad de ocurrencias: '))
print(f'La cantidad de ocurrencias del número {buscar} es de: {lista.count(buscar)}')