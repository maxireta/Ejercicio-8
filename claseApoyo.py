from clasePersonal import personal

class apoyo(personal):
    def __init__(self, cuil, apellido, nombre, sueldo, antiguedad, categoria):
        super().__init__(cuil, apellido, nombre, sueldo, antiguedad)
        self.__categoria = categoria
    def __str__(self):
        return f"Apoyo: {super().getApellido()} {super().getNombre()}, Categoria: {self.__categoria}"
    def getCuil(self):
        return super().getCuil()
    def setSueldo(self, nuevo):
        super().setSueldo(nuevo)
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
            "categoria": self.__categoria
        }