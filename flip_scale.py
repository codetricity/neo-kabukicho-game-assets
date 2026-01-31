import flet as ft


def main(page: ft.Page):
    page.title = "Neo Kabukicho Assets"
    page.padding = 0  # eliminate padding.  there was a gap before.
    page.add(
        ft.Row(
            controls=[
                ft.Container(
                    content=ft.Image(
                        src="actors/aki/aki-eating.png",
                        height=page.height * 0.70,
                    ),
                    expand=True,
                    alignment=ft.Alignment.BOTTOM_LEFT,
                ),
                # use scale_x=-1 to flip character horizontally
                ft.Image(
                    src="actors/aki/aki-eating.png",
                    scale=ft.Scale(scale_x=-1),
                ),
            ],
            expand=True,
        )
    )


ft.run(main=main, assets_dir="assets")
