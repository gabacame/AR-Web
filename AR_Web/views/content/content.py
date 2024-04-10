import reflex as rx
from AR_Web.views.content.principal.principal import principal
from AR_Web.views.content.manage_data.manage_data import manage
from AR_Web.views.content.fit.fit import fit
from AR_Web.views.content.predict.predict import predict
from AR_Web.components.button import Button_State

def actual_content():
    if Button_State.page == 1:
        return principal()
    elif Button_State.page == 2:
        return manage()
    elif Button_State.page == 3:
        return fit()
    elif Button_State.page == 4:
        return predict()
    
def content() -> rx.Component:
    return rx.box(
        rx.text(f"State:{Button_State.page}")
    )