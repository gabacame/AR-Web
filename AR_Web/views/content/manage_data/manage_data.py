import reflex as rx
from AR_Web.components.uploadbar import upload_button
import os

def delete_file(folder_path, file_name):
    file_path = os.path.join(folder_path, file_name)
    
    if os.path.isfile(file_path):
        try:
            os.remove(file_path)
            print(f"File '{file_name}' successfully deleted from folder '{folder_path}'.")
        except Exception as e:
            print(f"An error occurred while trying to delete the file: {e}")
    else:
        print(f"File '{file_name}' does not exist in the folder '{folder_path}'.")

def list_files_in_folder(folder):
    files = [file for file in os.listdir(folder) if os.path.isfile(os.path.join(folder, file))]
    return files

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
                    rx.foreach(list_files_in_folder('uploaded_files'), 
                               lambda file: 
                               rx.table.row(
                                   rx.table.cell(file),
                                   rx.table.cell(
                                       rx.button("Delete",
                                            bg="red",
                                            align="center",
                                            
                                   ))
                                )
                    )
            )  
        ),   
    )

def manage_data() -> rx.Component:
    return rx.box(
        rx.heading("MANAGE DATA PAGE"),
##---Upload Button---##
    upload_button(),
##---Upload Button---##
##-------Table-------##
    table()
##-------Table-------##
    )