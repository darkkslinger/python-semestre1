import statistics
listas = [4, 3, 8, 12 , 6, 10, 14, 3, 6]
listas.pop()
listas.insert (0, 2)
listas = list(set(listas))
listas = [4, 3, 8, 12 , 6, 10, 14, 3, 6]
media = round(statistics.mean(listas),1)  
mediana = statistics.median(listas)
print (media)
print (mediana)
print (listas)