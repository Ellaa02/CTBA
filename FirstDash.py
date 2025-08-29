from dash import Dash, html

## create a Dash app
app = Dash(__name__) # Dash() initialized your web application
app.title = "My First Dash App" # sets the title of the web page


app.layout = html.Div([
    html.H1("Hello Dash!", style = {"color" : "#081271",
                                    "fontSize" : "80px",
                                    "backgroundColor": "#858FE3"}), # html.H1 adds a header
    html.P("This is a simple dashboard.", style = {"border" : "1px solid black",
                                                   "borderRadius" : "10px",
                                                    "padding": "20px",
                                                    "margin" : "50px"}), # html.P adds a paragraph
    html.Br(), # html.br() adds a line break
    html.A("Click Here:",href = "https://plotly.com/dash/" ) # html.A adds a hyperlink
])

## run the app

if __name__ == "__main__": # ensures the server starts only when you run this file directly
    app.run(debug = True , use_reloader = False) 
    # app.run(…) starts the local server
    # debug=True will automatically refresh the app when you make changes to the code


