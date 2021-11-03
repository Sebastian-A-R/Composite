from composite import Composite


class SectorRRHH(Composite):
    def __init__(self,recu={}):
        super().__init__()
        self._cantidadRRHH=recu

    def getSueldo(self):
        return super().getSueldo()

    def agregar(self, p=...):
        return super().agregar(p=p)

    @property
    def cantidadRRHH(self):
        return self._cantidadRRHH

    @cantidadRRHH.setter
    def setCantidadRRHH(self,recu):
        self._cantidadRRHH=recu