import reflex as rx
import datetime
import ProyectoPython.constants as constants
import ProyectoPython.styles.styles as styles
from ProyectoPython.styles.styles import Size,Color,TextColor
from ProyectoPython.components.header_text import header_text
from ProyectoPython.components.button import button
from ProyectoPython.components.day import day
def calendar()->rx.Component:
    return rx.vstack(
        header_text(
            "heart",
            "Calendario de aDEViento"
        ),
        rx.vstack(
            rx.hstack(
            rx.text("El evento comienza en "),
            rx.text(id="countdown"),
            align_items="start"
            ),
            button(
                "Recordar",
                constants.FACEBOOK_URL
            ),
            rx.text(
                "Los regalos son sorpresa, permaneceran ocultos hasta el dia de su publicacion. No olvides pasarte por aqui cada dia para descubrir un nuevo sorteo"
            ),
            class_name="nes-container is-dark",
            align_items="start",
            width="100%"
        ),
        rx.grid(
            rx.foreach(
                list(range(1,25)), 
                lambda number:
                day(
                    number
                    )
            ),
            columns="3",
            spacing=Size.DEFAULT.value,
            width="100%",
            padding_top=Size.BIG.value,
            ),
        rx.script(src="/js/countdown.js"),
        style=styles.max_width_style,
    )