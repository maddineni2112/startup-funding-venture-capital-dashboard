# app.py
from dash import Dash, dcc, html, Input, Output
from layouts import (
    layout_main_page,
    layout_dashboard1,
    layout_dashboard2,
    layout_sheet1,
    layout_sheet2,
    layout_sheet3,
)
from callbacks import register_callbacks

app = Dash(__name__, suppress_callback_exceptions=True)

# Router wrapper layout
app.layout = html.Div(
    children=[
        dcc.Location(id="url"),
        html.Div(id="page-content"),
    ]
)

# Routing between pages
@app.callback(Output("page-content", "children"), Input("url", "pathname"))
def display_page(pathname):
    if pathname == "/dash1":
        return layout_dashboard1()
    elif pathname == "/dash2":
        return layout_dashboard2()
    elif pathname == "/sheet1":
        return layout_sheet1()
    elif pathname == "/sheet2":
        return layout_sheet2()
    elif pathname == "/sheet3":
        return layout_sheet3()
    else:
        return layout_main_page()


# Register all dynamic callbacks (dash1 + dash2)
register_callbacks(app)


if __name__ == "__main__":
    app.run(debug=True)
