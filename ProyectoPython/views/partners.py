import reflex as rx
import datetime
import ProyectoPython.constants as constants
import ProyectoPython.styles.styles as styles
from ProyectoPython.styles.styles import Size,Color,TextColor
from ProyectoPython.components.header_text import header_text
from ProyectoPython.components.button import button
def partners() -> rx.Component:
    return rx.vstack(
        rx.vstack(
          header_text(
              "star",
              "Patrocinado por ",
              False
          )  ,
          rx.text(
              "Con el apoyo de la comunidad y los patrocinadores costeare los 24 regalos. Imaginate tu logo aqui y en todas las comunicaciones diarias durante el evento."
              ),
          rx.text("¿Quieres apoyar esta iniciativa? Escribeme a mi CORREO"
                  ),
          padding_y=Size.VERY_BIG.value,
          style=styles.max_width_style
        ),
        bg=Color.ACCENT.value,
        width="100%",
        align_items="center"
    )