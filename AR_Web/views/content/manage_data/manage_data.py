import reflex as rx
from AR_Web.components.uploadbar import upload_button, refresh_button, delete_button,State


def table() -> rx.Component:
    return rx.container(
        rx.table.root(
            rx.table.header(
                rx.table.row(
                    rx.table.column_header_cell("File"),
                    rx.table.column_header_cell("Delete")
                )
            ),
            rx.table.body(
                    rx.foreach(State.files, 
                               lambda file:
                               rx.table.row(
                                   rx.table.cell(file),
                                   rx.table.cell(
                                        delete_button(file))
                                )
                    )
            )  
        ),   
    )

def manage_data() -> rx.Component:
    return rx.box(
        rx.heading("MANAGE DATA PAGE"),
##---Upload Button---##
    rx.hstack(
        upload_button(),
        refresh_button()
    ),
##---Upload Button---##
##-------Table-------##
    table()
##-------Table-------##
    )