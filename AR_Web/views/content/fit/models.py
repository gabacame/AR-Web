import reflex as rx
import pandas as pd
from sklearn.linear_model import LinearRegression


def params() -> rx.Component:
    return rx.button("Fit")