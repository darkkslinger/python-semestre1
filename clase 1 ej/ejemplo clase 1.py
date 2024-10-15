class Auto:
    # Abstracción de los objetos auto
    def __init__(self, gasolina):
        self.gasolina = gasolina
        print(f"Tenemos {self.gasolina} litros de gasolina")

    def arrancar(self):
        if self.gasolina > 0:
            print("Arranca")
        else:
            print ("No arranca")

    def conducir(self, consumo):
        if self.gasolina > consumo:
            self.gasolina -= consumo
            print(f"Quedan {self.gasolina} litros")
        else :
            print ("No se mueve")

# Ejemplo de uso
auto = Auto(10)  # Inicializa un auto con 10 litros de gasolina
auto.arrancar()   # Intenta arrancar
auto.conducir(3)  # Consume 3 litros de gasolina
auto.conducir(8)  # Intenta consumir más gasolina de la que hay 