import flet as ft

def main(page: ft.Page):
    def add1(e):
        numero = int(numberlabel.value)
        numero+=1
        numberlabel.value = str(numero)
        page.update()
    def minus1(e):
        numero = int(numberlabel.value)
        numero-=1
        if numero < 0:
            numero = 0
        numberlabel.value = str(numero)
        page.update()

    page.horizontal_alignment = "RIGHT"
    page.vertical_alignment = "RIGHT"

    titletext = ft.Text(value="Counter")
    numberlabel = ft.Text(value="0")
    plusbutton = ft.IconButton(icon="add", on_click=add1)
    minusbutton = ft.IconButton(icon="remove", on_click=minus1)
    rowbuttons =ft.Row(controls={minusbutton , plusbutton}, alignment=ft.MainAxisAlignment.CENTER)
    image = ft.Image(src="sea otter pet.jpg")
    page.add(titletext, numberlabel, rowbuttons, image)

ft.app(target=main)