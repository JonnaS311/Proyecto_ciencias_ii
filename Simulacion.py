import math

from ursina import *
from Controlador import Controlador
from ursina.window import instance as window
from textwrap import dedent
from Intermedio import mediador, orden_id
import sys


argumentos = sys.argv[1:] # Frecuencia, Origen, Ruido
class Nodo (Entity):
    def __init__(self, id: int, position_x, position_z, position_y):
        super ().__init__ (
            parent=scene,
            model='sphere',
            texture='texture_nodo.jpg',
            scale=(1.5, 1.5, 1.5),
            color=color.white,
            rotation=Vec3 (0, 0, 0),
            position=(position_x, position_z, position_y),
            collider='box'
        )
        self.id = id
        self.sala = None
        self.solucion = ''

    def __repr__(self):
        return f"{self.id} y {self.position}"


class Arista (Entity):
    def __init__(self, posicion, escala, rotacion):
        super ().__init__ (
            parent=scene,
            model='cilindro.obj',
            color=color.white66,
            scale=(0.1, 0.1, escala * 0.25),
            position=posicion,
            rotation=rotacion
        )


def gen_cilindro(nodo1: Nodo, nodo2: Nodo):
    posiciones = (nodo1.position, nodo2.position)
    dist_x = abs (posiciones[0].x - posiciones[1].x)
    dist_y = abs (posiciones[0].y - posiciones[1].y)
    dist_z = abs (posiciones[0].z - posiciones[1].z)

    if dist_y > 0:
        return Arista (nodo1.position, dist_y, (270, 0, 0))
    elif dist_z > 0:
        return Arista (nodo1.position, dist_z, (0, 0, 0))
    else:
        return Arista (nodo1.position, dist_x, (0, 90, 0))


def input(key):
    if key == 'escape':
        application.quit()

app = Ursina(editor_ui_enabled=True)

nodos = [
    [Nodo (orden_id[x], (x % 2) * 12, 6, x * 6 + 3 - (x % 2) * 6) for x in range (6)],       # Nivel 1
    [Nodo (orden_id[x + 6], (x % 2) * 12, 12, x * 6 + 3 - (x % 2) * 6) for x in range (6)],  # Nivel 2
    [Nodo (orden_id[x + 12], (x % 2) * 12, 18, x * 6 + 3 - (x % 2) * 6) for x in range (6)], # Nivel 3
    [Nodo (orden_id[x + 18], (x % 2) * 12, 24, x * 6 + 3 - (x % 2) * 6) for x in range (6)], # Nivel 4
    [Nodo (orden_id[x + 24], (x % 2) * 12, 30, x * 6 + 3 - (x % 2) * 6) for x in range (6)], # Nivel 5
    [Nodo(6,6,9,36),Nodo(20,6,21,36)],   # Lateral izquierdo
    [Nodo(13,6,15,-6),Nodo(27,6,27,-6)]  # Lateral derecho
]

nodos = mediador(nodos,int(argumentos[1]),float(argumentos[2]),float(argumentos[0]))

aristas = []
for k in range (1, 6):
    for i in range (4):
        temp = gen_cilindro (nodos[0][i], nodos[0][i + 2])
        temp.y = k * 6
        aristas.append (temp)
    for i in range (3):
        temp = gen_cilindro (nodos[0][i * 2], nodos[0][i * 2 + 1])
        temp.y = k * 6
        aristas.append (temp)

x = (math.atan((nodos[5][0].position[1]-nodos[0][4].position[1])/(nodos[5][0].position[0]-nodos[0][4].position[0])))\
    *180/math.pi
z = (math.atan((nodos[5][0].position[1]-nodos[0][4].position[1])/(nodos[5][0].position[2]-nodos[0][4].position[2])))\
    *180/math.pi
aristas.append(Arista(nodos[5][0].position,11,(z-5,145,x)))
aristas.append(Arista(nodos[5][0].position,11,(z-5,145+70,x)))
aristas.append(Arista(nodos[5][0].position,11,(abs(z-5-360),145,x)))
aristas.append(Arista(nodos[5][0].position,11,(abs(z-5-360),145+70,x)))

aristas.append(Arista(nodos[5][1].position,11,(z-5,145,x)))
aristas.append(Arista(nodos[5][1].position,11,(z-5,145+70,x)))
aristas.append(Arista(nodos[5][1].position,11,(abs(z-5-360),145,x)))
aristas.append(Arista(nodos[5][1].position,11,(abs(z-5-360),145+70,x)))

