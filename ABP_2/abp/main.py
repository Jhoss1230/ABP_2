import flet as ft
from flet import AppBar, ElevatedButton, View

def main(page: ft.Page):
    page.window_width=650
    page.window_height=800
    
    image_width_Portada = 800
    image_height_Portada = 400
    
    page.bgcolor="blue"
    page.title="Historia de la musica"
    
#funcion para detener audios (sirve para cunado o se junten dos audios al mismo tiempo)
    def StopAll():
        Intro.pause()
#funcion para reproducir
    def playIntro(e):
        StopAll()
        Intro.play()


#audios
    Intro=ft.Audio(src="intro de la musica.mp3",volume=1,balance=0)
    page.overlay.append(Intro)
    Img1=ft.Image(src="musica.jpg")
    
    
#Creamos la interfaz
    btnIntro=ft.FilledButton(text="Escucha el intro",disabled=False,on_click=playIntro)

    page.add(
        ft.Row(
            alignment="CENTER",
            controls=[btnIntro,Img1]
        )
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
                        ),
                        ft.Container(
                            ft.Column(
                                controls=[
                                    ElevatedButton(
                                        '>>>',
                                        on_click=lambda _: [page.go('/principios')]
                                    ),
                                    ft.Image(
                                        src="portada.jpg",
                                        width=image_width_Portada,
                                        height=image_height_Portada,
                                        fit="cover"
                                    ),
                                ]
                            )
                        )
                    ]
                )
            )

        page.update()
    
    page.on_route_change = route_change
    page.go(page.route)

ft.app(target=main, assets_dir="assets")
