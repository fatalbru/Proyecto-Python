import reflex as rx
import ProyectoPython.styles.styles as styles
def index() -> rx.Component:
    return rx.box(
        
        
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