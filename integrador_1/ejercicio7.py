class Cuenta:
    def __init__(self, titular="", cantidad=0): # constructor con parámetros
        self._titular = titular
        self._cantidad = cantidad
    
    # getters y setters
    def get_titular(self):
        return self._titular    
    
    def get_cantidad(self):
        return self._cantidad
    
    # mostrar los datos de la cuenta
    def mostrar(self):
        print(f"Titular: {self._titular}")
        print(f"Dinero en cuenta: ${self._cantidad}")
    
    # ingresar una cantidad a la cuenta
    def ingresar(self, titular, cantidad):
        # setter dentro de la función ingresar, porque sólo se puede modificar ingresando o retirando dinero
        def set_titular(titular): 
            self._titular = titular      
        def set_cantidad(cantidad):
            self._cantidad += cantidad
        self.set_titular = set_titular(titular)
        self.set_cantidad = set_cantidad(cantidad)
        print(f"Ingresó ${cantidad} a su cuenta.")
       
    # retirar una cantidad de la cuenta
    def retirar(self, titular, cantidad):
        # setter dentro de la función retirar, porque sólo se puede modificar ingresando o retirando dinero
        def set_titular(titular):
            self._titular = titular
        def set_cantidad(cantidad):
            self._cantidad -= cantidad
        self.set_titular = set_titular(titular)
        self.set_cantidad = set_cantidad(cantidad)
        print(f"Retiró ${cantidad} de su cuenta.")
    
    # método string
    def __str__(self):
        return f"Titular: {self._titular}. Dinero en cuenta ${self._cantidad}."

cuenta = Cuenta()
cuenta.ingresar("Florencia", 20)
cuenta.mostrar()
cuenta.retirar("Florencia", 10)
cuenta.mostrar()