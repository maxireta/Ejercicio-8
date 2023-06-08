from clasePersonal import personal

class docente(personal):
    def __init__(self, cuil, apellido, nombre, sueldo, antiguedad, carrera, cargo, catedra, area = '', tipo = ''):
        super().__init__(cuil, apellido, nombre, sueldo, antiguedad, carrera, cargo, catedra, area, tipo)
        self.__car = carrera
        self.__cargo = cargo
        self.__catedra = catedra
    def __str__(self):
        return f"Docente: {super().getApellido()} {super().getNombre()}, Carrera: {self.__car}"
    def getCuil(self):
        return super().getCuil()
    def setSueldo(self, nuevo):
        super().setSueldo(nuevo)
    def getCarrera(self):
        return self.__car
    def getCargo(self):
        return self.__cargo
    def getCatedra(self):
        return self.__catedra
    def getNom(self):
        return super().getNombre()
    def getApe(self):
        return super().getApellido()
    def getSueldo(self):
        return super().getSueldo()
    def dic(self):
        return {
            "cuil": super().getCuil(),
            "apellido": super().getApellido(),
            "nombre": super().getNombre(),
            "sueldo": super().getSueldo(),
            "antiguedad": super().getAntiguedad(),
            "carrera": self.__car,
            "cargo": self.__cargo,
            "catedra": self.__catedra

        }