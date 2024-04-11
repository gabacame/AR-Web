import reflex as rx


def button(text:str,root:str) -> rx.Component:
    return rx.button(
        text,
        bg="grey",
        width = "100%",
        align="center",
        on_click=rx.redirect(root)
    )



