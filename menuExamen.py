from examenCorvalan import *
#8 menu

def menu():
    while True:
        print('''\nMenú de opciones:
        1 - (Ya cargados) Carga de datos
        2 - Mostrar todos los datos
        3 - Calcular promedios
        4 - Ordenar por promedio DESC
        5 - Mostrar materia con mayor promedio
        6 - Buscar estudiante por legajo"
        7 - Contar calificaciones en una materia
        8 - Salir''')

        opcion = int(input("Ingrese una opción: "))

        match opcion:
            case 1:
                print("DATOS CARGADOS")
            case 2:
                mostrar_todos_estudiantes()
            case 3:
                calcular_promedios()
            case 4:
                ordenar_descendiente()
            case 5:
                mejor_promedio()
            case 6:
                legajo = int(input("Ingrese legajo a buscar: "))
                buscar_legajo(legajo)
            case 7:
                materia = int(input("Ingrese número de materia (1 a 5): "))
                if 1 <= materia <= 5:
                    repeticion_calificacion(materia)
                else:
                    print("Número de materia inválido.")
            case 8:
                print("Saliendo del programa")
                break
            case _:
                print("Numero Invalido")

menu()