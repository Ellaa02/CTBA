import dash
from dash import Dash, dcc, html
import dash_bootstrap_components as dbc

##initialize the app
app = Dash(__name__ , use_pages = True, suppress_callback_exceptions=True, title = "Multi-Page-App")
server = app.server 

app.layout = html.Div([
    dbc.NavbarSimple(
    children =[
        dbc.Navlink('home',href='/', active = "exact"),
        dbc.Navlink('page 1',href='/page1', active = "exact"),
        dbc.Navlink('page 2',href='/page2', active = "exact"),
    ],
    brand = 'Multi-Page App'),
    dash.page_container
])


if __name__ == "__main__":
    app.run(debug=True)

