import flet as ft


@ft.component
def App(page: ft.Page) -> ft.Component:
    page.title = "Hiroshi"
    return ft.Column(
        controls=[
            ft.Row(
                controls=[
                    ft.Image(
                        "actors/hiroshi/hiroshi-standing.png", fit=ft.BoxFit.CONTAIN
                    ),
                    ft.Image(
                        "actors/hiroshi/hiroshi-running.png", fit=ft.BoxFit.CONTAIN
                    ),
                    ft.Image(
                        "actors/hiroshi/hiroshi-whiskey.png", fit=ft.BoxFit.CONTAIN
                    ),
                    ft.Image(
                        "actors/hiroshi/hiroshi-motorcycle.png",
                        fit=ft.BoxFit.CONTAIN,
                    ),
                    ft.Image("actors/hiroshi/hiroshi-drunk.png"),
                ],
                expand=True,
            ),
            ft.Row(
                controls=[
                    ft.Image("actors/hiroshi/hiroshi-fight-a.png"),
                    ft.Image("actors/hiroshi/hiroshi-fight-b.png"),
                    ft.Image("actors/hiroshi/hiroshi-walking.png"),
                ],
                expand=True,
            ),
        ],
        expand=True,
    )


ft.run(lambda page: page.render(App, page))
