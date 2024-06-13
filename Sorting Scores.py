# Imprimimos por pantalla un mensaje de bienvenida al programa
print("----------------------------------------------------")
print("---- Bienvenido al Registro de Notas de Alumnos ----")
print("----------------------------------------------------")

# Creamos un diccionario vacío donde albergaremos tanto los nombre como las notas
grupo = {}

# Iniciamos un bucle While indefinido
while True:
    # Creamos la variable Alumno, donde consultaremos el nombre y apellidos del alumno
    alumno = input("-> Ingresa el nombre y apellidos del alumno ('Salir' para terminar): ")
    # Si el usuario introduce "Salir" o "salir", se termina el programa
    if alumno == "Salir" or alumno == "salir":
        break
    # creamos la variable Nota, donde consultaremos la nota del alumno
    nota = int(input("-> Ingresa la nota del alumno: "))
    # Si el nombre y apellidos del alumno no se repiten y su nota está entre 1-10, se añade
    if alumno not in grupo and nota > 0 and nota < 11:
        grupo[alumno] = nota
    # De lo contrario, se imprime un mensaje informando del error
    else:
        print("*** Nombre Repetido o Nota Fuera De Rango ***")
        continue

# Imprimimos un mensaje mostrando la lista completa de alumnos con sus respectivas notas
print("----------------------------------------------------")
print("-> El grupo de alumnos con sus respectivas notas es: ", "\n", grupo)
print("----------------------------------------------------")

# Creamos variables donde almacenaremos la nota máxima y mínima, además del sumador y contador
nota_max = 10
nota_min = 1
sumador = 0
contador = 0

# Iniciamos un bucle For que recorrerá cada nota dentro del grupo de alumnos
for nota in grupo.values():
    # Si la nota es menor o igual a la nota máxima, se añadirá en la variable Nota_max
    if nota <= nota_max:
        nota_max = nota
    # Si la nota es mayor o igual a la nota mínima, se añadirá en la variable Nota_min
    if nota >= nota_min:
        nota_min = nota
    # Añadimos cada nota en el Sumador y aumentamos en 1 el Contador con cada vuelta del bucle
    sumador += nota
    contador += 1

# Imprimos por pantalla los resultados finales. Tanto la nota mínima, como la nota
# máxima y por último también la nota media de toda la clase, que se consigue dividiendo
# el resultado de la suma de todas las notas por el número de notas que hay
print("-> La mayor nota de la clase es: ", nota_min)
print("-> La menor nota de la clase es: ", nota_max)
print("-> La nota media de la clase es: ", sumador/contador)
print("----------------------------------------------------")