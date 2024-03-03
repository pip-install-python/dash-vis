import dash
from dash import html
from dash_extensions import DeferScript
import dash_mantine_components as dmc
from dash_iconify import DashIconify

page = dash.register_page(__name__, path="/")

layout = html.Div(
    [
        html.Center(html.H1("dash vis.js")),
        dmc.Grid(
            [
                dmc.Col(
                    [html.Div(id="mygraph"), html.Div(id="info")],
                    span=6,
                    style={
                        "display": "flex",
                        "justify-content": "center",
                        "align-items": "center",
                    },
                ),
                dmc.Col(
                    dmc.Group(
                        [
                            html.A(
                                dmc.Button("Explore", color="green"), href="/graph3d"
                            ),
                            html.A(
                                dmc.Button(
                                    "GitHub",
                                    leftIcon=DashIconify(icon="line-md:github-loop"),
                                ),
                                href="https://github.com",
                            ),
                        ]
                    ),
                    span=6,
                ),
                dmc.Col(
                    html.Div(
                        id="visualization",
                        style={
                            "width": "100%",
                        },
                    ),
                    span=6,
                ),
                dmc.Col(
                    dmc.Group(
                        [
                            html.A(
                                dmc.Button("Explore", color="green"), href="/timeline"
                            ),
                            html.A(
                                dmc.Button(
                                    "GitHub",
                                    leftIcon=DashIconify(icon="line-md:github-loop"),
                                ),
                                href="https://github.com",
                            ),
                        ]
                    ),
                    span=6,
                ),
                dmc.Col(
                    span=6,
                    children=[
                        html.Div(id="2dvisualization"),
                    ],
                ),
                dmc.Col(
                    dmc.Group(
                        [
                            html.A(
                                dmc.Button("Explore", color="green"), href="/graph2d"
                            ),
                            html.A(
                                dmc.Button(
                                    "GitHub",
                                    leftIcon=DashIconify(icon="line-md:github-loop"),
                                ),
                                href="https://github.com",
                            ),
                        ]
                    ),
                    span=6,
                ),
                dmc.Col(
                    span=6,
                    children=[
                        html.Div(id="mynetwork", style={"width": "100%"}),
                    ],
                ),
                dmc.Col(
                    dmc.Group(
                        [
                            html.A(
                                dmc.Button("Explore", color="green"), href="/network"
                            ),
                            html.A(
                                dmc.Button(
                                    "GitHub",
                                    color="black",
                                    leftIcon=DashIconify(icon="line-md:github-loop"),
                                ),
                                href="https://github.com",
                            ),
                        ]
                    ),
                    span=6,
                ),
            ],
            grow=True,
            m=6,
            gutterSm=12,
            gutter="md",
        ),
        DeferScript(src="assets/timeline/vistimeline.js"),
        DeferScript(src="assets/graph3d/zzz_visgraph3d.js"),
        DeferScript(src="assets/graph2d/basic_example.js"),
        DeferScript(src="assets/network/node_circular_imgs.js"),
    ]
)
