Ciudades= ["Santiago","Temuco","Osorno","Punta Arenas"]
calidad_aire= [134,99,245,50]

indice_bajo = min(calidad_aire)
ciudad_baja = Ciudades[calidad_aire.index(indice_bajo)]

indice_alto = max(calidad_aire)
ciudad_alta = Ciudades[calidad_aire.index(indice_alto)]


print (f"Ciudad con el índice de calidad del aire más bajo: {ciudad_baja} y su calidad de aire es: {indice_bajo}")
print (f"Ciudad con el índice de calidad del aire más alto: {ciudad_alta} y su calidad de aire es: {indice_alto}")
