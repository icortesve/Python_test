class Usuario:
    def __init__(self, nombre, apellido, email):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.limite_credito = 30000
        self.saldo_pagar = 0
  
    def hacer_compra(self, monto):  #recibe como argumento el monto de la compra
        self.saldo_pagar += monto   #el saldo a pagar del usuario aumenta en la cantidad del valor recibido

# pagar_tarjeta(self, monto): crea un método que pague un monto de la
    def pagar_tarjeta(self, monto):
        self.saldo_pagar -= monto


# mostrar_saldo_usuario(self): crea un método que imprima el nombre completo del usuario y el saldo a pagar de su tarjeta.Ejemplo: “Usuario: Nariyoshi Miyagi, Saldo a Pagar: $50”
    def mostrar_saldo_usuario(self):
        return print(self.nombre, self.apellido, ", Saldo a pagar: $"self.saldo_pagar)

# BONUS: transferir_deuda(self, otro_usuario, monto): crea un método que reduzca la deuda (saldo_pagar) del usuario por el monto, y agrega esa cantidad al saldo_pagar de otro_usuario
    def transferir_deuda(self, otro_usuario, monto):
        return print(self.nombre, self.apellido, ", Saldo a pagar: $"self.saldo_pagar
        )

# Crea el archivo un Python con la clase Usuario, con la base que te proporcionamos
# Agrega el método pagar_tarjeta a la clase Usuario
# Agrega el método mostrar_saldo_usuario a la clase Usuario
# Crea 3 instancias de la clase Usuario

Usuario1 = Usuario("Michael", "Jackson", "mjackson@neverlan.com")
Usuario2 = Usuario("Jam", "Iroquai", "jamiroquai@music.net")
Usuario3 = Usuario("Mercedes", "Sosa", "msosa@tucuman.gov.ar")

# Haz que el primer usuario haga 2 compras y luego pague su tarjeta. Muestra su saldo

Usuario1.hacer_compra(800)
Usuario1.hacer_compra(600)
Usuario1.pagar_tarjeta(Usuario1.saldo_pagar())
print(Usuario1.mostrar_saldo_usuario())

# Haz que el segundo usuario haga 1 compra y luego pague 2 veces su tarjeta. Muestra su saldo

Usuario2.hacer_compra(800)
Usuario2.pagar_tarjeta(600)
Usuario2.pagar_tarjeta(Usuario2.saldo_pagar())
print(Usuario2.mostrar_saldo_usuario())

# Haz que el tercer usuario haga 3 compras y luego pague su tarjeta 4 veces. Muestra su saldo

Usuario3.hacer_compra(800)
Usuario3.hacer_compra(700)
Usuario3.hacer_compra(500)
Usuario3.pagar_tarjeta(600)
Usuario3.pagar_tarjeta(Usuario3.saldo_pagar())
Usuario3.pagar_tarjeta(Usuario3.saldo_pagar())
Usuario3.pagar_tarjeta(Usuario3.saldo_pagar())
Usuario3.pagar_tarjeta(Usuario3.saldo_pagar())
print(Usuario2.mostrar_saldo_usuario())