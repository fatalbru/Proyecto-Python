import reflex as rx
import ProyectoPython.styles.styles as styles
from ProyectoPython.components.button import button
from ProyectoPython.styles.styles import Color,TextColor,Size
import ProyectoPython.constants as constants 
def instructions() -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.text("¿Como funciona el evento?",
                    class_name="title",
                    color=TextColor.ACCENT.value),
            rx.text("- Del 1 al 24 de diciembre descubrire cada dia un nuevo regalo en el calendario"),
            rx.text("- Puedes participar desde cualquier parte del mundo"),
            rx.text("- Solo tendras que hacer retwitt a la publicacion que enlazare desde esta web. Tu cuenta de Twitter/X tiene que ser publica."),
            button(
                "Twitter",
                constants.GITHUB_URL
                ),
            rx.text("- Al dia siguiente realizare el sorteo de forma publica en directo desde Twitch y Youtube"),
            button(
                "Twitch",
                constants.YOUTUBE_URL
                ),
            rx.text(
                "- !Vuelta a empezar! Publicare un nuevo regalo y comenzara de nuevo el proceso."),
            class_name="nes-container is-dark with-title",
            align_items="start",
            width="100%"
        ),
        style=styles.max_width_style
    )
    