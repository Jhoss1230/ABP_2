import flet as ft
from flet import AppBar, ElevatedButton, View

def main(page: ft.Page):
    page.title = "La historia de la Musica"
    page.bgcolor="purple"
    page.window_width=900
    page.window_height=900
    
    image_width_Portada = 800
    image_height_Portada = 400


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
    
    
        
        

    page.update()
    
    page.on_route_change = route_change
    page.go(page.route)

ft.app(target=main, assets_dir="assets") 