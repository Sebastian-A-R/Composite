

from isueldo import ISueldo


class Composite(ISueldo):
    def __init__(self):
        self._empleado=[]

    def getSueldo(self):
        sumador=0
        for i in range(len(self._empleado)):
            sumador=sumador+self._empleado[i].getSueldo()
        return sumador

    def agregar(self,p={}):
        self._empleado.append(p)
