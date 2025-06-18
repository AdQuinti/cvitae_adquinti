import reflex as rx
import datetime #para coger el año actual y sacarlo en texto
import cvitae_adquinti.constants as const
from cvitae_adquinti.styles.styles import Size
from cvitae_adquinti.styles.colors import Color, TextColor

def footer() -> rx.Component: # retorna reflex componentes
    return rx.vstack (
        rx.image (
            src="favico.ico", # imagen
            width=Size.MEDIUM.value, # web accessibility definir tds tamaños
            height=Size.MEDIUM.value,
            alt="Logotipo de AdQuinti, entre imagen de un mundo." # web accessibility - description
        ),
        rx.hstack(
            rx.text(
                f"@ 2004-{datetime.date.today().year} ",
                font_size=Size.SLIM.value
            ),
            rx.link("Ad-Quinti",
                href="#",
                is_external=True,
                font_size=Size.SLIM.value
            ), # se abre en otra pag.web
            margin_top=Size.ZERO.value # tamaño size espacio
        ),
        rx.text(
            "By @AdQuinti Portfolio. Building Software with Reflex-Python - 💚💜- FROM MALAGA",
            font_size=Size.SLIM.value,
            margin_top=Size.ZERO.value # tamaño size espacio
        ),
    # colocación
        margin_bottom=Size.MEDIUM.value, # espacio pr abajo
        padding_bottom=Size.MEDIUM.value,
        padding_x=Size.MEDIUM.value,   # Design-Responsive - mantenga margenes ambos lados
        spacing='2', #Size.DEFAULT.value,
    # color
        color=TextColor.TXTFOOTER.value, # TXT color
    # centrar footer
        align_items='center'  # <- Esto centra el contenido
    ) # END vstack