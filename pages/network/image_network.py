import dash
from dash import html
from dash_extensions import DeferScript
import dash_mantine_components as dmc
from dash_iconify import DashIconify

page = dash.register_page(__name__, path="/network")

layout = html.Div(
    [
        html.Center(html.H3("dash network vis.js")),
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
                                                    id="card_network_simulator",
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
                                                    id="card_network_js",
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
                                                                html.Div(
                                                                    id="mynetwork",
                                                                    style={
                                                                        "width": "100%"
                                                                    },
                                                                ),
                                                            ]
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
    https://unpkg.com/vis@4.20.0/dist/vis-network.min.css'
],
external_scripts=[
    'https://unpkg.com/vis-network/standalone/umd/vis-network.min.js',
],
assets_url_path="assets",
use_pages=True,
server=server)

layout = html.Div([
    html.Div(id='2dvisualization'),

    DeferScript(src='assets/network/node_circular_imgs.js'),
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
                        DeferScript(src="assets/network/node_circular_imgs.js"),
                    ],
                ),
                id="card_display_network",
                span=6,
            ),
            grow=True,
        ),
    ]
)


@dash.callback(
    dash.Output("card_display_network", "children"),
    dash.Input("card_network_simulator", "n_clicks"),
    dash.Input("card_network_js", "n_clicks"),
)
def return_timeline(card_network_simulator, card_network_js):
    if card_network_simulator % 2 == 0:
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
                                                    id="card_network_simulator",
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
                                                    id="card_network_js",
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
                                                            id="mynetwork",
                                                            style={"width": "100%"},
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
    'https://unpkg.com/vis@4.20.0/dist/vis-network.min.css'
],
external_scripts=[
    'https://unpkg.com/vis-network/standalone/umd/vis-network.min.js',
],
assets_url_path="assets",
use_pages=True,
server=server)

layout = html.Div([
    html.Div(id='mynetwork'),

    DeferScript(src='assets/network/node_circular.js'),
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
                        DeferScript(src="assets/network/node_circular_imgs.js"),
                    ],
                ),
            ],
            id="card_display_network",
        )
    elif card_network_js % 2 == 0:
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
                                                    id="card_network_simulator",
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
                                                    id="card_network_js",
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
var DIR = "assets/network/imgs/";

var nodes = null;
var edges = null;
var network = null;

// Called when the Visualization API is loaded.
function draw() {
  // create people.
  // value corresponds with the age of the person
  var DIR = "assets/network/imgs/";
  nodes = [
    { id: 1, shape: "circularImage", image: DIR + "duck.png" },
    { id: 2, shape: "circularImage", image: DIR + "yellow.png" },
    { id: 3, shape: "circularImage", image: DIR + "duck.png" },
    { id: 4, shape: "circularImage", image: DIR + "pip.png", label: "pictures by this guy!",},
    { id: 5, shape: "circularImage", image: DIR + "red.png" },
    { id: 6, shape: "circularImage", image: DIR + "rain.png" },
    { id: 7, shape: "circularImage", image: DIR + "site_shadow.png" },
    { id: 8, shape: "circularImage", image: DIR + "pirate.png" },
    { id: 9, shape: "circularImage", image: DIR + "base.png" },
    { id: 10, shape: "circularImage", image: DIR + "duck.png" },
    { id: 11, shape: "circularImage", image: DIR + "duck.png" },
    { id: 12, shape: "circularImage", image: DIR + "duck.png" },
    { id: 13, shape: "circularImage", image: DIR + "duck.png" },
    { id: 14, shape: "circularImage", image: DIR + "duck.png" },
    {
      id: 15,
      shape: "circularImage",
      image: DIR + "missing.png",
      brokenImage: DIR + "missingBrokenImage.png",
      label: "when images\nfail\nto load",
    },
    {
      id: 16,
      shape: "circularImage",
      image: DIR + "anotherMissing.png",
      brokenImage: DIR + "duck.png",
      label: "fallback image in action",
    },
  ];

  // create connections between people
  // value corresponds with the amount of contact between two people
  edges = [
    { from: 1, to: 2 },
    { from: 2, to: 3 },
    { from: 2, to: 4 },
    { from: 4, to: 5 },
    { from: 4, to: 10 },
    { from: 4, to: 6 },
    { from: 6, to: 7 },
    { from: 7, to: 8 },
    { from: 8, to: 9 },
    { from: 8, to: 10 },
    { from: 10, to: 11 },
    { from: 11, to: 12 },
    { from: 12, to: 13 },
    { from: 13, to: 14 },
    { from: 9, to: 16 },
  ];

  // create a network
  var container = document.getElementById("mynetwork");
  var data = {
    nodes: nodes,
    edges: edges,
  };
  var options = {
    nodes: {
      borderWidth: 4,
      size: 30,
      color: {
        border: "#222222",
        background: "#666666",
      },
      font: { color: "#eeeeee" },
    },
    edges: {
      color: "lightgray",
    },
  };
  network = new vis.Network(container, data, options);
}


draw();
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
                                                                "height": "100%",
                                                                "width": "100%",
                                                                # 'overflow-x': 'scroll',  # 'hidden' or 'scroll'
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
            id="card_display_network",
        )
    else:
        return dash.no_update
