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

    img_height = 200
    img_width = 200

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
#renacimiento
    btn1 = ElevatedButton(content=ft.Image(src="giovanni.jpg", width=img_width, height=img_height, border_radius=border_radius, semantics_label="giovanni"), on_click=play_giovanni)
    btn2 = ElevatedButton(content=ft.Image(src="Gregor Aichinger.jpg", width=img_width, height=img_height, border_radius=border_radius,),)
    btn3 =ElevatedButton(content=ft.Image(src="Elias Nicolaus Ammerbach.jpg", width=img_width, height=img_height, border_radius=border_radius,),)
    btn4=ElevatedButton(content=ft.Image(src="Thoinot Arbeau.jpg", width=img_width, height=img_height, border_radius=border_radius,),)
    #barrocal
    btn5=ElevatedButton(content=ft.Image(src="Johann Sebastian Bach.jpg", width=img_width, height=img_height, border_radius=border_radius,),)
    btn6=ElevatedButton(content=ft.Image(src="Georg Friedrich Händel.jpg", width=img_width, height=img_height, border_radius=border_radius,),)
    btn7=ElevatedButton(content=ft.Image(src="Pietro Locatelli.jpg", width=img_width, height=img_height, border_radius=border_radius,),)
    btn8=ElevatedButton(content=ft.Image(src="Giovanni Battista Pergolesi.jpg", width=img_width, height=img_height, border_radius=border_radius,),)
    #clacismo
    btn9=ElevatedButton(content=ft.Image(src="Christoph Willibald Gluck.jpg", width=img_width, height=img_height, border_radius=border_radius,),)
    btn10=ElevatedButton(content=ft.Image(src="Ludwig van Beethoven.jpg", width=img_width, height=img_height, border_radius=border_radius,),)
    btn11=ElevatedButton(content=ft.Image(src="Wolfgang Amadeus Mozart.jpg", width=img_width, height=img_height, border_radius=border_radius,),)
    btn12=ElevatedButton(content=ft.Image(src="Joseph Haydn.jpg", width=img_width, height=img_height, border_radius=border_radius,),)
    #romanticismo
    btn13=ElevatedButton(content=ft.Image(src="Frédéric Chopin.jpg", width=img_width, height=img_height, border_radius=border_radius,),)
    btn14=ElevatedButton(content=ft.Image(src="Franz Schubert.jpg", width=img_width, height=img_height, border_radius=border_radius,),)
    btn15=ElevatedButton(content=ft.Image(src="Fanny Mendelssohn.jpg", width=img_width, height=img_height, border_radius=border_radius,),)
    btn16=ElevatedButton(content=ft.Image(src="Johannes Brahms.jpg", width=img_width, height=img_height, border_radius=border_radius,),)
    #moderno
    btn17=ElevatedButton(content=ft.Image(src="Ígor Stravinski.jpg", width=img_width, height=img_height, border_radius=border_radius,),)
    btn18=ElevatedButton(content=ft.Image(src="Paul Hindemith.jpg", width=img_width, height=img_height, border_radius=border_radius,),)
    btn19=ElevatedButton(content=ft.Image(src="Sergéi Prokófiev.jpg", width=img_width, height=img_height, border_radius=border_radius,),)
    btn20=ElevatedButton(content=ft.Image(src="Dmitri Shostakóvich.jpg", width=img_width, height=img_height, border_radius=border_radius,),)

#botones con informacion
#renacimiento
    a=ElevatedButton("Giovanni Gabrieli")
    b=ElevatedButton("Gregor Aichinger")
    c=ElevatedButton("Elias Nicolaus Ammerbach")
    d=ElevatedButton("Thoinot Arbeau")
    #barrocal
    e=ElevatedButton("Johann Sebastian Bach")
    f=ElevatedButton("Georg Friedrich Händel")
    g=ElevatedButton("Pietro Locatelli")
    h=ElevatedButton("Giovanni Battista Pergolesi")
    #clacismo
    i=ElevatedButton("Christoph Willibald Gluck")
    j=ElevatedButton("Ludwig van Beethoven")
    k=ElevatedButton("Wolfgang Amadeus Mozart")
    l=ElevatedButton("Joseph Haydn")
    #romanticismo
    m=ElevatedButton("Frédéric Chopin")
    n=ElevatedButton("Franz Schubert")
    ñ=ElevatedButton("Sergéi Prokófiev")
    o=ElevatedButton("Johannes Brahms")
    #moderno
    p=ElevatedButton("Ígor Stravinski")
    q=ElevatedButton("Paul Hindemith")
    r=ElevatedButton("Fanny Mendelssohn")
    s=ElevatedButton("Dmitri Shostakóvich")

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
                                        alignment="center",
                                        controls=[
                                            btn1,btn2,btn3
                                        ]
                                    ),
                                    ft.Row(
                                        alignment="center",
                                        controls=[
                                            a,b,c
                                        ]
                                    ),
                                    ft.Row(
                                        alignment="center",
                                        controls=[
                                            btn4
                                        ]
                                    ),
                                    ft.Row(
                                        alignment="center",
                                        controls=[
                                            d
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
                                    ft.Row(
                                        alignment="center",
                                        controls=[
                                            btn5,btn6,btn7
                                        ]
                                    ),
                                    ft.Row(
                                        alignment="center",
                                        controls=[
                                            e,f,g
                                        ]
                                    ),
                                    ft.Row(
                                        alignment="center",
                                        controls=[
                                            btn8
                                        ]
                                    ),
                                    ft.Row(
                                        alignment="center",
                                        controls=[
                                            h
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
                                    ),
                                    ft.Row(
                                        alignment="center",
                                        controls=[
                                            btn9,btn10,btn11
                                        ]
                                    ),
                                    ft.Row(
                                        alignment="center",
                                        controls=[
                                            i,j,k
                                        ]
                                    ),
                                    ft.Row(
                                        alignment="center",
                                        controls=[
                                            btn12
                                        ]
                                    ),
                                    ft.Row(
                                        alignment="center",
                                        controls=[
                                            l
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
                                    ft.Row(
                                        alignment="center",
                                        controls=[
                                            btn13,btn14,btn15
                                        ]
                                    ),
                                    ft.Row(
                                        alignment="center",
                                        controls=[
                                            m,n,ñ
                                        ]
                                    ),
                                    ft.Row(
                                        alignment="center",
                                        controls=[
                                            btn16
                                        ]
                                    ),
                                    ft.Row(
                                        alignment="center",
                                        controls=[
                                            o
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
                                        ),
                                        ft.Row(
                                        alignment="center",
                                        controls=[
                                            btn17,btn18,btn19
                                        ]
                                    ),
                                    ft.Row(
                                        alignment="center",
                                        controls=[
                                            p,q,r
                                        ]
                                    ),
                                    ft.Row(
                                        alignment="center",
                                        controls=[
                                            btn20
                                        ]
                                    ),
                                    ft.Row(
                                        alignment="center",
                                        controls=[
                                            s
                                        ]
                                    ),
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
                                        ),
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