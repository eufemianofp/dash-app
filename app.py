from dash import Dash, dcc, html, Input, Output, callback
from pages import page1, page2


app = Dash(__name__, suppress_callback_exceptions=True)
server = app.server

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])


@callback(
    Output('page-content', 'children'),
    Input('url', 'pathname')
)
def display_page(pathname):
    if pathname == '/page1':
        return page1.layout
    elif pathname == '/page2':
        return page2.layout
    else:
        return html.Div(id='main-div', children=[
            html.H3('Home'),
            dcc.Link('Go to Page 1', href='/page1'),
            html.Br(),
            dcc.Link('Go to Page 2', href='/page2'),
        ])


if __name__ == '__main__':
    app.run_server(debug=True)
