import reflex as rx

def predict() -> rx.Component:
    return rx.box(
        rx.heading("PREDICT PAGE"),
        rx.text("""In this page you'll be able to predict with your fitted models."""),
    )