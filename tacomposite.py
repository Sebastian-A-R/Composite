from banco import Banco
from empleado import Empleado
from sectoradministrativo import SectorAdministrativo
from sectorcajas import SectorCajas
from sectorcontaduria import SectorContaduria
from sectorgerencia import SectorGerencia
from sectorrrhh import SectorRRHH


if __name__ == "__main__":

    banco = Banco()

    administracion = SectorAdministrativo()
    cajas = SectorCajas()
    contaduria = SectorContaduria()
    gerencia = SectorGerencia()
    rrhh = SectorRRHH()

    banco.agregar(administracion)
    banco.agregar(cajas)
    banco.agregar(contaduria)
    banco.agregar(gerencia)
    banco.agregar(rrhh)

    cajero1 = Empleado("Naafer Salas","Cajero",300)
    cajero2 = Empleado("Diana Roa","Cajero",300)
    cajas.agregar(cajero1)
    cajas.agregar(cajero2)

    gerente = Empleado("Alvaro Molina","Gerente",500)
    gerencia.agregar(gerente)

    selector = Empleado("Pedro Cañas","RRHH",350)
    rrhh.agregar(selector)

    contador=Empleado("Monica Ardila","Contador",380)
    contaduria.agregar(contador)

    print(banco.getSueldo())