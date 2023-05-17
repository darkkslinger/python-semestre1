nombre=input("Ingresar nombre del estudiante: ")
asignatura= input("Ingrese la asignatura correspondiente: ")
lab1=float(input("Ingrese nota de laboratorio 1: "))
lab2=float(input("Ingrese nota de laboratorio 2: "))

promedio= (lab1)*0.3 + (lab2)*0.7

dic= {
    "nombre_estudiante": nombre,
    "nombre_asignatura": asignatura,
    "nota_lab1": lab1,
    "nota_lab2": lab2,
    #round=redondear      1=solo 1 decimal
    "promedio": round(promedio, 1)
}
print (dic)