import pandas as pd

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

import plotly.express as px
import plotly


df = pd.read_excel('Statistics.xlsx')

app = dash.Dash(__name__)
app.layout = html.Div([
        html.Div([
        html.Label(['Filter by: ']),
        dcc.Dropdown(
            id='dropdwn',
            options=[{'label': 'Past month', 'value': 'Pi month'},
                     {'label': 'Past 2 months', 'value': 'Pi 2 months'}],
            value='Pi month',
            multi=False,
            clearable=False,
            style={"width":"50%"},
        ),
    ]),
]),

html.Div([
    dcc.Graph(id='graph')
]),

@app.callback(
    Output(component_id='graph',component_property='figure')
    [Input(component_id='dropdwn',component_property='value')]
)

def update_graph(dropdwn):
    dff = df
    app=px.pie(
        data_frame=dff,
        names=dropdwn,
        hole=.3,
    )
    return (app)

plotly.offline.plot(app, filename="pichart.html")

app.run_server(debug=True)
