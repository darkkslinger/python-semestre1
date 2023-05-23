n=int(input("Ingrese un número: "))
print ()
if n % 2==0:
    print (n," es par","\n")
else:
    print (n, " es impar","\n")

nprimo = True
if n < 2:
    nprimo= False
else:
    i=2
    while i < n:
        if n % i ==0:
            nprimo= False
            break
        i+=1

if nprimo:
    print (n,"es primo","\n")
else:
    print (n, "no es primo","\n")

if n > 50:
    print (n," es mayor a 50","\n")
elif n < 50:
    print (n," es menor a 50","\n")
else:
    print ("numero ingresado es igual a 50","\n")




