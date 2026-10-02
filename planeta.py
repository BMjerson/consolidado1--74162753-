class Planeta:
    def __init__(self, nombre: str, masa: float, radio: float, distancia_al_sol: float, tiene_vida: bool = False):
        self.nombre = nombre
        self.masa = masa
        self.radio = radio
        self.distancia_al_sol = distancia_al_sol
        self.tiene_vida = tiene_vida

import math

class Planeta:
    def __init__(self, nombre: str, masa: float, radio: float, distancia_al_sol: float, tiene_vida: bool = False):
        self.nombre = nombre
        self.masa = masa
        self.radio = radio
        self.distancia_al_sol = distancia_al_sol
        self.tiene_vida = tiene_vida

    def calcular_densidad(self):
        volumen = (4/3) * math.pi * (self.radio ** 3)
        return self.masa / volumen

    def es_planeta_exterior(self):
        return self.distancia_al_sol > 5.2

import math

class Planeta:
    def __init__(self, nombre: str, masa: float, radio: float, distancia_al_sol: float, tiene_vida: bool = False):
        self.nombre = nombre
        self.masa = masa
        self.radio = radio
        self.distancia_al_sol = distancia_al_sol
        self.tiene_vida = tiene_vida

    def calcular_densidad(self):
        volumen = (4/3) * math.pi * (self.radio ** 3)
        return self.masa / volumen

    def es_planeta_exterior(self):
        return self.distancia_al_sol > 5.2

    def __str__(self):
        tipo = "exterior" if self.es_planeta_exterior() else "interior"
        return f"Planeta: {self.nombre} | Densidad: {self.calcular_densidad():.2f} kg/m^3 | Tipo: {tipo}"

# Instancias de prueba
if __name__ == "__main__":
    tierra = Planeta("Tierra", 5.972e24, 6371000.0, 1.0, True)
    jupiter = Planeta("Júpiter", 1.898e27, 69911000.0, 5.203, False)

    print(tierra)
    print(jupiter)