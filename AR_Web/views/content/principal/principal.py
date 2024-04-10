import reflex as rx
from AR_Web.components.uploadbar import uploadbar

def principal() -> rx.Component:
    return rx.box(
        rx.heading("Welcome to Auto Regression Web"),
        rx.text(f"""This page is for make regressions in automaticc way, 
                just draging your data here."""),
        #uploadbar()
    )