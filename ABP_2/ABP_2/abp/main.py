import flet as ft
from flet import AppBar, ElevatedButton, View

def main(page: ft.Page):
    page.title = "La historia de la Musica"
    page.bgcolor="blue"
    page.window_width=650
    page.window_height=800
    
    image_width_Portada = 800
    image_height_Portada = 400
    
#audios para la informacion
    Intro=ft.Audio(src="intro de la musica.mp3", volume=1, balance=0)
    page.overlay.append(Intro)
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
                            bgcolor="blue"
                        ),
                        ft.Container(
                            ft.Column(
                                controls=[
                                    ElevatedButton(
                                        "Intro",
                                        on_click=playIntro
                                    ),
                                    ft.Image(
                                        src="musica.jpg",
                                        width=image_width_Portada,
                                        height=image_height_Portada,
                                        fit="cover"
                                    ),
                                    ElevatedButton(
                                        '>>>',
                                        on_click=lambda _: [StopAll(),page.go('/principios')]
                                    ),
                                    
                                ],
                                alignment=ft.MainAxisAlignment.START
                            ),
                            bgcolor=page.bgcolor,
                            expand=True
                        )
                    ],
                    bgcolor=page.bgcolor
                )
            )
        #vista de informacion
        elif page.route == '/principios':
            page.views.append(
                View(
                    "/principios",
                    controls=[
                        AppBar(
                            title=ft.Text("principios de la Musica"),
                            bgcolor="blue"
                        ),
                        ft.Container(
                            ft.Column(
                                controls=[
                                    ElevatedButton(
                                        '>>>',
                                        on_click=lambda _: page.go('/renacimiento')
                                    )
                                ],
                                alignment=ft.MainAxisAlignment.START
                            ),
                            bgcolor=page.bgcolor,
                            expand=True
                        )
                    ],
                )
            )
        elif page.route == '/renacimiento':
            page.views.append(
                View(
                    "/renacimiento",
                    controls=[
                        AppBar(
                            title=ft.Text("El renacimiento de la musica"),
                            bgcolor="blue"
                        )
                    ]
                )
            )

        page.update()
    
    page.on_route_change = route_change
    page.go(page.route)

ft.app(target=main, assets_dir="assets")
