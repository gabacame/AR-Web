import reflex as rx
import pandas as pd
from AR_Web.components.uploadbar import State


def graph() -> rx.Component:
    data_csv=pd.read_csv(f"uploaded_files/{State.actual_dataset}")
    data=data_csv.to_dict(orient='records')
    return rx.recharts.scatter_chart(
        rx.recharts.scatter(
        data=data,
        fill="#8884d8",
    ),
    rx.recharts.x_axis(data_key="x", type_="number"),
    rx.recharts.y_axis(data_key="y"),
)