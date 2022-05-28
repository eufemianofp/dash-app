from dash import dcc, html, Input, Output, callback

layout = html.Div([
    html.H3('Page 1'),
    dcc.Dropdown(
        options={
            city.lower(): city
            for city in ['New York City', 'Montreal', 'Los Angeles']
        },
        id='page-1-dropdown',
        multi=True,
    ),
    html.Div(id='page-1-display-value'),
    dcc.Link('Go to Page 2', href='/page2'),
    html.Br(),
    dcc.Link('Go to Home', href='/'),
])


@callback(
    Output('page-1-display-value', 'children'),
    Input('page-1-dropdown', 'value'))
def display_value(value):
    return f'You have selected {value}'
