#EXAMEN


def validar_texto(valor):
    """Valida que el texto no esté vacío ni contenga solo espacios."""
    return valor.strip() != ""


def validar_duracion(duracion):
    """Valida que la duración sea un entero mayor que cero."""
    return duracion > 0


def validar_clasificacion(clasificacion):
    """Valida que la clasificación sea 'A', 'B' o 'C'."""
    return clasificacion.upper() in ("A", "B", "C")


def validar_es3d(valor):
    """Valida que el valor ingresado sea 's' o 'n'."""
    return valor.lower() in ("s", "n")


def validar_precio(precio):
    """Valida que el precio sea un entero mayor que cero."""
    return precio > 0


def validar_cupos(cupos):
    """Valida que los cupos sean un entero mayor o igual a cero."""
    return cupos >= 0




def buscar_codigo(codigo, diccionario):
    """Retorna True si el código existe en el diccionario dado."""
    for clave in diccionario:
        if clave.upper() == codigo.upper():
            return True
    return False


def obtener_clave_real(codigo, diccionario):
    """Retorna la clave exacta almacenada (respetando mayúsculas originales)."""
    for clave in diccionario:
        if clave.upper() == codigo.upper():
            return clave
    return None


def actualizar_precio(codigo, nuevo_precio, cartelera):
    """Actualiza el precio de una película si el código existe."""
    if buscar_codigo(codigo, cartelera):
        clave = obtener_clave_real(codigo, cartelera)
        cartelera[clave][0] = nuevo_precio
        return True
    return False


def eliminar_pelicula(codigo, peliculas, cartelera):
    """Elimina el registro de una película en ambos diccionarios."""
    if buscar_codigo(codigo, peliculas):
        clave = obtener_clave_real(codigo, peliculas)
        del peliculas[clave]
        del cartelera[clave]
        return True
    return False


def agregar_pelicula(codigo, titulo, genero, duracion, clasificacion, idioma,
                      es_3d, precio, cupos, peliculas, cartelera):
    """Agrega una nueva película en ambos diccionarios si el código no existe."""
    if buscar_codigo(codigo, peliculas):
        return False
    peliculas[codigo] = [titulo, genero, duracion, clasificacion, idioma, es_3d]
    cartelera[codigo] = [precio, cupos]
    return True




def cupos_genero(genero, peliculas, cartelera):
    """Muestra el total de cupos disponibles para un género dado."""
    total = 0
    for codigo, datos in peliculas.items():
        if datos[1].lower() == genero.lower():
            total += cartelera[codigo][1]
    print(f"El total de cupos disponibles es: {total}")


def busqueda_precio(p_min, p_max, peliculas, cartelera):
    """Muestra las películas dentro de un rango de precio y con cupos disponibles."""
    resultados = []
    for codigo, datos in cartelera.items():
        precio = datos[0]
        cupos = datos[1]
        if p_min <= precio <= p_max and cupos != 0:
            titulo = peliculas[codigo][0]
            resultados.append(f"{titulo}--{codigo}")

    resultados.sort()

    if len(resultados) == 0:
        print("No hay películas en ese rango de precios.")
    else:
        print(f"Las películas encontradas son: {resultados}")




def leer_opcion():
    """Solicita y valida la opción numérica del menú principal."""
    opcion_valida = False
    while not opcion_valida:
        try:
            opcion = int(input("Ingrese opción: "))
            if 1 <= opcion <= 6:
                opcion_valida = True
            else:
                print("Debe seleccionar una opción válida")
        except ValueError:
            print("Debe seleccionar una opción válida")
    return opcion




