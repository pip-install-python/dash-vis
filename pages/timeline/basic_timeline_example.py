import dash
from dash import html
from dash_extensions import DeferScript
import dash_mantine_components as dmc
from dash_iconify import DashIconify

page = dash.register_page(__name__, path="/timeline")

layout = html.Div(
    [
        html.Center(html.H3("dash timeline vis.js")),
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
                                                    id="card_vistimeline_simulator",
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
                                                    id="card_vistimeline_js",
                                                    n_clicks=1,
                                                ),
                                            ],
                                        ),
                                        dmc.Tooltip(
                                            label="CSS",
                                            position="bottom",
                                            offset=3,
                                            children=[
                                                dmc.ActionIcon(
                                                    DashIconify(
                                                        icon="skill-icons:css",
                                                        width=30,
                                                    ),
                                                    color="blue",
                                                    variant="transparent",
                                                    id="card_vistimeline_css",
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
                                                # dmc.Title("Custom html.Wbr() Simulator", order=2),
                                                html.Div(
                                                    [
                                                        html.Div(
                                                            id="visualization",
                                                            style={
                                                                "width": "100%",
                                                                "height": "100%",
                                                            },
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
    html.Div(id='visualization',
                     style={'width': '100%', 'height': '100%'}),
    DeferScript(src='assets/timeline/vistimeline.js'),
])

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
                    ],
                ),
                id="card_display_vistimeline",
                span=6,
            ),
            grow=True,
        ),
        DeferScript(src="assets/timeline/vistimeline.js"),
    ]
)


