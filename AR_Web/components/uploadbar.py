import reflex as rx

class State(rx.State):
    img: list[str]
    
    async def handle_upload(self, files: list[rx.UploadFile]):
        for file in files:
            if file.content_type == "text/csv":
                upload_data = await file.read()
                outfile = rx.get_upload_dir() / file.filename
                with outfile.open("wb") as file_object:
                    file_object.write(upload_data)
                self.img.append(file.filename)

def uploadbar() -> rx.Component:
    return rx.vstack(
        rx.upload(
            rx.text("Draggin to upload your CSV here"),
            id="upload_csv",
            border="1px dotted rgb(107,99,246)",
            padding="5em",
            on_drop=State.handle_upload(rx.upload_files(upload_id="upload_csv")),
        ),
        rx.foreach(State.img, lambda img: rx.text(img)),
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