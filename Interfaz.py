import flet as ft
from flet_core import theme

def main(page: ft.Page):
    page.title = "Ruido Net (Proyecto Final Ciencias de la computación II)"
    page.theme_mode = "LIGHT"
    page.theme = theme.Theme(color_scheme_seed="#8F1006")
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    def abrir(e):
        try:
            fqs =  float(frecuencia.value)
            org = int (origen.value)
            rui = float(ruido.value)

            if  fqs>0 and fqs<=250 and org>=0 and org<=33:
                btn_ejecutar.disabled = True
                mensaje.value = 'Generando simulación....'
                page.update ()
                import subprocess
                # Ruta al script que quieres ejecutar
                ruta_script = "Simulacion.py"
                # Ejecutar el script
                subprocess.run(["python", ruta_script,frecuencia.value,origen.value,ruido.value])
                # reestablecer valores
                mensaje.value = 'Llena los espacios para generar la simulación'
                btn_ejecutar.disabled = False
                frecuencia.value = ''
                origen.value = ''
                ruido.value = ''
                page.update ()
            else:
                mensaje.value = 'Los datos registrados no son validos.'
                page.update()
        except:
            mensaje.value = 'El tipo de los datos no corresponde.'
            page.update ()


    frecuencia = ft.TextField (label='Ingrese el valor de frecuencia')
    origen = ft.TextField (label='ingrese el Origen')
    ruido = ft.TextField (label='Ingrese el nivel de Ruido')
    mensaje = ft.Text('Llena los espacios para generar la simulación')
    btn_ejecutar =  ft.ElevatedButton ('Generar simulación', on_click=abrir)
    columna = ft.Row(controls=[
        ft.Column(controls=[
            ft.Text ('Frecuencia (Hz, valor entre 0 y 250)',size=18,italic=True, weight=ft.FontWeight.W_500),
            frecuencia,
            ft.Text ('Origen (valor entre 0 y 33)',size=18,italic=True, weight=ft.FontWeight.W_500),
            origen,
            ft.Text ('Nivel de Ruido (DB)',size=18,italic=True, weight=ft.FontWeight.W_500),
            ruido,
            btn_ejecutar,
            mensaje
        ],expand=True, horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            alignment=ft.MainAxisAlignment.CENTER,spacing=20),
        ft.Container(ft.Column(
            [ft.Text("Proyecto final de Ciencias de la computación II",size=18,text_align=ft.TextAlign.CENTER),
             ft.Image (
                 src='resource/grafo_2d.svg',
                 width=500,
                 height=500,
                 fit=ft.ImageFit.NONE,
                 repeat=ft.ImageRepeat.NO_REPEAT,
             ),
             ft.Text("Jonnathan Sotelo Rodríguez - Handersson Felipe Pacheco Espitia - Holman Alejandro Alacón Herrera - Juan David Pulido Rodríguez",text_align=ft.TextAlign.CENTER)],
            alignment= ft.MainAxisAlignment.SPACE_BETWEEN, horizontal_alignment= ft.CrossAxisAlignment.CENTER
        ), expand=True, bgcolor=ft.colors.PRIMARY_CONTAINER,
                     height=page.window_height,alignment=ft.alignment.center,
                     shadow=ft.BoxShadow(1,5,color=ft.colors.PRIMARY_CONTAINER),border_radius=ft.border_radius.all(20),
                    padding=15),
    ],expand=True,vertical_alignment=ft.CrossAxisAlignment.CENTER, alignment=ft.MainAxisAlignment.CENTER)

    page.add(
        columna
    )

ft.app(main)