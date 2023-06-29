
def identificacionpar(n):
   if n%2==0:
       return n
   else:
       return 0 
   
def identificacionimpar(n):
   if n%2==1:
       return n
   else:
       return 0
   
def prom(lista):
    promedio=sum(lista)/len(lista)
    return promedio

def total(lista):
    sumanum=sum(lista)
    return sumanum

def num_mayor(lista):
    mayor=max(lista)
    return mayor

listanum=[]
n=sumpar=sumimpar=sumatotal=0

while True:
    try:
        n=int(input('Ingrese un número (-1 para salir): '))
        if n==-1:
            break
        else:
            listanum.append(n)
            sumpar+=identificacionpar(n)
            sumimpar+=identificacionimpar(n)
    except:
        print('Ingresa un valor válido')
        n=int(input('Ingrese un número (-1 para salir): '))
        if n==-1:
            break
        else: 
            listanum.append(n)
            sumpar+=identificacionpar(n)
            sumimpar+=identificacionimpar(n)
mayor=num_mayor(listanum)
suma=total(listanum)
promedio=round(prom(listanum))
print(f'La suma de pares es: {sumpar}')
print(f'La suma de impares es: {sumimpar}')
print(f'La suma total es: {suma}')
print(f'El promedio es: {promedio}')
print(f'El numero mayor ingresado fue: {mayor}')
if mayor>promedio:
    print(f'El número es mayor que el promedio y este es {mayor}')
elif mayor == promedio:
    print(f'El promedio es igual al mayor y es {promedio}')
else:
    print(f'El número es menor que el promedio y este es {mayor}')
