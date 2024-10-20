import reflex as rx
from ProyectoPython.styles.styles import Size,TextColor
import ProyectoPython.styles.styles as styles
import ProyectoPython.constants as constants
def footer()->rx.Component:
    return rx.hstack(
        rx.vstack(
            rx.text(
                "Calendario de aDEViento 2024",
                font_size=Size.MEDIUM.value,
                margin_bottom=Size.ZERO.value
                ),
            rx.link(
                "Creado con ",
                rx.box(class_name="nes-icon is-small heart"),
                " (y gracias a ti) por fatalbru by Henry Quispe",
                href=constants.HENRY_URL,
                is_external=True,
                font_size=Size.MEDIUM.value,
                color=TextColor.TERTIARY.value
                ),
            align_items="start",
            spacing=Size.MEDIUM.value
        ),
        rx.spacer(),
        rx.image(
            src="logo.png",
            alt="logo mouredev. Una letra eme entre dos corchetes",
            class_name="nes-avatar is-large"
            ),
        padding_bottom=Size.BIG.value,
        style=styles.max_width_style,
        align_items="center"
        
    )