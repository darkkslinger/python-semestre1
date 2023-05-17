# import statistics
# listas = [4, 3, 8, 12 , 6, 10, 14, 3, 6]
# listas.pop()
# listas.insert (0, 2)
# listas = list(set(listas))
# listas = [4, 3, 8, 12 , 6, 10, 14, 3, 6]
# media = round(statistics.mean(listas),1)  
# mediana = statistics.median(listas)
# print (media)
# print (mediana)
# print (listas)

numeros=[4,3,8,12,6,10,14,3,6]
numeros.pop(-1)
print(f'La lista con el ultimo numero eliminado es: {numeros} \n')

numeros.insert(0,2)
print(f'Añadiendo el 2 en la primera posición de la lista: {numeros} \n')

numeros=list(set(numeros))
print(f'Eliminando los duplicados {numeros} \n')
numeros=[4,3,8,12,5,10,14,3,6]
# ----  Media  ----
cantidad=len(numeros)
suma=sum(numeros)
media=round((suma/cantidad),1)
# ---- Mediana ----
numeros.sort()
mediana_index=(cantidad//2)
if (cantidad/2)%1==0.5:
    mediana=numeros[mediana_index]
else:
    mediana1=numeros[mediana_index-1]
    mediana2=numeros[mediana_index]
    mediana=(mediana1+mediana2)/2
print(f'La lista ordenada es {numeros} y su media es de {media} y su mediana es {mediana}')

