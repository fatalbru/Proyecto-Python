import reflex as rx
import ProyectoPython.constants as constants
import ProyectoPython.styles.styles as styles
from ProyectoPython.styles.styles import Size,Color
from ProyectoPython.components.button import button
from ProyectoPython.components.header_text import header_text
def author() -> rx.Component:
    return rx.vstack(
        header_text(
            "like",
            "Hola, mi nombre es Henry Quispe"
        ),
        rx.flex(
            rx.avatar(
                name="Henry Quispe",
                size="2xl",
                src="mouredev.jpg",
                bg=Color.PRIMARY.value,
                padding="2px",
                border="4px",
                border_color=Color.SECONDARY.value,
                margin_right=Size.DEFAULT.value,
                margin_bottom=Size.DEFAULT.value
                ),
            rx.vstack(
            rx.text("Soy estudiante de Ingenieria Informatica de la FNI"),
            rx.text("Desde 2015 que incursiono en el mundo de la tecnologia y Programacion Competitiva"),
            rx.mobile_only(
              rx.vstack(
                  author_buttons()
              )  
            ),
            rx.tablet_and_desktop(
                rx.hstack(
                    author_buttons()
                )
            ),
            width="100%",
            aligh_items="start"
            ),
            aligh_items="start",
            spacing=Size.BIG.value,
            flex_direction=["column","column","column","row","row"]
        ),
        style=styles.max_width_style
    )
def author_buttons()->rx.Component:
   return rx.box(
        button(
            "Youtube",
            constants.YOUTUBE_URL
        ),
        button(
            "Facebook",
            constants.FACEBOOK_URL
        ),
        button(
            "Mi Web",
            constants.HENRY_URL
        )
    )