from composite import Composite


class SectorCajas(Composite):
    def __init__(self,cajero={}):
        super().__init__()
        self._cantidadCajeros=cajero

    def getSueldo(self):
        return super().getSueldo()

    def agregar(self, p=...):
        return super().agregar(p=p)

    @property
    def cantidadCajeros(self):
        return self._cantidadCajeros

    @cantidadCajeros.setter
    def setCantidadCajeros(self,cajero):
        self._cantidadCajeros=cajero