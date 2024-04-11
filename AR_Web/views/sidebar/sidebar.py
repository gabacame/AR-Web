import reflex as rx
from AR_Web.styles import styles
from AR_Web.components.button import button


def sidebar() -> rx.Component:
    return rx.vstack(
        rx.heading("Options", margin_bottom="1em"),
##############-SIDE BAR PARTS-#######################
        button("Data","/manage_data"),
        button("Fit","/fit_page"),
        button("Predict","/predict_page"),
######################################################        
        position="fixed",
        height="100%",
        left="0px",
        top="0px",
        z_index="5",
        padding_x="2em",
        padding_y="1em",
        background_color="lightgray",
        align_items="left",
        width="175px",
    )