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
                                        on_click=lambda _: [StopAll(),page.go('/principios')]
                                    ),
                                    ft.Image(
                                        src="portada.jpg",
                                        width=image_width_Portada,
                                        height=image_height_Portada,
                                        fit="cover"
                                    ),
                                    ElevatedButton(
                                        "Intro",
                                        on_click=playIntro
                                    ),
                                    
                                ],
                            )
                        )
                    ]
                )
            )

        page.update()
    
    page.on_route_change = route_change
    page.go(page.route)

ft.app(target=main, assets_dir="assets")
