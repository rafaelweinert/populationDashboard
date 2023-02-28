import pandas as pd
import numpy as np
import plotly.express as px
from dash import Dash, html, dcc, Input, Output
from dash_bootstrap_components.themes import BOOTSTRAP
from src.components import ids, yearSlider, populationDropdown


population_path = 'data/API_SP.POP.TOTL_DS2_en_csv_v2_4898931.csv'

def load_population(path):

    data = pd.read_csv(path, sep=',', skiprows=4)
    return data


def create_layout(app: Dash) -> html.Div:
    population_data = load_population(population_path)
    years = [int(num) for num in population_data.columns if num.isnumeric()]


    return html.Div(
        className='app-div',
        children=[
            html.H1(app.title),
            populationDropdown.render(app),
            yearSlider.render(app, min(years), max(years)),
            create_map(app, population_data)
        ],
        style={'margin': 70}
    )



def create_map(app: Dash, data):
    @app.callback(
        Output(ids.MAP, 'children'),
        Input(ids.YEAR_SLIDER, 'value'),
        Input(ids.POPULATION_DROPDOWN, 'value')
    )
    def update_map(year, population_type):

        fig = px.choropleth(data, locations="Country Code",
                            color=str(year) if population_type=='Absolute values' else (data['2021'] / data[str(year)]),
                            hover_name="Country Name",  # column to add to hover information
                            color_continuous_scale=px.colors.sequential.Plasma,
                            height=800,
                            range_color=(0, 1500000000 if population_type=='Absolute values' else 30),)

        return html.Div(
            dcc.Graph(figure=fig), id=ids.MAP
        )

    return html.Div(id=ids.MAP)


def main() -> None:
    app = Dash(external_stylesheets=[BOOTSTRAP])
    server = app.server
    app.title = 'Dashboard'
    app.layout = create_layout(app)
    app.run()

if __name__ == '__main__':
    main()


