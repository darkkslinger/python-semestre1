#DATOS DE TIPO NUMERICO
estatura = 1.71 #reales
edad = 29 #Entero
peso = 70 #reales
complejo =  1 +4j #Complejo, se pone j para los complejos
print("Impresion del numero complejo" ,complejo)
print(f"Mi estatura es de {estatura}")
# Operacion aritmetica basica para saar el imc
imc = peso/estatura**2
print("Mi IMC es de:",imc)

#El codigo {:.2f} es para aproximar y va entre comillas
print("Mi IMC es de: {:.2f}" .format (imc), "\n")
# Datos de tipo cadena de caracteres
asignatura= 'programación'
carrera= 'Ingenieria Civil en Informatica'
print('La asignatura de',asignatura, 'corresponde a la carrera de',carrera)
print('la asignatura de' , len (asignatura) , 'corresponde a la carrera de' , len (carrera))

#Funciones propias de python
#str() , int() , float() , len() , type()= String es para texto, len para enteros, float pra reales,
#y len uenta los caracteres, por ejemplo: "Hola"= 4

# Valores booleanos
ampolleta=False
interruptor=True


# Con type sabemos el tipo de datos que estamos tratando
print(type(ampolleta))

ampolleta='soy ampolleta'
print(type(ampolleta))

estudiantes= ['Matias', 'Marco', 'Cristobal', 'Sebastian']
num=[1 , 2 , 3 , 4 , 5 , 6]
lenguaje= ["Python"]
data=["Osorno", { "UV" : "nivel bajo", "Temp °C" :15}, ( -40.5725, -70.432 )]
print(data)
print(len(data))
print("lista de cadena de caracteres:",estudiantes)
print("lista de numeros:",num)
print("lista de elementos:",lenguaje)
#Con .count() podemos buscar un elemento dentro de una lista y nos muestra donde esta.
print(estudiantes.count("Matias"))

#Datos tipo array (objetos de tipo coleccion) o arreglos. Con array se gasta menos memoria que con list() pero con list() es mas dinamico
#y array es mas limitado a un tipo de dato.
nueva_lista = list()
print("Esta es una nueva lista vaia", nueva_lista)
#los corchetes [] se utilizan para crear una lista
#que es una oleccion ordenada, los elementos de la losta estan separados por comas