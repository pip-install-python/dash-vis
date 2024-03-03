import dash
from dash import (
    html,
)
from flask import Flask

server = Flask(__name__)

app = dash.Dash(__name__,
                external_stylesheets=[
                    "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css",
                    'https://unpkg.com/vis@4.20.0/dist/vis-network.min.css',
                    'https://unpkg.com/vis-timeline@latest/styles/vis-timeline-graph2d.min.css',

                ],
                external_scripts=[
                    'https://unpkg.com/vis@4.20.0/dist/vis-timeline-graph2d.min.js',
                    'https://unpkg.com/vis-network/standalone/umd/vis-network.min.js',
                    'https://unpkg.com/vis-timeline@latest/standalone/umd/vis-timeline-graph2d.min.js',
                    'https://unpkg.com/vis-graph3d@latest/dist/vis-graph3d.min.js',

                ],
                assets_url_path="assets",
                use_pages=True,
                server=server)

# App
app.layout = html.Div(
    [
        dash.page_container,
    ],
)

if __name__ == "__main__":
    app.run_server(port=43932, debug=True)

