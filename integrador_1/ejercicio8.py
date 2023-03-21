from ejercicio7 import Cuenta

class CuentaJoven(Cuenta):
    def __init__(self, bonificacion, titular="", cantidad=0):
        super().__init__(titular, cantidad)
        self._bonificacion = bonificacion
        self._edad = 20

    def get_titular(self):
        return super.__getattribute__ 
    
    def get_cantidad(self):
        return super.__getattribute__
    
    def get_edad(self):
        return self._edad
    
    def set_edad(self, edad):
        self._edad = edad

    def get_bonificacion(self):
        return self._bonificacion

    def set_bonificacion(self, bonificacion):
        self._bonificacion = bonificacion
    
    def es_titular_valido(self):
        edad = self.get_edad()
        return edad >= 18 and edad < 25
    
    def ingresar(self, titular, cantidad):
        if self.es_titular_valido():
            super().ingresar(titular, cantidad)
       
    def retirar(self, titular, cantidad):
        if self.es_titular_valido():
            super().retirar(titular, cantidad)

    def mostrar(self):  
        return (f"Cuenta Joven, Bonificación: {self.get_bonificacion()}")
    

cuentaJ = CuentaJoven(20)
cuentaJ.es_titular_valido()
cuentaJ.ingresar("Pepita", 30)
cuentaJ.mostrar()
cuentaJ.retirar("Florencia", 10)
cuentaJ.mostrar()
# %%
