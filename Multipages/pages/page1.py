import dash
from dash import html


dash.register_page(__name__, path = '/page1', name = "Page 1")

layout = html.Div([
    # Top row
    html.Div("Top(First Row)", className = "block block-top"),
    
    # Middle row - 2 Cols
    html.Div([
        html.Div("Middle left", className = "block"),
        html.Div("Middle right", className = "block"),
    ],
    className = "row-2"
    ),

    #Footer
    html.Div("Footer", className = "block block-footer")

], className = "page1-grid"
)