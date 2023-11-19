from Logica.edificio import salas, aristas, matriz_aristas_ady,  materiales


def calcular_propagacion(sala_fuente, db_ruido, frecuencia, visitados):
    if frecuencia <= 63:
        hz = 0
    elif frecuencia <= 125:
        hz = 1
    else:
        hz = 2

    visitados.append(sala_fuente)

    for id_sala in range(len(salas)):
        if matriz_aristas_ady[sala_fuente][id_sala] > 0:
            id_material_uno = aristas[matriz_aristas_ady[sala_fuente][id_sala] - 1].id_material_uno
            id_material_dos = aristas[matriz_aristas_ady[sala_fuente][id_sala] - 1].id_material_dos
            distancia = aristas[matriz_aristas_ady[sala_fuente][id_sala] - 1].distancia
            at = 1.5 * distancia
            propagacion = db_ruido - at - materiales[id_material_uno].resistencias_frecuencias[hz] - \
                          materiales[id_material_dos].resistencias_frecuencias[hz]

            # Verifica si la sala ya ha sido visitada y si la nueva propagación es mayor
            if id_sala in visitados and propagacion > salas[id_sala].db_ruido:
                salas[id_sala].set_db_ruido(propagacion)
                # Vuelve a evaluar la sala para propagar el cambio
                calcular_propagacion(id_sala, propagacion, frecuencia, visitados)
            elif id_sala not in visitados and propagacion > 0:
                salas[id_sala].set_db_ruido(propagacion)
                # Llamada recursiva sin la condición id_sala not in visitados
                calcular_propagacion(id_sala, propagacion, frecuencia, visitados)


def mostrar_salas():
    for i in range(len(salas)):
        print(f"{i + 1}) Sala: {salas[i].actividad.nombre} {salas[i].numero}")
        print(f"Nivel ruido: {salas[i].db_ruido}")

        if salas[i].db_ruido > salas[i].actividad.max_db:
            margen = salas[i].actividad.max_db * 0.25
            if salas[i].db_ruido < (margen + salas[i].actividad.max_db) and salas[i].db_ruido > (
                    salas[i].actividad.max_db - margen):
                print("Sala habitable con recomendaciones\n")
            else:
                print("Sala NO habitable\n")
        else:
            print("Sala habitable\n")
