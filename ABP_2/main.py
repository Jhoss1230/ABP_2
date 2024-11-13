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
    
    img_height = 150
    img_width = 150

#audios para la informacion
    Intro=ft.Audio(src="intro de la musica.mp3",volume=1, balance=0)
    page.overlay.append(Intro)

    giovanni = ft.Audio(src="Palestrina.mp3", volume=1, balance=0)
    page.overlay.append(giovanni)
    
#funcion para detener audios (sirve para cunado o se junten dos audios al mismo tiempo)
    def StopAll():
        Intro.pause()
        giovanni.pause()
#funcion para reproducir
    def playIntro(e):
        StopAll()
        Intro.play()

    def play_giovanni(e):
        StopAll()
        giovanni.play()

#botones
    btn1 = ElevatedButton(content=ft.Image(src="giovanni.jpg", width=img_width, height=img_height, border_radius=border_radius, semantics_label="giovanni"), on_click=play_giovanni)
    btn2 = ElevatedButton(content=ft.Image(src="Gregor Aichinger.jpg", width=img_width, height=img_height, border_radius=border_radius,),)
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
                                        on_click=lambda _: [StopAll(), page.go('/renacimiento')]
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
                                        on_click=lambda _: page.go('/')
                                    ),
                                    ft.Row(
                                        alignment="Giovanni Gabrieli""center",
                                        controls=[
                                            btn1
                                        ]
                                    ),
                                    ft.Row(
                                        alignment=btn1,
                                        controls=[
                                            ElevatedButton(
                                                'Giovanni Gabrieli',
                                            )
                                        ]
                                    ),
                                    ft.Column(
                                        alignment="Gregor Aichinger",
                                        controls=[
                                            btn2
                                        ]
                                    ),
                                    ft.Column(
                                        alignment=btn2,
                                        controls=[
                                            ElevatedButton(
                                                'Gregor Aichinger',
                                            )
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
                            title=ft.Text(" barrocal (1600-1750)"),
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
                                        on_click=lambda _: page.go('/romanticismo')
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
                        )
                    ],
                    bgcolor=page.bgcolor
                )
            )
        elif page.route == '/romanticismo':
            page.views.append(
                View(
                    "/romanticismo",
                    controls=[
                        AppBar(
                            title=ft.Text("Música del romanticismo"),
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
                                        on_click=lambda _: page.go('/contemporáneo')
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
        elif page.route == '/contemporáneo':
            page.views.append(
                View(
                    "/contemporáneo",
                    controls=[
                        AppBar(
                            title=ft.Text("contemporáneo 1960"),
                            bgcolor="purple"
                        ),
                        ft.Container(
                            ft.Column(
                                controls=[
                                    ElevatedButton(
                                        '>>>',
                                        on_click=lambda _: page.go('/2000')
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
        elif page.route == '/2000':
            page.views.append(
                View(
                    "/2000",
                    controls=[
                        AppBar(
                            title=ft.Text("Música de los años 2000"),
                            bgcolor="purple"
                        ),
                        ft.Container(
                            ft.Column(
                                controls=[
                                    ElevatedButton(
                                        '>>>',
                                        on_click=lambda _: page.go('/2020')
                                        ),
                                    ElevatedButton(
                                        '<<<',
                                        on_click=lambda _: page.go('/contemporáneo')
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
        elif page.route == '/2020': 
            page.views.append(
                View(
                    "/2020",
                    controls=[
                        AppBar(
                            title=ft.Text("Música del 2020"),
                            bgcolor="purple"
                        ),
                        ft.Container(
                            ft.Column(
                                controls=[
                                    ElevatedButton(
                                        '>>>',
                                        on_click=lambda _: page.go('/2024')
                                        ),
                                    ElevatedButton(
                                        '<<<',
                                        on_click=lambda _: page.go('/2000')
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
        elif page.route == '/2024': 
            page.views.append(
                View(
                    "/2024",
                    controls=[
                        AppBar(
                            title=ft.Text("Música del 2024"),
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
                                        on_click=lambda _: page.go('/2020')
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