# titulo de la zona de los botones - divide bloques
import reflex as rx
import cvitae_adquinti.styles.styles as styles


def title(text: str) -> rx.Component: # recibe solo titulo - divide bloque botones
    return rx.heading(
        text,
        #size="lg", # Propiedad tamaños HEADING - reflex.dev/docs/library/typography/heading/
            # puedes cambiar a --> "sm","md","lg","xl","2xl","3xl","4xl", 
        style=styles.title_style
    )