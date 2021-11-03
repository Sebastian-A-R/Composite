from composite import Composite


class SectorAdministrativo(Composite):
    def __init__(self,admin={}):
        super().__init__()
        self._cantidadAdmin=admin

    def getSueldo(self):
        return super().getSueldo()

    def agregar(self, p=...):
        return super().agregar(p=p)

    @property
    def cantidadAdmin(self):
        return self._cantidadAdmin

    @cantidadAdmin.setter
    def setCantidadAdmin(self,admin):
        self._cantidadAdmin=admin