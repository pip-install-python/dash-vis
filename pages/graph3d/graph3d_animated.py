import json
import os
import dash
from dash import html
from dash_extensions import DeferScript
import dash_mantine_components as dmc
from dash_iconify import DashIconify

page = dash.register_page(__name__, path="/graph3d")

layout = html.Div(
    [
        html.Center(html.H3("dash vis.js")),
        dmc.Grid(
            dmc.Col(
                dmc.MantineProvider(
                    theme={"colorScheme": "dark"},
                    children=[
                        dmc.Paper(
                            [
                                dmc.Space(h=10),
                                dmc.Group(
                                    [
                                        dmc.Tooltip(
                                            label="Simulator",
                                            position="bottom",
                                            offset=3,
                                            children=[
                                                dmc.ActionIcon(
                                                    DashIconify(
                                                        icon="logos:python",
                                                        width=30,
                                                    ),
                                                    variant="transparent",
                                                    id="card_graph3d_simulator",
                                                    n_clicks=1,
                                                )
                                            ],
                                        ),
                                        dmc.Tooltip(
                                            label="Javascript",
                                            position="bottom",
                                            offset=3,
                                            children=[
                                                dmc.ActionIcon(
                                                    DashIconify(
                                                        icon="skill-icons:javascript",
                                                        width=30,
                                                    ),
                                                    color="blue",
                                                    variant="transparent",
                                                    id="card_graph3d_js",
                                                    n_clicks=1,
                                                ),
                                            ],
                                        ),
                                    ],
                                    position="center",
                                ),
                                html.Hr(),
                                html.Div(
                                    [
                                        dmc.Container(
                                            [
                                                html.Div(
                                                    [
                                                        html.Div(
                                                            [
                                                                html.Div(id="mygraph"),
                                                                html.Div(id="info"),
                                                            ],
                                                            style={
                                                                "display": "flex",
                                                                "justify-content": "center",
                                                                "align-items": "center",
                                                            },
                                                        ),
                                                        dmc.Space(h=10),
                                                        html.Div(
                                                            [
                                                                dmc.Prism(
                                                                    """
import dash
from dash import html
from flask import Flask

server = Flask(__name__)

app = dash.Dash(__name__,
external_stylesheets=[
    "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css",
],
external_scripts=[
    'https://unpkg.com/vis-graph3d@latest/dist/vis-graph3d.min.js',
],
assets_url_path="assets",
use_pages=True,
server=server)

layout = html.Div([
    html.Div([
        html.Div(id='mygraph'),
        html.Div(id='info')
    ]),

    DeferScript(src='assets/zzz_visgraph3d.js'),
    ]
)

if __name__ == "__main__":
    app.run_server(port=43932, debug=True)
                                                                """,
                                                                    language="python",
                                                                    colorScheme="dark",
                                                                ),
                                                            ],
                                                            style={
                                                                "margin": 0,
                                                                "padding": 0,
                                                                "position": "relative",
                                                                "top": -20,
                                                                "height": "100%",
                                                                "width": "100%",
                                                                # 'overflow-x': 'scroll',  # 'hidden' or 'scroll'
                                                            },
                                                        ),
                                                    ]
                                                ),
                                            ]
                                        )
                                    ],
                                    style={"padding": "20px"},
                                ),
                            ]
                        ),
                        DeferScript(src="assets/graph3d/zzz_visgraph3d.js"),
                    ],
                ),
                id="card_display_graph3d",
                span=6,
            ),
            grow=True,
        ),
    ]
)


