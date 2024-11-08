import flet as ft
from flet import AppBar, ElevatedButton, View

def main(page: ft.Page):
    page.window_width=800
    page.window_height=800
    
    page.bgcolor="blue"
    page.title="Historia de la musica"
    
#funcion para detener audios (sirve para cunado o se junten dos audios al mismo tiempo)
    def detener():
        Intro.pause()
#funcion para reproducir
    def playIntro(e):
        detener()
        Intro.play()


#audios
    Intro=ft.Audio(src="intro de la musica.mp3",volume=1,balance=0)
    page.overlay.append(Intro)
    Img1=ft.Image(src="musica.jpg")
    
    
#Creamos la interfaz
    btnIntro=ft.FilledButton(text="Escucha el intro",disabled=False,on_click=playIntro)
    btnsig=ft.FilledButton(text=">>")

    page.add(
        ft.Row(
            alignment="CENTER",
            controls=[btnIntro,Img1]
        ),
        ft.Column(
            alignment="star",
            controls=[btnsig]
        ),
    )
    def route_change(route):
        page.views.clear()
        
        if page.route == '/':
            page.views.append(
                View(
                    "/",
                    controls=[
                        AppBar(
                            title=ft.Text("La historia de la musica"),
                            bgcolor="gray"
                        )
                    ]
                )
            )

ft.app(target=main)
