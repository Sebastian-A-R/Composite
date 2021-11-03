from isueldo import ISueldo


class Empleado(ISueldo):
    def __init__(self,nombre,cargo,sueldo) -> None:
        super().__init__()
        self._nombre=nombre
        self._cargo=cargo
        self._sueldo=sueldo

      
    @property
    def sueldo(self):
        return self._sueldo

    @sueldo.setter
    def setSueldo(self,sueldo):
        self._sueldo=sueldo

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def setNombre(self,nombre):
        self._nombre=nombre
    
    @property
    def cargo(self):
        return self._cargo

    @cargo.setter
    def setCargo(self,cargo):
        self._cargo=cargo

    def getSueldo(self):
        return self._sueldo