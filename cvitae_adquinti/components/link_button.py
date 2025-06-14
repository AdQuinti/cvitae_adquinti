import reflex as rx
import cvitae_adquinti.styles.styles as styles
from cvitae_adquinti.styles.styles import Size
from cvitae_adquinti.styles.colors import Color

def link_button(title: str, body: str, image: str, url: str) -> rx.Component: # recibe texto boton de links
    return rx.link(
        rx.button(
            rx.hstack(
                rx.image( # propiedades del icono
                    src=image, # imagen icono
                # # web accessibility - definicion exacta de tamaños
                    width=Size.LARGE.value, # anchura icono
                    height=Size.BIG.value, # altura icono
                    margin=Size.MEDIUM.value,
                    alt=title # web accessibility - titulo de cada boton
                ), #img predeterminada Reflex-libreria
                rx.vstack(
                    rx.text(title, style=styles.button_title_style),
                    rx.text(body, style=styles.button_body_style), # repetimos boton txt
                # colocación
                    align_items="start", # se aline al principio
                    spacing='1', #Size.SMALL.value,
                    padding_y=Size.SMALL.value,
                    padding_right=Size.SMALL.value # empuja a izq. DESIGN-RESPONSIVE
                ),
                width="100%" # ocupe objeto td el contenido del padre
            )
        ), 
        href=url,
        is_external=True,
        width="100%" # limita tamaño txt más grande
    )