from claseDocente import docente
from claseApoyo import apoyo
from claseInvestigador import investigador
from claseDocenteInvestigador import docenteinvestigador
from claseInterfaz import interfaz
from claseNodo import Nodo
from claseTesorero import ITesorero
from claseDirector import IDirector
import json

class lista(interfaz, ITesorero, IDirector):
    def __init__(self):
        self.__com = None
    def cargar(self):
        with open('personal.json') as archi:
            datos = json.load(archi)
        docentes = datos["docentes"]
        apoyos = datos["apoyo"]
        investigadores = datos["investigadores"]
        docentesinv = datos["docentes_investigadores"]
        
        for mos in docentes:
            self.creardocente(mos)
        for mos in apoyos:
            self.crearapoyo(mos)
        for mos in investigadores:
            self.crearinvestigador(mos)
        for mos in docentesinv:
            self.creardocenteinv(mos)
    def creardocente(self, mos):
        cuil = mos["cuil"]
        apellido = mos["apellido"]
        nombre = mos["nombre"]
        sueldo = float(mos["sueldo_basico"])
        antiguedad = mos["antiguedad"]
        carrera = mos["carrera"]
        cargo = mos["cargo"]
        catedra = mos["catedra"]
        doc = docente(cuil, apellido, nombre, sueldo, antiguedad, carrera, cargo, catedra)
        self.agregarElemento(doc)
    def crearapoyo(self, mos):
        cuil = mos["cuil"]
        apellido = mos["apellido"]
        nombre = mos["nombre"]
        sueldo = float(mos["sueldo_basico"])
        antiguedad = mos["antiguedad"]
        categoria = mos["categoria"]
        apo = apoyo(cuil, apellido, nombre, sueldo, antiguedad, categoria)
        self.agregarElemento(apo)
    def crearinvestigador(self, mos):
        cuil = mos["cuil"]
        apellido = mos["apellido"]
        nombre = mos["nombre"]
        sueldo = float(mos["sueldo_basico"])
        antiguedad = mos["antiguedad"]
        area = mos["area_investigacion"]
        tipo = mos["tipo_investigacion"]
        inv = investigador(cuil, apellido, nombre, sueldo, antiguedad, area, tipo)
        self.agregarElemento(inv)
    def creardocenteinv(self, mos):
        cuil = mos["cuil"]
        apellido = mos["apellido"]
        nombre = mos["nombre"]
        sueldo = float(mos["sueldo_basico"])
        antiguedad = mos["antiguedad"]
        carrera = mos["carrera"]
        cargo = mos["cargo"]
        catedra = mos["catedra"]
        area = mos["area_investigacion"]
        tipo = mos["tipo_investigacion"]
        categoria = mos["categoria"]
        importe = float(mos["importe_extra"])
        docinv = docenteinvestigador(cuil, apellido, nombre, sueldo, antiguedad, area, tipo, carrera, cargo, catedra, categoria, importe)
        self.agregarElemento(docinv)
    def creardinv(self):
        cuil = 123123123
        apellido = "Prueba"
        nombre = "Prueba"
        sueldo = float(20000)
        antiguedad = "Prueba"
        carrera = "Prueba"
        cargo = "Prueba"
        catedra = "Prueba"
        area = "Prueba"
        tipo = "Aplicada"
        categoria = "III"
        importe = float(20000)
        docinv = docenteinvestigador(cuil, apellido, nombre, sueldo, antiguedad, area, tipo, carrera, cargo, catedra, categoria, importe)
        return docinv
    def agregarElemento(self, elem):
        nodo = Nodo(elem)
        actual = self.__com
        if actual is None:
            actual = nodo
        else:
            while actual.getSig() is not None:
                actual = actual.getSig()
            actual.setSig(nodo)
    def insertarElemento(self, elem, pos):
        try:
            nodo = Nodo(elem)
            i = 1
            actual = self.__com
            while i < pos:
                i += 1
                ant = actual
                actual = actual.getSig()
            ant.setSig(nodo)
            nodo.setSig(actual)
        except IndexError:
            raise Exception("Posición inválida.")
    def mostrartodo(self):
        actual = self.__com
        while actual is not None:
            mos = actual.getPer()
            print(mos)
            actual = actual.getSig()
    def opcion1(self):
        inv = self.creardinv()
        pos = int(input("Ingrese una posición: "))
        pos -= 1
        self.insertarElemento(inv, pos)
    def opcion2(self):
        inv = self.creardinv()
        self.agregarElemento(inv)
    def opcion3(self):
        pos = int(input("Ingrese una posición: "))
        pos -= 1
        self.mostrarElemento(pos)
    def mostrarElemento(self, pos):
        try:
            i = 1
            actual = self.__com
            while i < pos:
                actual = actual.getSig()
                i += 1
            mos = actual.getPer()
            self.mostrar3(mos)
        except IndexError:
            raise Exception("Posición inválida.")
    def mostrar3(self, mos):
        if isinstance(mos, docente):
            print("Es agente docente.")
        elif isinstance(mos, apoyo):
            print("Es agente docente.")
        elif isinstance(mos, investigador):
            print("Es agente investigador.")
        else:
            print("Es agente docente investigador.")
    def opcion4(self, carr):
        fua = []
        actual = self.__com
        while actual is not None:
            mos = actual.getPer()
            if isinstance(mos, docente) or isinstance(mos, docenteinvestigador):
                fua.append(mos)
            actual = actual.getSig()
        fua2 = sorted(fua, key= lambda x: x.getNom())
        self.mostrarlista(fua2)
    def mostrarlista(self, fua):
        for mos in fua:
            print(f"Nombre: {mos.getNom()}")
    def opcion5(self, are):
        print(f"Area: {are}")
        di = 0
        i = 0
        actual = self.__com
        while actual is not None:
            mos = actual.getPer()
            if isinstance(mos, investigador):
                i += 1
            elif isinstance(mos, docenteinvestigador):
                di += 1
            actual = actual.getSig()
        self.mostrar5(di, i)
    def mostrar5(self, di, i):
        print(f"Hay {di} docentes investigadores trabajando en el area.")
        print(f"Hay {i} investigadores trabajando en el area.")
    def opcion6(self):
        fua = []
        actual = self.__com
        while actual is not None:
            mos = actual.getPer()
            fua.append(mos)
            actual = actual.getSig()
        fuaor = sorted(fua, key= lambda x: x.getApe())
        self.mostrar6(fuaor)
    def mostrar6(self, fua):
        for mos in fua:
            if isinstance(mos, docente):
                print(f"Apellido y nombre: {mos.getApe()} {mos.getNom()}, Agente: Docente, Sueldo: {mos.getSueldo()}")
            elif isinstance(mos, apoyo):
                print(f"Apellido y nombre: {mos.getApe()} {mos.getNom()}, Agente: Apoyo, Sueldo: {mos.getSueldo()}")
            elif isinstance(mos, investigador):
                print(f"Apellido y nombre: {mos.getApe()} {mos.getNom()}, Agente: Investigador, Sueldo: {mos.getSueldo()}")
            else:
                print(f"Apellido y nombre: {mos.getApe()} {mos.getNom()}, Agente: Docente Investigador, Sueldo: {mos.getSueldo()}")
    def opcion7(self, cate):
        importetotal = 0
        actual = self.__com
        while actual is not None:
            mos = actual.getPer()
            if isinstance(mos, docenteinvestigador):
                if mos.getCate() == cate:
                    importextra = mos.getImportextra()
                    print(f"Apellido y nombre: {mos.getApe()} {mos.getNom()}, Importe extra: {importextra}")
                    importetotal += importextra
    def opcion8(self):
        datos = self.hacerlista()
        with open('personal2.json', "w") as archi:
            json.dump(datos, archi, indent=4)
        print("Datos guardados correctamente.")
    def hacerlista(self):
        listar = []
        actual = self.__com
        while actual is not None:
            mos = actual.getPer()
            listar.append(mos.dic())
            actual = actual.getSig()
        return listar
    def tesorero(self):
        dni = input("Ingrese un dni: ")
        self.gastosSueldoPorEmpleado(dni)
    def gastosSueldoPorEmpleado(self, dni):
        actual = self.__com
        band = False
        while actual is not None and band is False:
            mos = actual.getPer()
            if mos.getCuil() == dni:
                band = True
            else:
                actual = actual.getSig()
        print(f"Sueldo: {mos.getSueldo()}")
    def director(self):
        print("1. Modificar sueldo basico.")
        opcion = input("Ingrese una opcion.")
        if opcion == '1':
            dni = input("Ingrese un dni: ")
            sueldo = float(input("Ingrese el sueldo nuevo: "))
            self.modificarBasico(dni, sueldo)
    def modificarBasico(self, dni, nuevoBasico):
        actual = self.__com
        band = False
        while actual is not None and band is False:
            mos = actual.getPer()
            if mos.getCuil() == dni:
                band = True
            else:
                actual = actual.getSig()
        mos.setSueldo(nuevoBasico)
        actual.setPer(mos)
    def modificarPorcentajeporcargo(self, dni, nuevoPorcentaje):
        actual = self.__com
        band = False
        while actual is not None and band is False:
            mos = actual.getPer()
            if mos.getCuil() == dni:
                band = True
            else:
                actual = actual.getSig()
        mos.setSueldo(nuevoPorcentaje)
        actual.setPer(mos)
    def modificarPorcentajeporcategoría(self, dni, nuevoPorcentaje):
        actual = self.__com
        band = False
        while actual is not None and band is False:
            mos = actual.getPer()
            if mos.getCuil() == dni:
                band = True
            else:
                actual = actual.getSig()
        mos.setSueldo(nuevoPorcentaje)
        actual.setPer(mos)
    def modificarImporteExtra(self, dni, nuevoImporteExtra):
        actual = self.__com
        band = False
        while actual is not None and band is False:
            mos = actual.getPer()
            if mos.getCuil() == dni:
                band = True
            else:
                actual = actual.getSig()
        mos.setImporte(nuevoImporteExtra)
        actual.setPer(mos)