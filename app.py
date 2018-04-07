# -*- coding: utf-8 -*-
import dash
# Higher level UI components (JS, HTML, CSS - via React.js)
import dash_core_components as dcc
# HTML elements (every html tag)
import dash_html_components as html
import pandas as pd

df = pd.read_csv(
    'https://gist.githubusercontent.com/chriddyp/'
    'c78bf172206ce24f77d6363a2d754b59/raw/'
    'c353e8ef842413cae56ae3920b8fd78468aa4cb2/'
    'usa-agricultural-exports-2011.csv')


def generate_table(dataframe, max_rows=10):
    return html.Table(
        # Header
        [html.Tr([html.Th(col) for col in dataframe.columns])] +

        # Body
        [html.Tr([
            html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
        ]) for i in range(min(len(dataframe), max_rows))]
    )

markdown_text = '''
### Dash and Markdown

Dash apps can be written in Markdown.
Dash uses the [CommonMark](http://commonmark.org/)
specification of Markdown.
Check out their [60 Second Markdown Tutorial](http://commonmark.org/help/)
if this is your first introduction to Markdown!
'''

# Colors dict referenced at various points in 'styles' below
colors = {
    "background" : "#111111",
    "text" : "#7FDBFF"
}

# App
app = dash.Dash()

# Tree of components - root is html.Div
# Notice 'styles' littered throughout
app.layout = html.Div(style={"backgroundColor" : colors["background"]}, children=[
    html.H1(
        children='Hello Dash',
        style = {
            "textAlign" : "center",
            "color" : colors["text"]
        }
    ),

    html.Div(
        children="Dash: A web application framework for Python.",
        style={
            "textAlign" : "center",
            "color" : colors["text"]
        }
    ),

    # Graph (from dcc) renders plotly objects (interactive)
    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
            ],
            'layout': {
                "plot_bgcolor" : colors["background"],
                "paper_bgcolor" : colors["background"],
                "font" : {
                    "color" : colors["text"]
                },
                'title': 'Dash Data Visualization'
            }
        }
    ),

    html.H4(
        children="US Agriculture Exports (2011)",
        style={
            "color" : colors["text"]
        }
    ),

    generate_table(df),

    html.Div(dcc.Markdown(
        children=markdown_text
    ),
        style={
            "color": colors["text"],
            "align" : "center"
        }
    )
])

app.css.append_css({"external_url": "https://codepen.io/chriddyp/pen/bWLwgP.css"})

if __name__ == '__main__':
    app.run_server(debug=True)