def main():
    peliculas = {
        'P101': ['Luz de Otoño', 'drama', 110, 'B', 'Español', False],
        'P102': ['Noche Neón', 'acción', 125, 'C', 'Ingles', True],
        'P103': ['Planeta Agua', 'documental', 90, 'A', 'Español', False],
        'P104': ['Risa Total', 'comedia', 105, 'A', 'Español', True],
        'P105': ['Código Zero', 'thriller', 118, 'C', 'Ingles', True],
        'P106': ['Viaje Lunar', 'ciencia ficción', 132, 'B', 'Ingles', False],
    }

    cartelera = {
        'P101': [5990, 40],
        'P102': [7990, 0],
        'P103': [4990, 25],
        'P104': [6990, 12],
        'P105': [8990, 8],
        'P106': [7490, 3],
    }

    programa_activo = True
    while programa_activo:
        print("\n========== MENÚ PRINCIPAL ==========")
        print("1. Cupos por género")
        print("2. Búsqueda de películas por rango de precio")
        print("3. Actualizar precio de película")
        print("4. Agregar película")
        print("5. Eliminar película")
        print("6. Salir")
        print("=====================================")

        opcion = leer_opcion()

       
        if opcion == 1:
            genero = input("Ingrese género a consultar: ")
            cupos_genero(genero, peliculas, cartelera)

        
        elif opcion == 2:
            valores_validos = False
            while not valores_validos:
                try:
                    p_min = int(input("Ingrese precio mínimo: "))
                    p_max = int(input("Ingrese precio máximo: "))
                    if p_min >= 0 and p_max >= 0 and p_min <= p_max:
                        valores_validos = True
                    else:
                        print("Debe ingresar valores enteros")
                except ValueError:
                    print("Debe ingresar valores enteros")
            busqueda_precio(p_min, p_max, peliculas, cartelera)

        
        elif opcion == 3:
            seguir = "s"
            while seguir == "s":
                codigo = input("Ingrese código de película: ")
                try:
                    nuevo_precio = int(input("Ingrese nuevo precio: "))
                    if nuevo_precio > 0:
                        if actualizar_precio(codigo, nuevo_precio, cartelera):
                            print("Precio actualizado")
                        else:
                            print("El código no existe")
                    else:
                        print("El precio debe ser un entero positivo")
                except ValueError:
                    print("Debe ingresar un valor entero")

                seguir = input("¿Desea actualizar otro precio (s/n)?: ").lower()

       
        elif opcion == 4:
            codigo = input("Ingrese código de película: ")
            titulo = input("Ingrese título: ")
            genero = input("Ingrese género: ")

            try:
                duracion = int(input("Ingrese duración (minutos): "))
                duracion_ok = validar_duracion(duracion)
            except ValueError:
                duracion = None
                duracion_ok = False

            clasificacion = input("Ingrese clasificación: ")
            idioma = input("Ingrese idioma: ")
            es_3d_texto = input("¿Es 3D? (s/n): ")

            try:
                precio = int(input("Ingrese precio: "))
                precio_ok = validar_precio(precio)
            except ValueError:
                precio = None
                precio_ok = False

            try:
                cupos = int(input("Ingrese cupos: "))
                cupos_ok = validar_cupos(cupos)
            except ValueError:
                cupos = None
                cupos_ok = False

            codigo_ok = validar_texto(codigo) and not buscar_codigo(codigo, peliculas)
            titulo_ok = validar_texto(titulo)
            genero_ok = validar_texto(genero)
            clasificacion_ok = validar_clasificacion(clasificacion)
            idioma_ok = validar_texto(idioma)
            es3d_ok = validar_es3d(es_3d_texto)

            if not codigo_ok:
                print("El código no es válido o ya existe")
            elif not titulo_ok:
                print("El título no es válido")
            elif not genero_ok:
                print("El género no es válido")
            elif not duracion_ok:
                print("La duración no es válida")
            elif not clasificacion_ok:
                print("La clasificación no es válida")
            elif not idioma_ok:
                print("El idioma no es válido")
            elif not es3d_ok:
                print("El valor de 3D no es válido")
            elif not precio_ok:
                print("El precio no es válido")
            elif not cupos_ok:
                print("Los cupos no son válidos")
            else:
                es_3d = es_3d_texto.lower() == "s"
                if agregar_pelicula(codigo, titulo, genero, duracion,
                                     clasificacion.upper(), idioma, es_3d,
                                     precio, cupos, peliculas, cartelera):
                    print("Película agregada")
                else:
                    print("El código ya existe")

        
        elif opcion == 5:
            codigo = input("Ingrese código de película a eliminar: ")
            if eliminar_pelicula(codigo, peliculas, cartelera):
                print("Película eliminada")
            else:
                print("El código no existe")

       
        elif opcion == 6:
            programa_activo = False
            print("Programa finalizado.")


if __name__ == "__main__":
    main()