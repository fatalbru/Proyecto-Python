import reflex as rx
import ProyectoPython.styles.styles as styles
from ProyectoPython.styles.styles import Size
from ProyectoPython.views.navbar import navbar
from ProyectoPython.views.header import header
from ProyectoPython.views.partners import partners
from ProyectoPython.views.author import author
from ProyectoPython.views.instructions import instructions
from ProyectoPython.views.calendar import calendar
from ProyectoPython.views.footer import footer
from ProyectoPython.components.github import github
def index() -> rx.Component:
    return rx.box(
        rx.script("document.documentElement.lang='es'"),
        rx.script(src="/js/snow.js"),
    navbar(),
    rx.center(
        rx.vstack(
            header(),
            instructions(),
            calendar(),
            author(),
            partners(),
            footer(),
            github(),
            width="100%",
            justify_content="center",  # Centrar los elementos dentro del stack
            align_items="center", 
            spacing=Size.VERY_BIG.value
        )
    )
        
    )
    
app = rx.App(
    
    stylesheets=styles.STYLESHEETS,
    style=styles.BASE_STYLE
)
app.add_page(
    index,
    title="Calendario de aDEViento 2024 | 24 dias. 24 regalos",
    description="Por tercer año, !aqui esta el calendario de adviento sorpresa de nuestra comunidad de developers!"
     )