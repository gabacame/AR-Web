import reflex as rx

def manage() -> rx.Component:
    return rx.box(
        rx.heading("MANAGE DATA PAGE"),
        rx.text("""In this page you'll be able to manage your data."""),
    )