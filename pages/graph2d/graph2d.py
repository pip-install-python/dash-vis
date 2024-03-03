import json
import os
import dash
from dash import html
from dash_extensions import DeferScript
import dash_mantine_components as dmc
from dash_iconify import DashIconify

page = dash.register_page(__name__, path="/graph2d")

layout = html.Div(
    [
        html.Center(html.H3("dash graph2d vis.js")),
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
                                                    id="card_graph2d_simulator",
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
                                                    id="card_graph2d_js",
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
                                                                    id="2dvisualization"
                                                                ),
                                                            ]
                                                        ),
                                                        dmc.Space(h=20),
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
    'https://unpkg.com/vis@4.20.0/dist/vis-timeline-graph2d.min.css'
],
external_scripts=[
    'https://unpkg.com/vis@4.20.0/dist/vis-timeline-graph2d.min.js',
],
assets_url_path="assets",
use_pages=True,
server=server)

layout = html.Div([
    html.Div(id='2dvisualization'),

    DeferScript(src='assets/graph2d/basic_example.js'),
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
                        DeferScript(src="assets/graph2d/basic_example.js"),
                    ],
                ),
                id="card_display_graph2d",
                span=6,
            ),
            grow=True,
        ),
    ]
)


@dash.callback(
    dash.Output("card_display_graph2d", "children"),
    dash.Input("card_graph2d_simulator", "n_clicks"),
    dash.Input("card_graph2d_js", "n_clicks"),
)
def return_timeline(card_graph2d_simulator, card_graph2d_js):
    if card_graph2d_simulator % 2 == 0:
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
                                                        html.Div(id="2dvisualization"),
                                                        dmc.Space(h=20),
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
    'https://unpkg.com/vis@4.20.0/dist/vis-timeline-graph2d.min.css'
],
external_scripts=[
    'https://unpkg.com/vis@4.20.0/dist/vis-timeline-graph2d.min.js',
],
assets_url_path="assets",
use_pages=True,
server=server)

layout = html.Div([
    html.Div(id='2dvisualization'),

    DeferScript(src='assets/graph2d/basic_example.js'),
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
                        DeferScript(src="assets/graph2d/basic_example.js"),
                    ],
                ),
            ],
            id="card_display_graph3d",
        )
    elif card_graph2d_js % 2 == 0:
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
                                                    id="card_graph2d_simulator",
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
                                                    id="card_graph2d_js",
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
var container = document.getElementById("2dvisualization");
var label1 = {
  content: "Label 1 (with offset)",
  xOffset: 20,
  yOffset: 20,
};

var label2 = {
  content: "Label 2",
  className: "red",
};

var label3 = {
  content: "Label 3",
};
var items = [
  { group: 1, x: "2014-06-11", y: 10, label: label1 },
  { group: 1, x: "2014-06-12", y: 25, label: label2 },
  { group: 1, x: "2014-06-13", y: 30 },
  { group: 1, x: "2014-06-14", y: 10 },
  { group: 1, x: "2014-06-15", y: 15, label: label3 },
  { group: 1, x: "2014-06-16", y: 30 },

  { group: 2, x: "2014-06-17", y: 10, label: label1 },
  { group: 2, x: "2014-06-18", y: 25, label: label2 },
  { group: 2, x: "2014-06-19", y: 30 },
  { group: 2, x: "2014-06-20", y: 10 },
  { group: 2, x: "2014-06-21", y: 15, label: label3 },
  { group: 2, x: "2014-06-22", y: 30 },

  { group: 3, x: "2014-06-23", y: 10, label: label1 },
  { group: 3, x: "2014-06-24", y: 25, label: label2 },
  { group: 3, x: "2014-06-25", y: 30 },
  { group: 3, x: "2014-06-26", y: 10 },
  { group: 3, x: "2014-06-27", y: 15, label: label3 },
  { group: 3, x: "2014-06-28", y: 30 },
];

var groups = new vis.DataSet();
groups.add({
  id: 1,
  content:
    "Only draw items with labels. Make the data point bigger and a square.",
  options: {
    drawPoints: function group1Renderer(item, group, grap2d) {
      if (item.label == null) {
        return false;
      }
      return {
        style: "square",
        size: 15,
      };
    },
  },
});

groups.add({
  id: 2,
  content:
    "Draw according to the Graph2d callback, but make it every datapoint square one.",
  options: {
    drawPoints: {
      style: "square",
    },
  },
});

groups.add({
  id: 3,
  content:
    "I want to render datapoints with no labels. Screw the graph2d options. Except the style/size should be according to the graph2d option.",
  options: {
    drawPoints: function (item, group, grap2d) {
      return item.label == null;
    },
  },
});

var dataset = new vis.DataSet(items);
var options = {
  start: "2014-06-10",
  end: "2014-06-29",
  style: "bar",
  drawPoints: {
    onRender: function (item, group, grap2d) {
      return item.label != null;
    },
    style: "circle",
  },
};

var graph2d = new vis.Graph2d(container, dataset, groups, options);

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
            id="card_display_graph2d",
        )
    else:
        return dash.no_update
