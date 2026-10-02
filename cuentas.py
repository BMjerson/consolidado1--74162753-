class CuentaBancaria:
    def __init__(self, numero_cuenta: str, titular: str):
        self.numero_cuenta = numero_cuenta
        self.titular = titular
        self._saldo = 0.0

    def depositar(self, monto: float):
        if monto <= 0:
            raise ValueError("El monto a depositar debe ser mayor a 0.")
        self._saldo += monto

    def retirar(self, monto: float):
        if monto <= 0:
            raise ValueError("El monto a retirar debe ser mayor a 0.")
        if monto > self._saldo:
            raise ValueError("Saldo insuficiente.")
        self._saldo -= monto

    def consultar_saldo(self):
        return self._saldo

    def __str__(self):
        return f"Cuenta: {self.numero_cuenta} | Titular: {self.titular} | Saldo: S/{self._saldo:.2f}"

class CuentaAhorros(CuentaBancaria):
    def __init__(self, numero_cuenta: str, titular: str, tasa_interes: float):
        super().__init__(numero_cuenta, titular)
        self.tasa_interes = tasa_interes

    def calcular_interes(self):
        return self._saldo * (self.tasa_interes / 100)

    def __str__(self):
        return super().__str__() + f" | Tasa: {self.tasa_interes}% | Interés anual: S/{self.calcular_interes():.2f}"

class CuentaCorriente(CuentaBancaria):
    def __init__(self, numero_cuenta: str, titular: str, limite_sobregiro: float):
        super().__init__(numero_cuenta, titular)
        self.limite_sobregiro = limite_sobregiro

    def retirar(self, monto: float):
        if monto <= 0:
            raise ValueError("El monto a retirar debe ser mayor a 0.")
        if monto > (self._saldo + self.limite_sobregiro):
            raise ValueError("Excede el límite de sobregiro permitido.")
        self._saldo -= monto

    def permite_sobregiro(self):
        return self._saldo < 0

    def __str__(self):
        return super().__str__() + f" | Límite Sobregiro: S/{self.limite_sobregiro:.2f}"

if __name__ == "__main__":
    print("--- PRUEBA CUENTA AHORROS ---")
    ahorros = CuentaAhorros("AH-001", "Juan Perez", 4.5)
    ahorros.depositar(1000)
    ahorros.retirar(200)
    print(ahorros)

    print("\n--- PRUEBA CUENTA CORRIENTE ---")
    corriente = CuentaCorriente("CC-001", "Maria Lopez", 500.0)
    corriente.depositar(500)
    corriente.retirar(800)
    print(corriente)
    print(f"¿Está en sobregiro? {corriente.permite_sobregiro()}")