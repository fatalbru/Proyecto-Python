import reflex as rx
import ProyectoPython.constants as constants
from ProyectoPython.styles.styles import Size,Color,TextColor


def github() -> rx.Component:
    return rx.link(

        rx.vstack(
            rx.vstack(
                rx.text(
                    "Proyecto"
                ),
                rx.text(
                    "en GitHub"
                ),
                align_items="start",
                class_name="nes-balloon from-right is-dark",
                margin_bottom=Size.BIG.value
            ),
            rx.box(
                rx.text(
                    constants.VERSION,
                    class_name="is-error"
                ),
                class_name="nes-badge"
            )
        ),
        rx.box(
            class_name="nes-octocat animate"
        ),
        href=constants.GITHUB_REPO_URL,
        is_external=True,
        align_items="end",
        display="flex",
        margin_top=Size.ZERO.value
    )
