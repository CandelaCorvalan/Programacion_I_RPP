'''
Para ello, se tienen los siguientes datos:
 Una matriz de números enteros de 30 filas por 5 columnas que corresponde a las calificaciones, donde:
o Cada fila representa un estudiante.
o Cada columna representa una materia.
o Cada valor en la intersección es una calificación entera entre 1 y 10.
 Una lista de nombre de los estudiantes.
 Una lista de géneros de los estudiantes. Cada género debe ser alguno de los siguientes: [‘F’ | ‘M’ | ‘X’]
 Una lista de legajos de los estudiantes. Cada legajo debe ser numérico del tipo entero de cinco cifras.
Cada una de estas listas, se corresponden con las filas de la matriz. Es decir, que se debe trabajar como listas
paralelas entre la matriz y las otras listas.
Se deberá programar un menú de opciones operado por consola, que realice lo siguiente:
1 – Realizar la carga de los datos en la matriz y en cada una de las listas. Realizar una función para validar cada
dato a ser cargado.
2 – Mostrar todos los datos, esto es la matriz completa de calificaciones conjuntamente con las listas de legajo,
género y nombre del estudiante. Realizar una función que muestre uno y otra que muestre todos.
3 – Calcular el promedio de cada estudiante y guardarlo en una nueva lista. Realizar una función que calcule el
promedio.
4 – Ordenar y mostrar los datos de los estudiantes por promedio de manera DESC. Realizar una función que
ordene, la cual deberá ordenar de manera ASC o DESC de acuerdo a un parámetro de ordenamiento.
5 – Mostrar la/s materia/s con mayor promedio general. Realizar una función para mostrar todas y otra para
mostrar una. Teniendo en cuenta que no hay una lista de materias, sino que cada columna de la matriz
representa una materia, entonces cada materia tomará la siguiente nomenclatura para su nombre MATERIA_
índice más uno. Por ejemplo: para la materia del índice cero de la columna, será MATERIA_1.
6 – Buscar y mostrar todos los datos de un estudiante por legajo, incluyendo el promedio calculado en el ítem 3.
Realizar una función de búsqueda. Realizar una función que muestre uno y otra que muestre todos.
7 – Buscar y mostrar cuantas veces se repite cada calificación en una asignatura determinada.
Realizar una función que reciba la matriz de calificaciones y el número de materia (índice más uno) como
parámetros, y retorne una lista de 10 elementos, donde en el índice 0 estará la cantidad de veces que se repite la
nota 1, en el índice 1 estará la cantidad de veces que se repite la nota 2, y así sucesivamente hasta el índice 9
donde estará la cantidad de veces que se repite la nota 10.
8 – Salir del programa.
'''
nombres = [
    "Ludmila", "Bruno", "Andy", "Diego", "Elena", "Facundo", "Micaela", "Hugo", "Isabel", "Joaquín",
    "Amelia", "Luis", "María", "Nicolás", "Olga", "Pablo", "Daniel", "Ramiro", "Sofía", "Tomás",
    "Uriel", "Valeria", "Mateo", "Valentina", "Ramon", "Zoe", "Alma", "Benjamín", "Clara", "Damián"
]

generos = [
    "F", "M", "X", "F", "M", "X", "F", "M", "X", "F",
    "M", "X", "F", "M", "X", "F", "M", "X", "F", "M",
    "X", "F", "M", "X", "F", "M", "X", "F", "M", "X"
]

legajos = [
    10000, 10001, 10002, 10003, 10004, 10005, 10006, 10007, 10008, 10009,
    10010, 10011, 10012, 10013, 10014, 10015, 10016, 10017, 10018, 10019,
    10020, 10021, 10022, 10023, 10024, 10025, 10026, 10027, 10028, 10029
]

