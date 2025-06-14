# LIBRERIA DE COLORES - https://htmlcolorcodes.com/es/nombres-de-los-colores/
from enum import Enum

class Color(Enum): # encapsulado colores importantes web
    BACKGROUND = "#FAFDFD" # azul casi Snow #FFFAFA
    # BOTON ESTADO
    BOTONPAUSA = "#FFFAFA" # boton pausa - MintCream
    HOME = "#087ec4" # raton sobre boton


class TextColor(Enum): # colores de textos
    PRIMARY = "#4682B4" # SteelBlue #4682B4
    HOME = "#087ec4" # azul
    TXTPRIMARY = "#F5FFFA" # txt boton raton por encima -MintCream
    TXTSECUNDY = "#9E9EE2" #  sombra claro de azul-magenta. - otro Lavender -> #E6E6FA
    TXTHEADER ="#1E90FF" # txt cabecera - DodgerBlue
    TXTCONTENT = "#000080"  # txt cuerpo - Navy
    TXTFOOTER = "#6A5ACD"  # txt pie pagina2 - SlateBlue
    TXTBOTOMPAUSE = "#003153" # Azul de Prusia