class Libro:
    def __init__(self, titulo, autor, genero, puntuacion):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.puntuacion = puntuacion

lista_libros = []

while True:
    print("\n¿Qué acción deseas realizar?")
    print("1. Agregar Libro")
    print("2. Buscar Libros por Género")
    print("3. Recomendar Libro")
    print("4. Salir")
    opcion = input("Ingrese el número de la acción que deseas realizar: ")

    if opcion == "1":
        libro = Libro(input("Título: "), input("Autor: "), input("Género: "), float(input("Puntuación: ")))
        lista_libros.append(libro)
        print("Libro agregado exitosamente.")

    elif opcion == "2":
        genero = input("Género a buscar: ")
        libros = [libro.titulo for libro in lista_libros if libro.genero == genero]
        if libros:
            print("Libros en el género", genero, ":", ", ".join(libros))
        else:
            print("No se encontraron libros en el género", genero)

    elif opcion == "3":
        genero = input("Género de interés: ")
        libros = [libro for libro in lista_libros if libro.genero == genero]
        if libros:
            libro_recomendado = max(libros, key=lambda x: x.puntuacion)
            print("Libro recomendado en el género", genero, ":", libro_recomendado.titulo)
        else:
            print("No hay libros disponibles en el género", genero)

    elif opcion == "4":
        print("¡Gracias por usar la aplicación!")
        break

    else:
        print("Opción no válida. Por favor, ingrese un número válido.")