@dash.callback(
    dash.Output("card_display_graph3d", "children"),
    dash.Input("card_graph3d_simulator", "n_clicks"),
    dash.Input("card_graph3d_js", "n_clicks"),
)
def return_timeline(card_vistimeline_simulator, card_vistimeline_js):
    if card_vistimeline_simulator % 2 == 0:
        return html.Div(
            [
                dmc.MantineProvider(
                    theme={"colorScheme": "dark"},
                    children=[
                        dmc.Paper(
                            [
                                dmc.Space(h=10),
                                dmc.Group(
                                    [
                                        dmc.Tooltip(
                                            label="Simulator",
                                            position="bottom",
                                            offset=3,
                                            children=[
                                                dmc.ActionIcon(
                                                    DashIconify(
                                                        icon="logos:python",
                                                        width=30,
                                                    ),
                                                    variant="transparent",
                                                    id="card_graph3d_simulator",
                                                    n_clicks=1,
                                                )
                                            ],
                                        ),
                                        dmc.Tooltip(
                                            label="Javascript",
                                            position="bottom",
                                            offset=3,
                                            children=[
                                                dmc.ActionIcon(
                                                    DashIconify(
                                                        icon="skill-icons:javascript",
                                                        width=30,
                                                    ),
                                                    color="blue",
                                                    variant="transparent",
                                                    id="card_graph3d_js",
                                                    n_clicks=1,
                                                ),
                                            ],
                                        ),
                                    ],
                                    position="center",
                                ),
                                html.Hr(),
                                html.Div(
                                    [
                                        dmc.Container(
                                            [
                                                html.Div(
                                                    [
                                                        html.Div(
                                                            [
                                                                html.Div(id="mygraph"),
                                                                html.Div(id="info"),
                                                            ]
                                                        ),
                                                        html.Div(
                                                            [
                                                                dmc.Prism(
                                                                    """
import dash
from dash import html
from flask import Flask

server = Flask(__name__)

app = dash.Dash(__name__,
external_stylesheets=[
    "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css",
    'https://unpkg.com/vis-timeline@latest/styles/vis-timeline-graph2d.min.css'
],
external_scripts=[
    'https://unpkg.com/vis-timeline@latest/standalone/umd/vis-timeline-graph2d.min.js',
],
assets_url_path="assets",
use_pages=True,
server=server)

layout = html.Div([
    html.Div([
        html.Div(id='mygraph'),
        html.Div(id='info')
    ]),

    DeferScript(src='assets/zzz_visgraph3d.js'),
    ]
)

if __name__ == "__main__":
    app.run_server(port=43932, debug=True)
                                                                """,
                                                                    language="python",
                                                                    colorScheme="dark",
                                                                ),
                                                            ],
                                                            style={
                                                                "margin": 0,
                                                                "padding": 0,
                                                                "position": "relative",
                                                                "top": -20,
                                                                "height": "100%",
                                                                "width": "100%",
                                                                # 'overflow-x': 'scroll',  # 'hidden' or 'scroll'
                                                            },
                                                        ),
                                                    ]
                                                ),
                                            ]
                                        )
                                    ],
                                    style={"padding": "20px"},
                                ),
                            ]
                        ),
                        DeferScript(src="assets/graph3d/zzz_visgraph3d.js"),
                    ],
                ),
            ],
            id="card_display_graph3d",
        )
    elif card_vistimeline_js % 2 == 0:
        return html.Div(
            [
                dmc.MantineProvider(
                    theme={"colorScheme": "dark"},
                    children=[
                        dmc.Paper(
                            [
                                dmc.Space(h=10),
                                dmc.Group(
                                    [
                                        dmc.Tooltip(
                                            label="Simulator",
                                            position="bottom",
                                            offset=3,
                                            children=[
                                                dmc.ActionIcon(
                                                    DashIconify(
                                                        icon="logos:python",
                                                        width=30,
                                                    ),
                                                    variant="transparent",
                                                    id="card_graph3d_simulator",
                                                    n_clicks=1,
                                                )
                                            ],
                                        ),
                                        dmc.Tooltip(
                                            label="Javascript",
                                            position="bottom",
                                            offset=3,
                                            children=[
                                                dmc.ActionIcon(
                                                    DashIconify(
                                                        icon="skill-icons:javascript",
                                                        width=30,
                                                    ),
                                                    color="blue",
                                                    variant="transparent",
                                                    id="card_graph3d_js",
                                                    n_clicks=1,
                                                ),
                                            ],
                                        ),
                                    ],
                                    position="center",
                                ),
                                html.Hr(),
                                html.Div(
                                    [
                                        dmc.Container(
                                            [
                                                html.Div(
                                                    [
                                                        html.Div(
                                                            [
                                                                dmc.Prism(
                                                                    """
                                                    document.addEventListener("DOMContentLoaded", function() {
                                                        setTimeout(drawVisualization, 1000); // Delay for 1 second
                                                        var data = null;
                                                        var graph = null;

                                                        function custom(x, y, t) {
                                                          return Math.sin(x / 50 + t / 10) * Math.cos(y / 50 + t / 10) * 50 + 50;
                                                        }

                                                        // Called when the Visualization API is loaded.
                                                        function drawVisualization() {
                                                          // Create and populate a data table.
                                                          data = new vis.DataSet();
                                                          // create some nice looking data with sin/cos
                                                          var steps = 25;
                                                          var axisMax = 314;
                                                          var tMax = 31;
                                                          var axisStep = axisMax / steps;
                                                          for (var t = 0; t < tMax; t++) {
                                                            for (var x = 0; x < axisMax; x += axisStep) {
                                                              for (var y = 0; y < axisMax; y += axisStep) {
                                                                var value = custom(x, y, t);
                                                                data.add([{ x: x, y: y, z: value, filter: t, style: value }]);
                                                              }
                                                            }
                                                          }

                                                          // specify options
                                                          var options = {
                                                            width: "600px",
                                                            height: "600px",
                                                            style: "surface",
                                                            showPerspective: true,
                                                            showGrid: true,
                                                            showShadow: false,
                                                            // showAnimationControls: false,
                                                            keepAspectRatio: true,
                                                            verticalRatio: 0.5,
                                                            animationInterval: 100, // milliseconds
                                                            animationPreload: true,
                                                          };

                                                          // create our graph
                                                          var container = document.getElementById("mygraph");
                                                          graph = new vis.Graph3d(container, data, options);
                                                        }

                                                        drawVisualization();
                                                    });
                                                                """,
                                                                    language="javascript",
                                                                    colorScheme="dark",
                                                                ),
                                                            ],
                                                            style={
                                                                "margin": 0,
                                                                "padding": 0,
                                                                "position": "relative",
                                                                "top": -20,
                                                                "height": "60vh",
                                                                "width": "100%",
                                                                "overflow-x": "scroll",  # 'hidden' or 'scroll'
                                                                "overflow-y": "scroll",
                                                            },
                                                        )
                                                    ]
                                                ),
                                            ]
                                        )
                                    ],
                                    style={"padding": "20px"},
                                ),
                            ]
                        ),
                    ],
                ),
            ],
            id="card_display_graph3d",
        )
    else:
        return dash.no_update
