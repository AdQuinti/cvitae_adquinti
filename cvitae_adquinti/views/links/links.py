import reflex as rx
import cvitae_adquinti.constants as const
from cvitae_adquinti.components.link_button import link_button as LB # boton creado importamos
from cvitae_adquinti.components.title import title # title creado importamos
from cvitae_adquinti.styles.styles import Size

def links() -> rx.Component:
    return rx.vstack(
#        title("Por las redes"),
#        LB("Linkedin", "Puedes consultar información sobre mí.", "icons/linkedin-in.svg", const.LINKEDIN_URL),
        #LB("GoogleSites", "CV en porfolio", "icons/google_site.svg", const.GOOGLE_SITES),
#        LB("X", "Consulta mis inquietudes y lo último que estoy haciendo", "icons/x.svg", const.TWITTER_X_URL),
#        LB("Threads", "Red Social", "icons/threads.svg", const.THREADS_URL),
        #LB("Instagram", "Red Social", "icons/instagram.svg", const.INSTAGRAM_URL),
        
#        title("Recursos"),
#        LB("Git y GitHub", "Aquí puedes encontrar mis trabajos realizados", "icons/github.svg", const.GITHUB_URL),
#        LB("Youtube", "Videos manuales", "icons/youtube.svg", const.YOUTUBE_URL),
#        LB("Youtube", "Videos - guías - todo lo que necesitas para aprender", "icons/youtube_old.svg", const.YOUTUBE_2URL),
#        LB("Facebook", "Red Social", "icons/facebook-f.svg", const.FACEBOOK_URL),
#        LB("Twitch", "Red Social", "icons/twitch.svg", const.TWITCH_URL),
        
        title("Contacto"),
        LB("Linkedin", "Puedes consultar información sobre mí.", "icons/linkedin-in.svg", const.LINKEDIN_URL),
#        LB("MyPublicInbox", "Respuesta rápida y con preferencia", "icons/checkemail.svg", const.MYPUBLICINBOX_URL),
        LB(
            "Email",
            const.EMAIL,
            "icons/email.svg",
            f"mailto:{const.EMAIL}"
        ),
        
        width="100%",
        spacing='1' #Size.MEDIUM.value 
        # espacio que dejamos entre cada uno componentes
    )