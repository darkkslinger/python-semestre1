#DATOS DE TIPO NUMERICO
estatura = 1.71
peso = 70
complejo =  1 +4j
print("Impresion del numero complejo" ,complejo)

# Operacion aritmetica basica
imc = peso/estatura**2
print("Mi IMC es de:",imc)

# Datos de tipo cadena de caracteres
asignatura= 'programación'
carrera= 'Ingenieria Civil en Informatica'
print('La asignatura de',asignatura, 'corresponde a la carrera de',carrera)


# Valores booleanos
ampolleta=False
interruptor=True


# Con type sabemos el tipo de datos que estamos tratando
print(type(ampolleta))

ampolleta='soy ampolleta'
print(type(ampolleta))
#Datos tipo array (objetos de tipo coleccion)
estudiantes = {'Matias', 'Marco', 'Cristobal', 'Sebastian'}
num=(estudiantes)
print(num)