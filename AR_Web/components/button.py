import reflex as rx
import os 

def button(text:str,root:str) -> rx.Component:
    return rx.button(
        text,
        bg="grey",
        width = "100%",
        align="center",
        on_click=rx.redirect(root)
    )

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

# Example of usage:
# delete_file('path_to_your_folder', 'your_file_name.txt')


def delete_button(file_name) -> rx.Component:
    return rx.button(
        "Delete",
        bg="red",
        width = "100%",
        align="center",
        on_click=delete_file('uploaded_file',file_name)
    )