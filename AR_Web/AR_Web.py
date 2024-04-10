from rxconfig import config
from AR_Web.components.navbar import navbar
from AR_Web.views.sidebar.sidebar import sidebar
from AR_Web.views.content.content import content
import reflex as rx


def index() -> rx.Component:
    return rx.fragment(
        sidebar(),
        navbar(),
        rx.container(
            content(),
            max_width="60em",
            margin_left="180px",
            padding="2em",
        )


    )


app = rx.App()
app.add_page(index)
