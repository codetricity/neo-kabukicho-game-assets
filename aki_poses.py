import flet as ft


@ft.component
def App(page: ft.Page):
    return ft.Column(
        controls=[
            ft.Row(
                controls=[
                    ft.Container(
                        content=ft.Image(
                            "actors/aki/aki_fight.png",
                            fit=ft.BoxFit.CONTAIN,
                        ),
                        expand=True,
                    ),
                    ft.Image("actors/aki/aki_fight.png", rotate=ft.Rotate(angle=-0.6)),
                    ft.Image("actors/aki/aki-computer.png"),
                    ft.Image("actors/aki/aki-running.png"),
                    ft.Image("actors/aki/aki-fight-2.png"),
                ],
                expand=True,
            ),
            ft.Row(
                controls=[
                    ft.Image("actors/aki/aki_motorcycle.png"),
                    ft.Image("actors/aki/aki-punching.png"),
                    ft.Text("Aki", size=100, weight=ft.FontWeight.BOLD),
                ],
                expand=True,
                alignment=ft.MainAxisAlignment.SPACE_EVENLY,
            ),
        ],
        expand=True,
    )


ft.run(lambda page: page.render(App, page), assets_dir="assets")
