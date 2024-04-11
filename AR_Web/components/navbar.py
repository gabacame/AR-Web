import reflex as rx
from AR_Web.styles import styles



def navbar() -> rx.Component:
    return rx.center(
        rx.button("Auto Regression Web",
                align="center",
                color="white",
                bg="grey",
                on_click=rx.redirect('/')
        ),
        position="sticky",
        align="center",
        bg="grey"
        )

    