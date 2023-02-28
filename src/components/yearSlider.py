import pandas as pd
import numpy as np
import plotly.express as px
from dash import Dash, html, dcc, Input, Output
from dash_bootstrap_components.themes import BOOTSTRAP
from src.components import ids


def render(app:Dash, min_year, max_year):

    return html.Div(
        children=[
            html.H5('Year'),

            dcc.Slider(
                id=ids.YEAR_SLIDER,
                value=min_year,
                min=min_year,
                max=max_year,
                step=1,
                marks=None,
                tooltip={"placement": "bottom", "always_visible": True},
                updatemode='drag'
            ),
        ],
    )