from Logica.algoritmo import calcular_propagacion, mostrar_salas
from Logica.edificio import *
from ursina import *


orden_id = [1,0,3,2,5,4,12,11,10,9,8,7,15,14,17,16,19,18,26,25,24,23,22,21,29,28,31,30,33, 32]

solucion_avanzada = ['Cortinas y tapices gruesos',
                     'Muebles y alfombras',
                     'Sellado de puertas y ventanas',
                     'Paneles acústicos']

solucion_media = ['Acondicionamiento acústico profesional',
                  'Doble acristalamiento',
                  'Renovación arquitectónica',
                  'Sistemas de cancelación de ruido']
def mediador(nodos:list,origen,ruido,frecuencia):
    salas[origen].set_db_ruido (ruido)
    calcular_propagacion (origen, ruido, frecuencia, visitados)

    for i in nodos:
        for j in i:
            j.sala = salas[j.id]
            if salas[j.id].db_ruido > salas[j.id].actividad.max_db:
                margen = salas[j.id].actividad.max_db * 0.25
                if salas[j.id].db_ruido < (margen + salas[j.id].actividad.max_db) and salas[j.id].db_ruido > (
                        salas[j.id].actividad.max_db - margen):
                    j.color = color.orange
                    j.solucion = solucion_media[random.randint(0,3)]
                else:
                    j.color = color.red
                    j.solucion = solucion_avanzada[random.randint(0,3)]
            else:
                j.color = color.green
                j.solucion = 'No requiere efectuar ningún cambio'
    return nodos