aristas.append(Arista(nodos[6][0].position,11,(z-5,145+180,x)))
aristas.append(Arista(nodos[6][0].position,11,(z-5,145+70+180,x)))
aristas.append(Arista(nodos[6][0].position,11,(abs(z-5-360),145+180,x)))
aristas.append(Arista(nodos[6][0].position,11,(abs(z-5-360),145+70+180,x)))

aristas.append(Arista(nodos[6][1].position,11,(z-5,145+180,x)))
aristas.append(Arista(nodos[6][1].position,11,(z-5,145+70+180,x)))
aristas.append(Arista(nodos[6][1].position,11,(abs(z-5-360),145+180,x)))
aristas.append(Arista(nodos[6][1].position,11,(abs(z-5-360),145+70+180,x)))

ground = Entity (model='plane', scale=(100, 1, 100), color=color.white.tint (-.2), texture='pasto',
                 texture_scale=(50, 50), collider='box', position=(6, 0, 12))
roof = Entity (model='cube', scale=(100, 1, 100), color=color.rgb (255, 255, 255, 100),
               texture_scale=(100, 100), collider='box', position=(6, 43, 12))
plane_left = Entity (model='cube', scale=(100, 1, 80), color=color.rgb (255, 255, 255, 100),
                     texture_scale=(50, 50), collider='box', position=(6, 3, 62), rotation=(90, 0, 0))
plane_right = Entity (model='cube', scale=(100, 1, 80), color=color.rgb (255, 255, 255, 100),
                      texture_scale=(50, 50), collider='box', position=(6, 3, -38), rotation=(90, 0, 0))
plane_north = Entity (model='cube', scale=(80, 1, 100), color=color.rgb (255, 255, 255, 100),
                      texture_scale=(50, 50), collider='box', position=(-44, 3, 12), rotation=(0, 0, 90))
plane_south = Entity (model='cube', scale=(80, 1, 100), color=color.rgb (255, 255, 255, 100),
                      texture_scale=(50, 50), collider='box', position=(56, 3, 12), rotation=(0, 0, 90))
player = Controlador ()
sky = Sky ()

# Configuración de la pantalla de información
column = Entity(parent=window.editor_ui, position=window.top_left)
column.textField = TextField(parent=column, scale=.5, font='Consolas', max_lines=20, position=(0,0),
                             register_mouse_input=True, text_input=None, active=False)
column.textField.text_entity.color = color.azure
column.textField.text_entity.size = 0.04
column.textField.render()
column.textField.bg.color = color.black66
column.textField.bg.scale_x = 1.5

def update():
    entidad = mouse.hovered_entity
    if isinstance(entidad, Nodo):
        # Información de un nodo concreto
        habitabilidad = None
        if entidad.color == color.red:
            habitabilidad = 'No es habitable'
        elif entidad.color == color.orange:
            habitabilidad = 'Habitable con recomendaciones'
        else:
            habitabilidad = 'Es habitable'

        column.textField.text = dedent ('''
           --------- CONSOLA DE INFORMACIÓN ----------
            Frecuencia: {frecuencia}
            Origen: {origen}
            Nivel de ruido: {ruido} 
            Habitabilidad: {habitabilidad}
            Sala: {sala}
            Nivel Ruido: {n_ruido}
            Actividad: {actividad}
            Ruido permitido : {max}
            Sugerencia: {sugerencia}
            ''').format(frecuencia=argumentos[0], origen=argumentos[1], ruido= argumentos[2], id=entidad.id,
                        habitabilidad=habitabilidad, sala=entidad.sala.id,n_ruido=entidad.sala.db_ruido,
                        actividad=entidad.sala.actividad.nombre, max=entidad.sala.actividad.max_db,
                        sugerencia=entidad.solucion)
        column.textField.render()
    else:
        column.textField.text = dedent ('''
                   --------- CONSOLA DE INFORMACIÓN ----------
                    Frecuencia: {frecuencia}
                    Origen: {origen}
                    Nivel de ruido: {ruido} 
                    ''').format (frecuencia=argumentos[0], origen=argumentos[1], ruido=argumentos[2])
        column.textField.render ()


app.run()
