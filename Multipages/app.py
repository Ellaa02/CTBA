import dash
from dash import Dash, dcc, html
import dash_bootstrap_components as dbc

##initialize the app
app = Dash(__name__ , use_pages = True, suppress_callback_exceptions=True, title = "Multi-Page-App")
server = app.server 

app.layout = html.Div([
    dbc.NavbarSimple(
    children =[
        dbc.NavLink('home',href='/', active = "exact"), #navigation only on app.py - create a hyperlink that lead to each page
        dbc.NavLink('page 1',href='/page1', active = "exact"),
        dbc.NavLink('page 2',href='/page2', active = "exact"),
        dbc.NavLink('page 3',href='/page3', active = "exact"),
    ],
    brand = 'Multi-Page App'),
    dash.page_container
])


if __name__ == "__main__":
    app.run(debug=True)

