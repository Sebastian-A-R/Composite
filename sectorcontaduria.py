from composite import Composite


class SectorContaduria(Composite):
    def __init__(self,conta={}):
        super().__init__()
        self._cantidadContaduria=conta

    def getSueldo(self):
        return super().getSueldo()

    def agregar(self, p=...):
        return super().agregar(p=p)

    @property
    def cantidadContaduria(self):
        return self._cantidadContaduria

    @cantidadContaduria.setter
    def setCantidadContaduria(self,conta):
        self._cantidadContaduria=conta