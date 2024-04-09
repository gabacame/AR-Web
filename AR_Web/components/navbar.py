import reflex as rx
from AR_Web.styles import styles


def navbar() -> rx.Component:
    return rx.center(
        rx.text("Auto Regression Web",
                align="center",
                color="white"),
        position="sticky",
        align="center",
        bg="grey"
        )

    