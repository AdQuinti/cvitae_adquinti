import reflex as rx
from enum import Enum
from .colors import Color, TextColor
from .fonts import Font, FontWeight # traemos fuente y peso de la fuente

# Constants
MAX_WIDTH="560px"

# Styles - fuentes desde web
# STYLESHEETS = ["https://fonts.googleapis.com/css2?family=Poopins:wght@300;500&display=swap",
#            "https://fonts.googleapis.com/css2?family=Comfortaa:wght@500&display=swap"]
STYLESHEETS = ["https://fonts.googleapis.com/css2?family=Pacifico:wght@400&display=swap",
            "https://fonts.googleapis.com/css2?family=Poopins:wght@300;500&display=swap",
            "https://fonts.googleapis.com/css2?family=Comfortaa:wght@500&display=swap"]
# fuente -> dire googleapis/css?family=fuente:tamña@concreta;concreta2..
#display=swap -> mostrará fuente por defecto


# Sizes
class Size(Enum): # encapsulado espaciadores de la web
    ZERO = "0.1px !importat"
    SMALL = "0.4em"
    SLIM = "0.6em"
    MEDIUM = "0.8em"
    DEFAULT = "1.2em"
    LARGE = "1.8em"
    BIG = "3em"
    VERY_BIG = "4em"

# Components Styles
BASE_STYLE = {  # APLICA_A_TODO
    "font_family": Font.DEFAULT.value, # referecia a las fuentes
    "font_weight": FontWeight.LIGHT.value, # peso de la fuente
    "background_color": Color.BACKGROUND.value, # color fondo
    rx.heading:{ # cabecera web
        "color": TextColor.TXTHEADER.value, # referencia color txt
        "font_family": Font.TITLE.value, # referencia fuente
        "font_weight": FontWeight.MEDIUM.value  # peso de la fuente
    },
    rx.button: { # td botones aplicación cogeran este estilo
        "width": "100%",
        "height": "100%",
        "padding": Size.SMALL.value,
        "border_radius": Size.DEFAULT.value,
        #"color": TextColor.TXTBOTOMPAUSE.value, # color texto botones
        "background_color": Color.BOTONPAUSA.value, # color fondo BOTON
        "white_space": "normal", # obliga txt pasar a 2lineas y no salga pantalla -> DESIGN-RESPONSIVE
        "text_align": "start", # alinear txt a izq.- DESIGN-RESPONSIVE
        "_hover": { # color BOTON evento pasar raton por encima
            "background_color": TextColor.TXTBOTOMPAUSE.value, # color fondo
            #"color": TextColor.TXTPRIMARY.value, # color texto botones
        }
    },
    rx.link: {
        "text_decoration": "none",  # desaparesca subrayadado de link
        "_hover": {}  # desaparesca subrayadado de link
    }
}

# Estilo de los TITULOS para NAVBAR
navbar_title_style= dict(
    #font_family="Comfortaa-Bold", # poniendole nombre fuente directa de google --> ya vale
    font_family=Font.LOGO.value, # cargamos fuente
    font_weight=FontWeight.MITAD.value, # peso de la fuente
    font_size=Size.LARGE.value # tamaño
)

# Estilo de los TITULOS - utilizado en separador de botones
title_style= dict(
    width="100%", # para que ocupe el máximo
    padding_top=Size.DEFAULT.value, # espacio para colocarlo mejor
    font_size=Size.LARGE.value # tamaño
)

# Diccionario de propiedades - TXT
button_title_style = dict( # TXT top boton
    font_family=Font.TITLE.value, # fuente
    font_weight=FontWeight.MEDIUM.value, # tamaño fuente
    font_size=Size.DEFAULT.value, # tamaño 
    color=TextColor.HOME.value # color texto TXTHEADER
)
button_body_style = dict( # TXXT bottom boton
    font_weight=FontWeight.LIGHT.value, # tamaño fuente
    font_size=Size.MEDIUM.value,  # tamaño 
    color=TextColor.TXTSECUNDY.value # color texto
)