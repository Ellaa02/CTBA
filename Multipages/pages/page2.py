import dash
from dash import html, dcc, callback, Output, Input, register_page
import requests


dash.register_page(__name__, path = '/page2', name = "Page 2")

layout = html.Div([
    html.H2("Page 2", className= "page-title"),
    html.P("Click to fetch a random cat fact from a public API"),
    html.Button("Get Cat Fact", id = "bin-cat", n_clicks=0),
    dcc.Loading(html.Div(id="cat-fact"))
], className = "page2-wrap")

@callback(
    Output("cat-fact", "children"),
    Input("bin-cat", "n_clicks"),

)

def get_cat_fact(n):
    try:
        r = requests.get("https://catfact.ninja/fact", timeout=5)
        r.raise_for_status()
        fact = r.json().get("fact", "No fact found.")
        return html.Div(fact)
    except requests.RequestException as e:
        return html.Div(f"Error contacting API: {e}")
    

