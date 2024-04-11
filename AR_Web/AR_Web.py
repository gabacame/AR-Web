from rxconfig import config
from AR_Web.components.navbar import navbar
from AR_Web.views.sidebar.sidebar import sidebar
from AR_Web.views.content.principal.principal import principal
from AR_Web.views.content.manage_data.manage_data import manage_data
from AR_Web.views.content.fit.fit import fit
from AR_Web.views.content.predict.predict import predict
import reflex as rx

@rx.page(route="/index", title="Principal page")
def index() -> rx.Component:
    return rx.fragment(
        sidebar(),
        navbar(),
        rx.container(
            principal(),
            max_width="60em",
            margin_left="180px",
            padding="2em",
        )
    )

@rx.page(route="/manage_data", title="Manage data page")
def manage_page() -> rx.Component:
    return rx.fragment(
        sidebar(),
        navbar(),
        rx.container(
            manage_data(),
            max_width="60em",
            margin_left="180px",
            padding="2em",
        )
    )

@rx.page(route="/fit_page", title="Fitting data page")
def fit_page() -> rx.Component:
    return rx.fragment(
        sidebar(),
        navbar(),
        rx.container(
            fit(),
            max_width="60em",
            margin_left="180px",
            padding="2em",
        )
    )

@rx.page(route="/predict_page", title="Predict data page")
def predict_page() -> rx.Component:
    return rx.fragment(
        sidebar(),
        navbar(),
        rx.container(
            predict(),
            max_width="60em",
            margin_left="180px",
            padding="2em",
        )
    )

app = rx.App()