temperaturas_min = {9, 5, 2, 7, 6, 1}
temperaturas_max = {12, 14, 11, 10, 15, 9}

if 5 in temperaturas_min and 5 in temperaturas_max:
    print("temperatura 9 está en ambos set")
else:
    print("temperatura 9 no está en ambos set")

if 6 in temperaturas_min or 6 in temperaturas_max:
    print("temperatura 6 encontrada en uno de los sets")
else:
    print("temperatura 6 no encontrada en los sets")
if 17 in temperaturas_min or 17 in temperaturas_max:
    print("temperatura 17 encontrada en uno de los sets")
print("temperatura 17 no encontrada en los sets")

#temperaturas_min={**4 for in temperaturas_min}
#temperaturas_max={**4 for in temperaturas_max}
#temperaturas_min=(temperaturas_min**4)
#print(temperaturas_min)
#temperaturas_max=(temperaturas_max**4)
#print(temperaturas_max)

temperaturas=temperaturas_max.union(temperaturas_min)
print(temperaturas)
