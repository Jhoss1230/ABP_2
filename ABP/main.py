import flet as ft
from flet import AppBar, ElevatedButton, View

def main(page: ft.Page):
    page.title = "La historia de la Musica"
    page.bgcolor="purple"
    page.window_width=900
    page.window_height=900
    
    image_width_Portada = 800
    image_height_Portada = 400
    
    border_radius = 25 
    
    img_height = 75
    img_width = 75


#audios para la informacion
    Intro=ft.Audio(src="intro de la musica.mp3",volume=1, balance=0)
    page.overlay.append(Intro)

    giovanni=ft.Audio(src="giovanni.mp3",volume=1, balance=0)
    page.overlay.append(giovanni)
#funcion para detener audios (sirve para cunado o se junten dos audios al mismo tiempo)
    def StopAll():
        Intro.pause()
        giovanni.pause()
#funcion para reproducir
    def playIntro(e):
        StopAll()
        Intro.play()

    def playgiovanni(e):
        StopAll()
        giovanni.play()

#botones
    btn1=ElevatedButton(content=ft.Image(src="giovanni.jpg", width=img_width, height=img_height, border_radius=border_radius, semantics_label="giovanni palestrina"), on_click=play_giovanni)
    
    def route_change(route):
        page.views.clear()
        
        if page.route == '/':
            page.views.append(
                View(
                    "/",
                    controls=[
                        AppBar(
                            title=ft.Text("La historia de la musica"),
                            bgcolor="purple"
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
                                        on_click=lambda _: [StopAll(), page.go('/principios')]
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
                            title=ft.Text("Principios de la Musica"),
                            bgcolor="purple"
                        ),
                        ft.Container(
                            ft.Column(
                                controls=[
                                    ElevatedButton(
                                        '>>>',
                                        on_click=lambda _: page.go('/renacimiento')
                                    ),
                                    ElevatedButton(
                                        '<<<',
                                        on_click=lambda _: page.go('/')
                                    )
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
        elif page.route == '/renacimiento':
            page.views.append(
                View(
                    "/renacimiento",
                    controls=[
                        AppBar(
                            title=ft.Text("El renacimiento de la musica (1400-1600)"),
                            bgcolor="purple"
                        ),
                        ft.Container(
                            ft.Column(
                                controls=[
                                    ElevatedButton(
                                        '>>>',
                                        on_click=lambda _: page.go('/barroco')
                                    ),
                                    ElevatedButton(
                                        '<<<',
                                        on_click=lambda _: page.go('/principios')
                                    ),
                                    ft.Row(
                                        alignment="center",
                                        controls=[
                                            btn1
                                        ]
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
        elif page.route == '/barroco':
            page.views.append(
                View(
                    "/barroco",
                    controls=[
                        AppBar(
                            title=ft.Text(" Baroco (1600-1750)"),
                            bgcolor="purple"
                        ),
                        ft.Container(
                            ft.Column(
                                controls=[
                                    ElevatedButton(
                                        '>>>',
                                        on_click=lambda _: page.go('/clasicismo')
                                    ),
                                    ElevatedButton(
                                        '<<<',
                                        on_click=lambda _: page.go('/renacimiento')
                                    )
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
        elif page.route == '/clasicismo':
            page.views.append(
                View(
                    "/clasicismo",
                    controls=[
                        AppBar(
                            title=ft.Text("El Clasicismo (1750-1820)"),
                            bgcolor="purple"
                        ),
                        ft.Container(
                            ft.Column(
                                controls=[
                                    ElevatedButton(
                                        '>>>',
                                        on_click=lambda _: page.go('/romantic')
                                        ),
                                    ElevatedButton(
                                        '<<<',
                                        on_click=lambda _: page.go('/barroco')
                                        )
                                    ],
                                alignment=ft.MainAxisAlignment.START
                            ),
                            bgcolor=page.bgcolor,
                            expand=True
                        ),
                    ],
                    bgcolor=page.bgcolor
                )
            )
        elif page.route == '/romantic':
            page.views.append(
                View(
                    "/romantic",
                    controls=[
                        AppBar(
                            title=ft.Text("El romanticismo(1820-1900)"),
                            bgcolor="purple"
                        ),
                        ft.Container(
                            ft.Column(
                                controls=[
                                    ElevatedButton(
                                        '>>>',
                                        on_click=lambda _: page.go('/moderno')
                                        ),
                                    ElevatedButton(
                                        '<<<',
                                        on_click=lambda _: page.go('/clasicismo')
                                        )
                                ],
                                alignment=ft.MainAxisAlignment.START
                            ),
                            bgcolor=page.bgcolor,
                            expand=True
                        ),
                    ],
                    bgcolor=page.bgcolor
                )
            )
        elif page.route == '/moderno':
            page.views.append(
                View(
                    "/moderno",
                    controls=[
                        AppBar(
                            title=ft.Text("El periodo moderno (1900-1960)"),
                            bgcolor="purple"
                        ),
                        ft.Container(
                            ft.Column(
                                controls=[
                                    ElevatedButton(
                                        '>>>',
                                        on_click=lambda _: page.go('/presente')
                                        ),
                                    ElevatedButton(
                                        '<<<',
                                        on_click=lambda _: page.go('/romantic')
                                        )
                                ],
                                alignment=ft.MainAxisAlignment.START
                            ),
                            bgcolor=page.bgcolor,
                            expand=True
                        ),
                    ],
                    bgcolor=page.bgcolor
                )
            )
        elif page.route == '/presente': 
            page.views.append(
                View(
                    "/presente",
                    controls=[
                        AppBar(
                            title=ft.Text("El periodo contemporaneo (1960-Presente)"),
                            bgcolor="purple"
                        ),
                        ft.Container(
                            ft.Column(
                                controls=[
                                    ElevatedButton(
                                        '>>>',
                                        on_click=lambda _: page.go('/')
                                        ),
                                    ElevatedButton(
                                        '<<<',
                                        on_click=lambda _: page.go('/moderno')
                                        )
                                    ],
                                    alignment=ft.MainAxisAlignment.START
                                ),
                                bgcolor=page.bgcolor,
                                expand=True
                            ),
                        ],
                        bgcolor=page.bgcolor
                    )
                )

        page.update()
    
    page.on_route_change = route_change
    page.go(page.route)

ft.app(target=main, assets_dir="assets") 
