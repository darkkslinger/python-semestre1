#DATOS DE TIPO NUMERICO
estatura = 1.71 #reales
edad = 29 #Entero
peso = 70 #reales
complejo =  1 +4j #Complejo

print(f"Mi estatura es de {estatura} y mi peso es de {peso}")
print("Impresion de un numero complejo" ,complejo, "/n")

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

estudiantes = ["Matias", "Marco", "Cristobal", "Sebastián", "Marco"]
num = [1,2,3,4,5,6,1]             
lenguaje = list(["Python","Dart"])

# ¿Se puede realizar una lista de datos compuestos?
data = ['Osorno', {'UV': 'nivel bajo', 'Temp °C': 15}, (-40.5725, -73.1353)]
listamixta = ['Felipe', 100, True]

print("Lista de cadena de caracteres:",estudiantes)
print("Lista de números:",num)
print("Lista de un elemento:",lenguaje)
print("Esta es una lista mixta:", listamixta)
print("Esto igual es una lista:",data)
print(len(listamixta)) #para saber la cantidad de elementos de una lista
print(estudiantes.count("Marco"))   
print(num.count(5000))  #cantidad de ocurrencias de un elemento en especifico dentro de la lista

lenguaje = ["JavaScript"]
print("Nuevo valor del Arreglo de un elemento:",lenguaje)

#¿Como accedo a un elemento especifico de la lista?
print(estudiantes[0]) #correcto (1° elemento de la lista)
print(estudiantes[1]) #(2° elemento de la lista)
#print(estudiantes[6]) #incorrecto
print("Posicion -2 de la lista estudiantes:",estudiantes[-2]) #impresión desde atras hacia adelante

#Reasignando el valor de la 3° posicion de la lista
estudiantes[3] = "Gabriela"
print("El nuevo arreglo de estudiantes es:",estudiantes)

#Inicializando otra lista de datos mixtos
data_asig = [10023,"Programación",1,True]

#¿Que hace este código?    #Desempaquetando elementos de la lista (data_asig) a variables
cod,ramo,semestre,estado = data_asig
print(ramo)

#¿Se pueden sumar listas?
print("Suma de listas:",estudiantes + num)

#¿Qué hacen estas funciones?
print(list("Python"))
print(list(range(10))) #genera una lista 10 elementos
print("\n")

# > En el fichero de listas se mostrarán más funciones 

#05 - TUPLAS - (No mutables)
newtupla = tuple()                     
grupo1 = ("Daniel","Cristian","Felipe",200,100,"Daniel")
print("######## 05-TUPLAS ########")
print(type(grupo1))

#Accediendo al primer elemento de la tupla
print(grupo1[0])

#Consultando el elemento "Daniel" cuantas veces se encuentra en la tupla
print("El elemento se repite:",grupo1.count("Daniel"))

#Muestra el indice del primer elemento buscado
print("Indice del elemento:",grupo1.index ("Daniel"))

#Reasignando el primer elemento de la tupla
"""grupo1[0] = "Constanza"
print(grupo1)"""

#¿Se pueden sumar las tuplas?


#Obteniendo un trozo de la tupla
grupo2 = ("Pedro",100,"Felipe","Diego",2020,"Alejandra")
print("Trozo de la tupla",grupo2[0:3])

#¿Entonces como no puedo modificar una tupla, que puedo hacer?
grupo1 = list(grupo1)
print("La tupla ahora es de tipo:",type(grupo1),"\n")
print("\n")

#06 - SETS (Conjuntos) -  Estructura fija
#Formas de inicializar un Set
print("######## 06-SETS ########")
conjunto_vacio = set()           
conjunto_vacio1 = {}  #¿diccionario o set?
print(type(conjunto_vacio1))
conjunto_colores = set({"Azul","Rojo","Verde"}) #utilizando la funcion set
conjunto_animales = {"Gato","Perro","Loro"}     #utilizando llaves

print(type(conjunto_colores)) #tipo de dato set
print(type(conjunto_animales)) #tipo de dato set
print("El primer set contiene los siguientes colores:",conjunto_colores)
print("El segundo set contiene los siguientes animales:",conjunto_animales)

#print(conjunto_animales[0]) #accediendo al primer elemento del set
conjunto_colores.add("Celeste")
print("El set de colores lo conforman:",conjunto_colores)  #un set es una estructura desordenada a diferencia de una Lista

#conjunto_animales.add("Gato")
print("El set de animales lo conforman:",conjunto_animales,"\n") #un set no acepta duplicados, a diferencia de las listas que si.


#07 - DICCIONARIOS (Clave-Valor)
print("######## 06-DICCIONARIOS ########")

diccionario1 = dict()
diccionario2 = {}

datos_personales = {
    "Nombre":"Victor",
    "Institucion":"Ulagos",
    "Edad":29
    }

print(datos_personales)

datos_personales = {
    "Nombre":"Victor",
    "Institucion":"Ulagos",
    "Edad": 29,
    "Asignaturas": {"Estructura de Datos", "Programación"}
    }

print("Diccionario inicial:",datos_personales)

#Consulta la cantidad de elementos del Diccionario
print(len(datos_personales))

#Es facilmente accesible a los elementos dentro de un diccionario
print(datos_personales["Institucion"])

#¿Como actualizamos el valor de una clave dentro de un diccionario?
datos_personales["Institucion"] = "USS" 
print("Diccionario actualizado:",datos_personales)

#Agregando un nuevo clave al diccionario
datos_personales["Ciudad"] = "Osorno"
print(datos_personales)
print("Diccionario con el nuevo campo:",datos_personales)

#Eliminando un campo del diccionario
del datos_personales["Ciudad"]
print("Diccionario con el campo eliminado:",datos_personales)

hospital = dict(
    nombre = "Hospital San Jose",
    direccion = "Dr. Guillermo Buhler 1765",
    ciudad = "Osorno"
)