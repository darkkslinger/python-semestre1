i,j,suma=500,456,0
for i in range(500,801,10):
    suma+=i
    if i<=800: 
        suma+=j
        j-=2
print(f'La sumatoria es de {suma}')