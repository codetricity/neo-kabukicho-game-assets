import flet as ft


@ft.component
def App(page: ft.Page):
    return ft.Row(controls=[ft.Text("hello")])


def main(page: ft.Page):
    page.render(App, page)


ft.run(main)
