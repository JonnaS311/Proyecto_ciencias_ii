from algoritmo import calcular_propagacion, mostrar_salas
from edificio import salas, visitados


origen = -1
while origen < 0 or origen > 34:
    origen = int(input("Digite el ID de la sala de ruido (1-34): ")) - 1

ruido = int(input("Digite la cantidad de ruido en DB: "))

frecuencia = -1
while frecuencia < 0 or frecuencia > 250:
    frecuencia = int(input("Digite la frecuencia entre los valores de 0 a 250Hz: "))

salas[origen].set_db_ruido(ruido)


calcular_propagacion(origen, ruido, frecuencia, visitados)

mostrar_salas()
