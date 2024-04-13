import reflex as rx
import os
from pathlib import Path

class State(rx.State):
    img: list[str]
    files:list[str]

    async def handle_upload(self, files: list[rx.UploadFile]):
        for file in files:
            if file.content_type == "text/csv":
                upload_data = await file.read()
                outfile = rx.get_upload_dir() / file.filename
                with outfile.open("wb") as file_object:
                    file_object.write(upload_data)
                self.img.append(file.filename)
                await self.list_files_in_folder()

    async def list_files_in_folder(self):
        self.files = [file for file in os.listdir('uploaded_files') if os.path.isfile(os.path.join('uploaded_files', file))]

    async def delete_file_from_folder(self, file_name: str):
        file_path = Path('uploaded_files') / file_name
        os.remove(file_path)
        await self.list_files_in_folder()

    actual_dataset:str
    actual_model:str

    def handle_submit(self, actual_dataset):
        self.actual_dataset= actual_dataset


def uploadbar() -> rx.Component:
    return rx.vstack(
        rx.upload(
            rx.text("Draggin to upload your CSV here"),
            id="upload_csv",
            border="1px dotted rgb(107,99,246)",
            padding="5em",
            on_drop=State.handle_upload(rx.upload_files(upload_id="upload_csv")),
        ),
        padding="5em",
    )

def upload_button() -> rx.Component:
    color = "rgb(107,99,246)"
    return rx.vstack(
            rx.upload(
                rx.button("Select File", color=color, bg="white", border=f"1px solid {color}"),
                id="upload1",
                padding="0.125em",
                on_drop=State.handle_upload(rx.upload_files(upload_id="upload_csv"))
            ),
        )
def refresh_button() -> rx.Component:
    return rx.button(
        "Refresh",
        on_click=State.list_files_in_folder()
    )

def delete_button(file_name) -> rx.Component:
    return rx.alert_dialog.root(
    rx.alert_dialog.trigger(
        rx.button("Delete", bg="red"),
    ),
    rx.alert_dialog.content(
        rx.alert_dialog.title("DELETE"),
        rx.alert_dialog.description(
            "Are you sure? This file will no longer be accessible.",
        ),
        rx.flex(
            rx.alert_dialog.cancel(
                rx.button("Cancel"),
            ),
            rx.alert_dialog.action(
                rx.button("Delete", bg="red", on_click=State.delete_file_from_folder(file_name)),
            ),
            spacing="3",
        ),
    ),
)