pacientes = []
for i in range (3):
    print("Ingresando datos del paciente", i+1)
    nombre = input("Nombre: ")
    peso = float(input("Peso (kg): "))
    estatura = float(input("Estatura (metros): "))

    while True:
        try:
            edad = int(input("Edad: "))
            if edad > 0:
                break
            else:
                print("Error: La edad debe ser un número positivo.")
        except ValueError:
            print("Error: La edad debe ser un número entero.")

    paciente = (nombre, peso, estatura, edad)
    pacientes.append(paciente)
print ("\n","\n")

print("Datos de los pacientes:","\n")

# paciente=tupla pacientes=lista
for paciente in pacientes:
    nombre, peso, estatura, edad = paciente
    print("Nombre:", nombre)
    print("Peso:", peso, "kg")
    print("Estatura:", estatura, "metros")
    print("Edad:", edad)
    print("-" * 20)
