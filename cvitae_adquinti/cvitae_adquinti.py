"""Web PORFOLIO proyecto reflex
utiliza componente de react y verdaderamente libreria de chakra """

import reflex as rx
import cvitae_adquinti.styles.styles as styles
from cvitae_adquinti.components.navbar import navbar
from cvitae_adquinti.views.header.header import header
from cvitae_adquinti.views.links.links import links
from cvitae_adquinti.components.footer import footer
from cvitae_adquinti.styles.styles import Size as Size

#class State(rx.State): # Debe estar aunque sea vacia - NO NECESARIO -
#    pass

def index() -> rx.Component:
    #index
    return rx.box(
        rx.script("document.documentElement.lang='es'"), # html -> meta spanish
        navbar(), # llamamos instancia navbar
        rx.center(
            rx.vstack( # bloque vertical principal
                header(), # cabecera (textos)
                links(), # botones
                max_width=styles.MAX_WIDTH, # archivo STYLES tamaño
                width="100%", # ocupe td espacio
                margin_y=Size.BIG.value, # margen arriba y abajo
                padding=Size.BIG.value
            )
        ), 
        footer() # (final pag)
    )


# Add state and page to the app.
app = rx.App(
    stylesheets=styles.STYLESHEETS,
    style=styles.BASE_STYLE,
    head_components=[
        rx.script(src="https://www.googletagmanager.com/gtag/js?id=G-3YGHT3XJFS"),
        rx.script(
            """ window.dataLayer = window.dataLayer || [];
            function gtag(){dataLayer.push(arguments);}
            gtag('js', new Date());
            gtag('config', 'G-3YGHT3XJFS');"""
        ),
    ],
) # carga lo q indiquemos para todos
app.add_page(
    index,
    title="AdQuinti - Porfolio",
    description="Docente de TI, conocimientos en Artificial Intelling (AI), Ciberseguridad, developer siteWeb, programador en backend y frontend, Java, Python, Reflex, Css3, Html5, SQL, MySQL, redes ...",
    image="avatar.jpg"
    ) # añade pag a aplicación
# ya no es necesaria COMPILE
#app.compile() 