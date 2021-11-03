from composite import Composite


class SectorGerencia(Composite):
    def __init__(self,geren={}):
        super().__init__()
        self._cantidadGerencia=geren

    def getSueldo(self):
        return super().getSueldo()

    def agregar(self, p=...):
        return super().agregar(p=p)

    @property
    def cantidadGerencia(self):
        return self._cantidadGerencia

    @cantidadGerencia.setter
    def setCantidadGerencia(self,geren):
        self._cantidadGerencia=geren