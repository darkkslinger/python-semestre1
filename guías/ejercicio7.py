print('Determinar el factorial de un número n')
n=1

while n!=0:
    i,n=1,int(input('Ingrese un número para determinar su factorial (0 para salir): '))
    if n==0:
        break
    suma=n
    while i<n:
        a=n-i
        suma*=a
        i+=1
    print(f'El factorial de {n}! es {suma}')
    