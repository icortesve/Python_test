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


# Crear tarjetas
tarjeta1 = TarjetaCredito(1000, 0.02)
tarjeta2 = TarjetaCredito(2000, 0.03)
tarjeta3 = TarjetaCredito(500, 0.05)

# Tarjeta 1: 2 compras, 1 pago, interés y mostrar (encadenado)
tarjeta1.compra(200).compra(300).pago(100).cobrar_interes().mostrar_info_tarjeta()

# Tarjeta 2: 3 compras, 2 pagos, interés y mostrar
tarjeta2.compra(500).compra(400).compra(300).pago(200).pago(100).cobrar_interes().mostrar_info_tarjeta()

# Tarjeta 3: exceder límite
tarjeta3.compra(200).compra(200).compra(200).compra(200).compra(200).mostrar_info_tarjeta()

# BONUS
TarjetaCredito.mostrar_todas_las_tarjetas()