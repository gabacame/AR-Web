import reflex as rx

def uploadbar() -> rx.Component:
    return  rx.upload(
                rx.text(
                    "Drag and drop your csv files here or click to select files"
                ),
                id="my_upload",
                border="1px dotted rgb(107,99,246)",
                padding="5em",
        )  