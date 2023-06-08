from claseLista import lista

if __name__ == '__main__':
    guardar = lista()
    guardar.cargar()

    print("Menú")
    print("1. Insertar agentes.")
    print("2. Agregar agentes.")
    print("3. Mostrar una posición.")
    print("4. Mostrar docentes investigadores ordenado.")
    print("5. Contar investigadores y docentes investigadores.")
    print("6. Mostrar todos los agentes.")
    print("7. Mostrar docentes investigadores de una categoria.")
    print("8. Almacenar datos.")
    guardar.mostrartodo()
    opcion = input("Elija una opción: ")
    if opcion == '1':
        guardar.opcion1()
    elif opcion == '2':
        guardar.opcion2()
    elif opcion == '3':
        guardar.opcion3()
    elif opcion == '4':
        car = input("Ingrese una carrera: ")
        guardar.opcion4(car)
    elif opcion == '5':
        are = input("Ingrese un area: ")
        guardar.opcion5(are)
    elif opcion == '6':
        guardar.opcion6()
    elif opcion == '7':
        cate = input("Ingrese una categoria: ")
        guardar.opcion7(cate)
    elif opcion == '8':
        guardar.opcion8()
    elif opcion == '9':
        usuario = input("Ingrese el nombre de usuario: ")
        contraseña = input("Ingrese la contraseña: ")
        if usuario == 'uTesorero' and contraseña == 'ag@74ck':
            guardar.tesorero()
        elif usuario == 'uDirector' and contraseña == 'ufC77#!1':
            guardar.director()
        else:
            print("Usuario o contraseña incorrectos.")