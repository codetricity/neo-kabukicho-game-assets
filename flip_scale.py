import flet as ft


def main(page: ft.Page):
    page.title = "Neo Kabukicho Assets"
    page.padding = 0  # eliminate padding.  there was a gap before.
    page.add(
        ft.Row(
            controls=[
                ft.Container(
                    padding=ft.Padding(left=20, top=20),
                    content=ft.Column(
                        spacing=10,
                        controls=[
                            ft.Text(
                                "scale height of character: height=page.height * 0.70",
                                size=20,
                            ),
                            ft.Text(
                                "horizontal flip: scale=ft.Scale(scale_x=-1)",
                                size=20,
                            ),
                            ft.Column(
                                spacing=0,
                                controls=[
                                    ft.Text(
                                        "align character to bottom: expand=True",
                                        size=20,
                                    ),
                                    ft.Text(
                                        "on both Container and Column",
                                        size=20,
                                    ),
                                ],
                            ),
                            ft.Container(
                                content=ft.Image(
                                    src="actors/aki/aki-eating.png",
                                    height=page.height * 0.70,
                                ),
                                expand=True,
                                alignment=ft.Alignment.BOTTOM_LEFT,
                            ),
                        ],
                    ),
                ),
                # use scale_x=-1 to flip character horizontally
                ft.Image(
                    src="actors/aki/aki-eating.png",
                    scale=ft.Scale(scale_x=-1),
                ),
                ft.Container(
                    content=ft.Image(
                        src="actors/aki/aki-standing.png",
                        height=page.height * 0.50,
                    ),
                ),
            ],
            expand=True,
        )
    )


ft.run(main=main, assets_dir="assets")
