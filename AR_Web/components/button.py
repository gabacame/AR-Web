import reflex as rx

class Button_State(rx.State):
    page: int = 1
 
    def default_state(self):
        self.page = 1

    def data_state(self):
        self.page = 2
 
    def fit_state(self):
        self.page = 3
 
    def predict_state(self):
        self.page = 4
        

def button(text:str, state_page:Button_State) -> rx.Component:
    return rx.button(
        text,
        bg="grey",
        width = "100%",
        align="center",
        on_click=state_page
    )