class Cuenta:
    def __init__(self): # constructor vacío
        self._titular = ""
        self._cantidad = 0

    #def __init__(self, titular, cantidad=0): # constructor con parámetros
    #    self._titular = titular
    #    self._cantidad = cantidad
    
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
    def ingresar(titular, cantidad):
        # setter dentro de la función ingresar, porque sólo se puede modificar ingresando o retirando dinero
        def set_titular(self, titular): 
            self._titular = titular      
        def set_cantidad(self, cantidad):
            self._cantidad += cantidad
        set_titular(titular)
        set_cantidad(cantidad)
        print(f"Ingresó ${cantidad} a su cuenta.")
       
    # retirar una cantidad de la cuenta
    def retirar(titular, cantidad):
        # setter dentro de la función retirar, porque sólo se puede modificar ingresando o retirando dinero
        def set_titular(self, titular):
            self._titular = titular
        def set_cantidad(self, cantidad):
            self._cantidad -= cantidad
        set_titular(titular)
        set_cantidad(cantidad)
        print(f"Retiró ${cantidad} de su cuenta.")
    
    # método string
    def __str__(self):
        return f"Titular: {self._titular}. Dinero en cuenta ${self._cantidad}."

Cuenta()
Cuenta.get_titular
Cuenta.get_cantidad
Cuenta.ingresar("Florencia", 20)
Cuenta.mostrar
Cuenta.retirar("Florencia", 10)
Cuenta.mostrar