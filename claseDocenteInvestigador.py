from claseInvestigador import investigador
from claseDocente import docente

class docenteinvestigador(docente, investigador):
    def __init__(self, cuil, apellido, nombre, sueldo, antiguedad, area, tipo, carrera, cargo, catedra, categoria, importe):
        #investigador.__init__(self, cuil, apellido, nombre, sueldo, antiguedad, area, tipo)
        #docente.__init__(self, cuil, apellido, nombre, sueldo, antiguedad, carrera, cargo, catedra)
        super().__init__(cuil, apellido, nombre, sueldo, antiguedad, carrera, cargo, catedra, area, tipo)
        self.__categoria = categoria
        self.__importe = importe
    def __str__(self):
        return f"Docente investigador: {super().getApellido()} {super().getNombre()}, Importe: {self.__importe}"
    def getCuil(self):
        return super().getCuil()
    def setSueldo(self, nuevo):
        super().setSueldo(nuevo)
    def setImporte(self, nuevo):
        self.__importe = nuevo
    def getNom(self):
        return super().getNom()
    def getArea(self):
        return super().getArea()
    def getApe(self):
        return super().getApe()
    def getSueldo(self):
        return super().getSueldo()
    def getImportextra(self):
        return self.__importe
    def getCate(self):
        return self.__categoria
    def dic(self):
        return {
            "cuil": super().getCuil(),
            "apellido": super().getApellido(),
            "nombre": super().getNombre(),
            "sueldo": super().getSueldo(),
            "antiguedad": super().getAntiguedad(),
            "carrera": super().getCarrera(),
            "cargo": super().getCargo(),
            "catedra": super().getCatedra(),
            "area": super().getArea(),
            "tipo": super().getTipo(),
            "categoria": self.__categoria,
            "importe_extra": self.__importe
        }