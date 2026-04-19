class TarjetaCredito:

    # lista para BONUS (guardar todas las tarjetas)
    tarjetas = []

    def __init__(self, limite_credito, intereses, saldo_pagar=0):
        self.saldo_pagar = saldo_pagar
        self.limite_credito = limite_credito
        self.intereses = intereses

        TarjetaCredito.tarjetas.append(self)

    def compra(self, monto):
        if self.saldo_pagar + monto > self.limite_credito:
            print("Tarjeta Rechazada, has alcanzado tu límite de crédito")
        else:
            self.saldo_pagar += monto
        return self

    def pago(self, monto):
        self.saldo_pagar -= monto
        return self

    def mostrar_info_tarjeta(self):
        print(f"Saldo a Pagar: ${self.saldo_pagar}")
        return self

    def cobrar_interes(self):
        self.saldo_pagar += self.saldo_pagar * self.intereses
        return self

    # BONUS
    @classmethod
    def mostrar_todas_las_tarjetas(cls):
        print("\n--- Todas las tarjetas ---")
        for i, tarjeta in enumerate(cls.tarjetas, start=1):
            print(f"Tarjeta {i}: Saldo = ${tarjeta.saldo_pagar}")