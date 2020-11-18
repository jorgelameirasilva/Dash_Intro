import dash 
import dash_html_components as html

app = dash.Dash()

app.layout = html.Div([
    html.H1("Title 1"),
    html.H2("Title 2"),
    html.H3("Title 3"),

    html.Button("Click me !!")
])



app.run_server(debug=True)


