import reflex as rx
from ProyectoPython.styles.styles import Size,TextColor
import ProyectoPython.styles.styles as styles
import ProyectoPython.constants as constants
def header() -> rx.Component:
    return rx.vstack(
        rx.heading(
            "Calendario de aDEViento 2024",
            font_size=Size.BIG.value,
            padding_bottom=Size.DEFAULT.value,
            margin_bottom=Size.MEDIUM.value
            ),
        rx.flex(
            rx.image(
                src="mouredev.png",
                alt="Imagen pixel art de Mouredev con estilo navideño",
                width="16em",
                height="16em",
                margin_right= Size.BIG.value
                ),
            rx.vstack(
                rx.box(
                    "24 dias. 24 regalos\n",
                    "Del 1 al 24 de diciembre",
                    class_name="nes-balloon from-left is-dark",
                    font_size="18px"
                ),
                rx.text(
                    "Por tercer año, !aqui esta el calendario de adviento sorpresa de nuestra ",
                    rx.text(
                        "comunidad de developers",
                        color=TextColor.ACCENT.value,
                        font_size=Size.DEFAULT.value
                    ),
                    "!",
                    ),
                rx.text(
                    "Una actividad en la que cada dia sorteare un regalo relacionado con programacion y desarrollo de software(libros, cursos, etc)"
                    ),
                rx.text(
                    "Su finalidad es ayudar a compartir conocimiento y fomentar el aprendizaje en comunidad"
                    ),
                rx.link(
                    "#aDEViento2024",
                    href=constants.HASHTAG_URL,
                    is_external=True,
                    color=TextColor.TERTIARY.value,
                    padding_top=Size.BIG.value,
                    font_size=Size.MEDIUM.value
                ),
        align_items="start"
            ),
            flex_direction=["column","column","column","row","row"]
        ),
        padding_top=Size.VERY_BIG.value,
        style=styles.max_width_style
    )
    