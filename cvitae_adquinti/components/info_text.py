import reflex as rx
from cvitae_adquinti.styles.styles import Size
from cvitae_adquinti.styles.colors import TextColor

def info_text(title: str, body: str) -> rx.Component:
    return rx.center(
        rx.text(
            rx.text(
                title,
                as_="span",
                font_weight="bold",
                color=TextColor.TXTFOOTER.value,
            ),
            f" {body}",
            as_="span",
            font_size=Size.SLIM.value,
            color=TextColor.TXTCONTENT.value,
        ),
        align="center",
        justify="center",
        text_align="center"
    )
