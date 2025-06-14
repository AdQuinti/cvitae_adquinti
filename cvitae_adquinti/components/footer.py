import reflex as rx
import datetime #para coger el año actual y sacarlo en texto
import cvitae_adquinti.constants as const
from cvitae_adquinti.styles.styles import Size
from cvitae_adquinti.styles.colors import Color, TextColor

def footer() -> rx.Component: # retorna reflex componentes
    return rx.vstack (
        rx.image (
            src="favico.ico", # imagen
            width=Size.BIG.value, # web accessibility definir tds tamaños
            height=Size.BIG.value,
            alt="Logotipo de AdQuinti, entre imagen de un mundo." # web accessibility - description
        ),
        rx.hstack(
            rx.text(
                f"@ 2004-{datetime.date.today().year} ",
                font_size=Size.MEDIUM.value
            ),
            rx.link("Ad-Quinti",
                href="#",
                is_external=True,
                font_size=Size.MEDIUM.value
            ), # se abre en otra pag.web
            margin_top=Size.ZERO.value # tamaño size espacio
        ),
        rx.text(
            "By Ad_Quinti Portfolio-V1-Beta. Building Software with Reflex-Python - 💚💜- FROM MALAGA",
            font_size=Size.MEDIUM.value,
            margin_top=Size.ZERO.value # tamaño size espacio
        ),
    # colocación
        margin_bottom=Size.BIG.value, # espacio pr abajo
        padding_bottom=Size.BIG.value,
        padding_x=Size.BIG.value,   # Design-Responsive - mantenga margenes ambos lados
        spacing='2', #Size.DEFAULT.value,
    # color
        color=TextColor.TXTFOOTER.value # TXT color
    ) # END vstack