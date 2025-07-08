# iconos redes sociales
import reflex as rx
#import cvitae_adquinti.styles.styles as styles
from cvitae_adquinti.styles.styles import Size

def link_icon(image: str, url: str, alt: str) -> rx.Component:
    return rx.link(
        rx.image(
            src=image,
        # web accessibility - definicion tamaños
            width=Size.BIG.value,
            height=Size.BIG.value,
            alt=alt # web accessibility - titulo de cada boton, pr eso se pasa pr parametro
        ),
        href=url,
        is_external=True
    )
