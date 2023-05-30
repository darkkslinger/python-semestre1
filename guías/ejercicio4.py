print('Algoritmo: Propiedad de Nicomaco de Gerasa')
n=int(input('Ingrese n: '))
impar = 1
for i in range(1,n+1):
    print(f'{i}³= ',end='') 
    suma = 0
    for j in range(i):
        suma+=impar
        if j!=0:
            print(' + ',end='')
        print(impar,end='')
        impar+=2
    print(f' = {suma}')