class Automovil:
    def __init__(self, marca: str, modelo: str, velocidad_max: float, nivel_combustible: float, año_fabricacion: int):
        self.marca = marca
        self.modelo = modelo
        self.velocidad_max = velocidad_max
        self.nivel_combustible = nivel_combustible
        self.año_fabricacion = año_fabricacion

    @property
    def año_fabricacion(self):
        return self.__año_fabricacion

    @año_fabricacion.setter
    def año_fabricacion(self, valor: int):
        if not (1886 <= valor <= 2026):
            raise ValueError("El año de fabricación debe estar entre 1886 y 2026.")
        self.__año_fabricacion = valor

    @property
    def nivel_combustible(self):
        return self.__nivel_combustible

    @nivel_combustible.setter
    def nivel_combustible(self, valor: float):
        if not (0.0 <= valor <= 100.0):
            raise ValueError("El nivel de combustible debe estar entre 0.0 y 100.0.")
        self.__nivel_combustible = valor

    @property
    def velocidad_max(self):
        return self.__velocidad_max

    @velocidad_max.setter
    def velocidad_max(self, valor: float):
        if valor <= 0:
            raise ValueError("La velocidad máxima debe ser mayor a 0.")
        self.__velocidad_max = valor

    def tiempo_llegada(self, distancia_km: float):
        return distancia_km / self.velocidad_max

    def __str__(self):
        return f"Automóvil: {self.marca} {self.modelo} ({self.año_fabricacion}) | Vel. Máx: {self.velocidad_max} km/h | Combustible: {self.nivel_combustible}%"

if __name__ == "__main__":
    # Instancia correcta demostrando el método tiempo_llegada
    mi_auto = Automovil("Toyota", "Corolla", 180.0, 75.5, 2020)
    print(mi_auto)
    print(f"Tiempo estimado para 360 km: {mi_auto.tiempo_llegada(360.0):.2f} horas")

    # Prueba de validación con try/except (Año incorrecto)
    try:
        auto_error = Automovil("Ford", "Fiesta", 150.0, 50.0, 1800)
    except ValueError as e:
        print(f"Error de validación capturado: {e}")