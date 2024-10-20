import reflex as rx
from ProyectoPython.styles.styles import Size, Color
from ProyectoPython.components.link_icon import link_icon
import ProyectoPython.constants as constants
def navbar() -> rx.Component:
    return rx.vstack(
        rx.hstack(
        rx.image(
            src="mouredev.png",
            alt="Imagen pixel art de MoureDev con estilo navideño",
            width=Size.VERY_BIG.value,
            heigth=Size.VERY_BIG.value
            ),
        rx.text("aDEViento 2024"),
        rx.spacer(),
        link_icon(
          "youtube",
          constants.YOUTUBE_URL
        ),
        link_icon(
          "facebook",
          constants.FACEBOOK_URL
        ),
        link_icon(
          "github",
          constants.GITHUB_URL
        ),
        width="100%"
        ),
        bg=Color.PRIMARY.value,
        position="sticky",
        border_bottom=f"0.25em solid {Color.SECONDARY.value}",
        padding_x=Size.BIG.value,
        padding_y=Size.DEFAULT.value,
        z_index="999",
        top="0",
        width="100%"
    )