calificaciones = [
    [5, 8, 10, 10, 2], [4, 6, 4, 7, 10], [7, 1, 9, 7, 10], [5, 4, 7, 4, 10], [7, 7, 8, 10, 10],
    [4, 9, 7, 6, 9], [10, 5, 8, 4, 6], [4, 4, 4, 9, 8], [4, 7, 9, 5, 7], [9, 4, 8, 5, 10],
    [7, 7, 8, 5, 6], [5, 9, 5, 10, 7], [6, 4, 7, 10, 8], [9, 4, 5, 9, 9], [10, 6, 4, 9, 6],
    [9, 9, 8, 7, 8], [10, 9, 5, 6, 6], [8, 3, 10, 8, 7], [8, 10, 4, 7, 5], [9, 10, 7, 7, 9],
    [5, 6, 8, 9, 10], [9, 9, 6, 4, 7], [9, 8, 4, 10, 5], [8, 10, 7, 6, 7], [9, 4, 7, 4, 6],
    [9, 10, 8, 8, 8], [7, 9, 5, 5, 8], [5, 4, 10, 5, 8], [10, 8, 5, 7, 8], [6, 10, 8, 6, 7]
]

promedios = [0] * 30
#1 

def mostrar_matriz(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(matriz[i][j], end = " ")
        print("")

def inicializar_matriz(cantidad_filas:int, cantidad_columnas:int, valor_inicial: any) -> list:
    matriz_estudiantes = []
    for i in range(cantidad_filas):
        fila = [valor_inicial] * cantidad_columnas

        matriz_estudiantes += [fila]

    return matriz_estudiantes

notas = inicializar_matriz(30, 5, 0)

def cargar_datos():
  for i in range(30):
    for j in range(5):
        notas[i][j] = calificaciones[i][j]

#2
def mostrar_todos_estudiantes(i):
    print(f"{i+1}) Legajo: {legajos[i]}, Nombre: {nombres[i]}, Género: {generos[i]}, Notas: {calificaciones[i]}")

def mostrar_uno():
    for i in range(30):
        mostrar_todos_estudiantes(i)

#3
def calcular_promedios():
    for i in range(30):
        suma = 0
        for j in range(5):
            suma = suma + calificaciones[i][j]
        promedio = suma / 5
        promedios[i] = promedio

#4
def ordenar_descendiente():
    for i in range(1, len(promedios), 1):
        for j in range(i + 1, len(promedios)):
            if promedios[i] < promedios[j]:
                aux = promedios[i]
                promedios[i] = promedios[j]
                promedios[j] = aux

                aux = nombres[i]
                nombres[i] = nombres[j]
                nombres[j] = aux

                aux = legajos[i]
                legajos[i] = legajos[j]
                legajos[j] = aux

                aux = generos[i]
                generos[i] = generos[j]
                generos[j] = aux

                aux = calificaciones[i]
                calificaciones[i] = calificaciones[j]
                calificaciones[j] = aux

def mostrar_ordenados_por_promedio():
    calcular_promedios()
    ordenar_descendiente()
    print("Estudiantes ordenados por promedio descendente:")
    for i in range(30):
        promedio = promedios[i]
        if type(promedio) == float or type(promedio) == int:
            promedio_mostrar = int(promedio * 100) // 100
        else:
            promedio_mostrar = "ERROR"
        print(
            str(i + 1) + ") Legajo:", legajos[i],
            "- Nombre:", nombres[i],
            "- Género:", generos[i],
            "- Promedio:", promedio_mostrar
        )


#5
def mejor_promedio():
    promedios_materia = [0] * 5
    for j in range(5):
        suma = 0
        for i in range(30):
            suma = suma + calificaciones[i][j]
        promedios_materia[j] = suma // 30

    mayor = promedios_materia[0]
    for j in range(1, 5):
        if promedios_materia[j] > mayor:
            mayor = promedios_materia[j]

    print("Materia/s con mayor promedio:")
    for j in range(5):
        if promedios_materia[j] == mayor:
            print("MATERIA_", j + 1, "con promedio", mayor)

#6
def buscar_legajo(leg):
    for i in range(30):
        if legajos[i] == leg:
            mostrar_todos_estudiantes(i)
            return
    print("Legajo no encontrado.")

#7
def repeticion_calificacion(materia):
    conteo = [0] * 10
    j = materia - 1
    for i in range(30):
        nota = calificaciones[i][j]
        conteo[nota - 1] = conteo[nota - 1] + 1
    for i in range(10):
        print("Nota", i + 1, "aparece", conteo[i], "veces.")



