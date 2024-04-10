import reflex as rx

def fit() -> rx.Component:
    return rx.box(
        rx.heading("FIT PAGE"),
        rx.text("""In this page you'll be able to fit your model."""),
    )