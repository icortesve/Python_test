class Usuario:
    def __init__(self, nombre, apellido, email):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.limite_credito = 30000
        self.saldo_pagar = 0
  
    def hacer_compra(self, monto):  #recibe como argumento el monto de la compra
        self.saldo_pagar += monto   #el saldo a pagar del usuario aumenta en la cantidad del valor recibido
        return self

# pagar_tarjeta(self, monto): crea un método que pague un monto de la tarjeta de crédito. haciendo que se reduzca el saldo_pagar.
    def pagar_tarjeta(self, monto):
        self.saldo_pagar -= monto
        if self.saldo_pagar < 0:
            self.saldo_pagar = 0
        return self

# mostrar_saldo_usuario(self): crea un método que imprima el nombre completo del usuario y el saldo a pagar de su tarjeta.Ejemplo: “Usuario: Nariyoshi Miyagi, Saldo a Pagar: $50”
    def mostrar_saldo_usuario(self):
        print(f"Usuario:{self.nombre} {self.apellido}, Saldo a pagar: ${self.saldo_pagar}")
        return self

# BONUS: transferir_deuda(self, otro_usuario, monto): crea un método que reduzca la deuda (saldo_pagar) del usuario por el monto, y agrega esa cantidad al saldo_pagar de otro_usuario
    def transferir_deuda(self, otro_usuario, monto):
        if self.saldo_pagar >= monto:
            self.saldo_pagar -= monto
            otro_usuario.saldo_pagar += monto
        else:
            print("No hay suficiente deuda para transferir")
        return self

# Crea el archivo un Python con la clase Usuario, con la base que te proporcionamos
# Agrega el método pagar_tarjeta a la clase Usuario
# Agrega el método mostrar_saldo_usuario a la clase Usuario
# Crea 3 instancias de la clase Usuario

Usuario1 = Usuario("Michael", "Jackson", "mjackson@neverland.com")
Usuario2 = Usuario("Jam", "Iroquai", "jamiroquai@music.net")
Usuario3 = Usuario("Mercedes", "Sosa", "msosa@tucuman.gov.ar")

# Haz que el primer usuario haga 2 compras y luego pague su tarjeta. Muestra su saldo

Usuario1.hacer_compra(800) #Primera compra
Usuario1.hacer_compra(600) #Segunda compra
Usuario1.pagar_tarjeta(200) #Pago
Usuario1.mostrar_saldo_usuario() #Mostrar saldo

##Encadenamiento:
Usuario1.hacer_compra(800).hacer_compra(600).pagar_tarjeta(200).mostrar_saldo_usuario()


# Haz que el segundo usuario haga 1 compra y luego pague 2 veces su tarjeta. Muestra su saldo

Usuario2.hacer_compra(500) #Primera compra
Usuario2.pagar_tarjeta(100) #Primer pago
Usuario2.pagar_tarjeta(200) #Segundo pago
Usuario2.mostrar_saldo_usuario() #Mostrar saldo

##Encadenamiento:
Usuario2.hacer_compra(500).pagar_tarjeta(100).pagar_tarjeta(200).mostrar_saldo_usuario()

# Haz que el tercer usuario haga 3 compras y luego pague su tarjeta 4 veces. Muestra su saldo

Usuario3.hacer_compra(800) #Primera compra
Usuario3.hacer_compra(700) #Segunda compra
Usuario3.hacer_compra(500) #Tercera compra
Usuario3.pagar_tarjeta(600) #Primer pago
Usuario3.pagar_tarjeta(50) #Segundo pago
Usuario3.pagar_tarjeta(80) #Tercer pago
Usuario3.pagar_tarjeta(100) #Cuarto pago
Usuario3.mostrar_saldo_usuario() #Mostrar saldo

##Encadenamiento:
Usuario3.hacer_compra(800).hacer_compra(700).hacer_compra(500).pagar_tarjeta(600).pagar_tarjeta(50).pagar_tarjeta(80).pagar_tarjeta(100).mostrar_saldo_usuario()
