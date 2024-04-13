import reflex as rx
from AR_Web.components.uploadbar import State
from AR_Web.views.content.fit.models import params
from AR_Web.views.content.fit.graph import graph




def select_data() -> rx.Component:
    return rx.vstack(
        rx.form.root(
            rx.hstack(
                rx.select(
                    State.files,
                    default_value=State.files[0],
                    name="actual_dataset"
                ),
                rx.button("Submit", type="submit"),
            ),
            on_submit=State.handle_submit,
            reset_on_submit=True,
        )
        )



'''
def select_data() -> rx.Component:
    return rx.select.root(
    rx.select.trigger(),
    rx.select.content(
        rx.select.group(
            rx.select.label("Data sets"),
            rx.foreach(State.files,
                       lambda file:
                       rx.select.item(file,value=file)),
        ),
    ),
    default_value=State.files[0],
)
'''


    

def fit() -> rx.Component:
    return rx.vstack(
        rx.heading("FIT MODELS PAGE"),
        select_data(),
        rx.hstack(
        rx.box(
            rx.heading("Graph"),
            ####################
            #graph(),
            ####################
            padding_left="12px",
            padding_right="12px",
            background_color="var(--gray-2)",
        ),
        rx.box(
            rx.heading("Model parameters"),
            ##################
            params(),
            ###########
            padding_left="12px",
            padding_right="12px",
            background_color="var(--gray-2)",
        ),
        width="100%",
    )
    )