@dash.callback(
    dash.Output("card_display_vistimeline", "children"),
    dash.Input("card_vistimeline_simulator", "n_clicks"),
    dash.Input("card_vistimeline_js", "n_clicks"),
    dash.Input("card_vistimeline_css", "n_clicks"),
)
def return_timeline(
    card_vistimeline_simulator, card_vistimeline_js, card_vistimeline_css
):
    print(card_vistimeline_simulator, card_vistimeline_js, card_vistimeline_css)
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
                                                    id="card_vistimeline_simulator",
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
                                                    id="card_vistimeline_js",
                                                    n_clicks=1,
                                                ),
                                            ],
                                        ),
                                        dmc.Tooltip(
                                            label="CSS",
                                            position="bottom",
                                            offset=3,
                                            children=[
                                                dmc.ActionIcon(
                                                    DashIconify(
                                                        icon="skill-icons:css",
                                                        width=30,
                                                    ),
                                                    color="blue",
                                                    variant="transparent",
                                                    id="card_vistimeline_css",
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
                                                            id="visualization",
                                                            style={
                                                                "width": "100%",
                                                                "height": "100%",
                                                            },
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
                        html.Div(id='visualization',
                                         style={'width': '100%', 'height': '100%'}),
                        DeferScript(src='assets/timeline/vistimeline.js'),
                    ])
            
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
                    ],
                ),
                DeferScript(src="assets/timeline/vistimeline.js"),
            ],
            id="card_display_vistimeline",
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
                                                    id="card_vistimeline_simulator",
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
                                                    id="card_vistimeline_js",
                                                    n_clicks=1,
                                                ),
                                            ],
                                        ),
                                        dmc.Tooltip(
                                            label="CSS",
                                            position="bottom",
                                            offset=3,
                                            children=[
                                                dmc.ActionIcon(
                                                    DashIconify(
                                                        icon="skill-icons:css",
                                                        width=30,
                                                    ),
                                                    color="blue",
                                                    variant="transparent",
                                                    id="card_vistimeline_css",
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
                                                                var container = document.getElementById("visualization");
            
                                                                // note that months are zero-based in the JavaScript Date object
                                                                var items = new vis.DataSet([
                                                                  {
                                                                    start: new Date(2024, 7, 23),
                                                                    content:
                                                                      '<div>Conversation</div><img src="https://icons.iconarchive.com/icons/iconfactory/looney/32/Madador-B-icon.png" style="width:32px; height:32px;">',
                                                                  },
                                                                  {
                                                                    start: new Date(2024, 7, 23, 23, 0, 0),
                                                                    content:
                                                                      '<div>Mail from boss</div><img src="https://cdn.wikimg.net/en/strategywiki/images/4/40/WD_Babasama.gif" style="width:32px; height:32px;">',
                                                                  },
                                                                  { start: new Date(2024, 7, 24, 16, 0, 0), content: "Report" },
                                                                  {
                                                                    start: new Date(2024, 7, 26),
                                                                    end: new Date(2024, 8, 2),
                                                                    content: "Traject A",
                                                                  },
                                                                  {
                                                                    start: new Date(2024, 7, 28),
                                                                    content:
                                                                      '<div>Memo</div><img src="https://gadgetsin.com/uploads/2021/03/divoom_pixoo_max_pixel_led_display_1-66x66.jpg" style="width:48px; height:48px;">',
                                                                  },
                                                                  {
                                                                    start: new Date(2024, 7, 29),
                                                                    content:
                                                                      '<div>Phone call</div><img src="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fwww.iconsdb.com%2Ficons%2Fpreview%2Fdim-gray%2Fphone-32-xl.png&f=1&nofb=1&ipt=dde3425f8a9454a0655ad8e4a21aaf30c64fcc548ab7c3b6c414b6b088f635a3&ipo=images" style="width:32px; height:32px;">',
                                                                  },
                                                                  {
                                                                    start: new Date(2024, 7, 31),
                                                                    end: new Date(2024, 8, 3),
                                                                    content: "Traject B",
                                                                  },
                                                                  {
                                                                    start: new Date(2024, 8, 4, 12, 0, 0),
                                                                    content:
                                                                      '<div>Report</div><img src="hhttp://127.0.0.1:43932/assets/timeline/imgs/duck.png" style="width:32px; height:32px;">',
                                                                  },
                                                                ]);
            
                                                                var options = {
                                                                  editable: true,
                                                                  margin: {
                                                                    item: 20,
                                                                    axis: 40,
                                                                  },
                                                                };
            
                                                                var timeline = new vis.Timeline(container, items, options);
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
            id="card_display_vistimeline",
        )
    elif card_vistimeline_css % 2 == 0:
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
                                                    id="card_vistimeline_simulator",
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
                                                    id="card_vistimeline_js",
                                                    n_clicks=1,
                                                ),
                                            ],
                                        ),
                                        dmc.Tooltip(
                                            label="CSS",
                                            position="bottom",
                                            offset=3,
                                            children=[
                                                dmc.ActionIcon(
                                                    DashIconify(
                                                        icon="skill-icons:css",
                                                        width=30,
                                                    ),
                                                    color="blue",
                                                    variant="transparent",
                                                    id="card_vistimeline_css",
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
body {
  font-family: purisa, "comic sans", cursive;
}

.vis-timeline {
  border: 2px solid #111c44;
  font-family: purisa, "comic sans", cursive;
  font-size: 12pt;
  background: #8cd9f8;
}

.vis-item {
  border-color: #000000;
  background-color: #fd690d;
  font-size: 15pt;
  color: #111c44;
  box-shadow: 5px 5px 20px rgba(128, 128, 128, 0.5);
}

.vis-item,
.vis-item.vis-line {
  border-width: 3px;
}

.vis-item.vis-dot {
  border-width: 10px;
  border-radius: 10px;
}

.vis-item.vis-selected {
  border-color: green;
  background-color: lightgreen;
}

.vis-time-axis .vis-text {
  color: #111c44;
  padding-top: 10px;
  padding-left: 10px;
}

.vis-time-axis .vis-text.vis-major {
  font-weight: bold;
}

.vis-time-axis .vis-grid.vis-minor {
  border-width: 2px;
  border-color: #000000;
}

.vis-time-axis .vis-grid.vis-major {
  border-width: 2px;
  border-color: #000000;
}

.element.style {
    height: 32px !important;
    width: 32px !important;
}
                                                                """,
                                                                    language="css",
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
            id="card_display_vistimeline",
        )
    else:
        return dash.no_update
