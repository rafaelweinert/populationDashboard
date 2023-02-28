import pandas as pd
import numpy as np
import plotly.express as px
from dash import Dash, html, dcc, Input, Output
from dash_bootstrap_components.themes import BOOTSTRAP
from src.components import ids


def render(app:Dash):

    return html.Div(
        children=[
            html.H5('Year'),

            dcc.Dropdown(
                id=ids.POPULATION_DROPDOWN,
                options = ['Absolute values', 'Relative values (to most recent year)'],
                value='Absolute values'
            ),
        ],
    )