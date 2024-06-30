import os
from dash import Dash, html, dcc, callback, Input, Output, State
import dash_bootstrap_components as dbc
import dash


from embedchain import App

os.environ["OPENAI_API_KEY"] = "sk-proj-6kY8KkNOmPb5TvcWxK4KT3BlbkFJyY8T4YGVHbIvaqvjLetu"
ai_bot = App.from_config(config_path="config.yaml")


ai_bot.add("https://www.calendly.com/leadership")


app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = dbc.Container([
    dbc.Row([
        dbc.Col(html.H1('testBot'), width=12)
    ]),
    dbc.Row([
        dbc.Col(html.H3('ask anything about info you have provided'), width=12)
    ]),
    dbc.Row([
        dbc.Col([
            html.Label('Ask Away:'),
            dcc.Textarea(id='question-area', value='', style={'width': '100%', 'height': 100}),
            html.Br(),
            dbc.Button('Submit', id='submit-btn', color='primary'),
            html.Br(),
            dcc.Loading(id="load", children=html.Div(id='response-area')),
        ], width=12)
    ])
], fluid=True)



@callback(
    Output('response-area', 'children'),
    Input('submit-btn', 'n_clicks'),
    State('question-area', 'value'),
    prevent_initial_call=True
)
def create_response(_, question):
    answer = ai_bot.query(question)
    return answer


if __name__ == '__main__':
    app.run_server(debug=False)