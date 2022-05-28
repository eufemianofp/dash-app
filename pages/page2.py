from dash import dcc, html, Input, Output, callback

layout = html.Div([
    html.H3('Page 2'),
    dcc.Dropdown(
        options={
            city.lower(): city
            for city in ['London', 'Berlin', 'Paris']
        },
        id='page-2-dropdown',
    ),
    html.Div(id='page-2-display-value'),
    dcc.Link('Go to Page 1', href='/page1'),
    html.Br(),
    dcc.Link('Go to Home', href='/'),
])


@callback(
    Output('page-2-display-value', 'children'),
    Input('page-2-dropdown', 'value'))
def display_value(value):
    return f'You have selected {value}'
