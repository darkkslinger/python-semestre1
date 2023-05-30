parrafo=('''
La Universidad de los Lagos es una institución estatal fundada en 1993. Esta universidad regional
entrega una contribución significativa al desarrollo sostenible del territorio. Como Universidad sus
pilares fundamentales se basan en la inclusión, pluralismo, conciencia ambiental y participación democrática
''').lower().split()

parrafo=tuple(parrafo)

print(f'La cantidad de veces que se repite la palabra "Universidad" es de: {(parrafo.count("universidad"))} veces')