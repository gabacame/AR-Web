import reflex as rx
from AR_Web.styles import styles
from AR_Web.components.button import Button_State


def navbar() -> rx.Component:
    return rx.center(
        rx.button("Auto Regression Web",
                align="center",
                color="white",
                bg="grey",
                on_click=Button_State.default_state),
        position="sticky",
        align="center",
        bg="grey"
        )

    