import dash
import dash_html_components as html
import dash_design_kit as ddk
import dash_core_components as dcc
import dash_html_components as html
import textwrap
import requests
import sodapy as Socrata


name = "asdf3135"
url = f'https://staging-bellerophon.herokuapp.com/genericApp/app_configurations/query.json?customer_domain=platform-bellerophon-{name}.genericapp.socrata-qa.com'

response = requests.get(url)
configuration = response.json()['configurations']

app = dash.Dash(__name__)
server = app.server  # expose server variable for Procfile

controls = [
    ddk.ControlItem(
        dcc.Dropdown(
            options=[
                {'label': i, 'value': i}
                for i in ['Rear', 'Front', 'Side']
            ],
            multi=True,
            value=['Rear']
        ),
        label='Engine',
    ),
    ddk.ControlItem(
        dcc.Slider(
            min=0,
            max=10,
            marks={
                0: '0',
                3: '3',
                5: '5',
                7.65: '7.65 °F',
                10: '10'
            },
            value=5
        ),
        label='Thrusters',
    ),
    ddk.ControlItem(
        dcc.Input(
            value=50,
            type='number'
        ),
        label='Power',
    )
]

menu = ddk.Menu([
    ddk.CollapsibleMenu(
        title='Performance',
        default_open=False,
        children=[
            dcc.Link('Team 1', href=app.get_relative_path('/')),
            dcc.Link('Team 2', href=app.get_relative_path('/')),
        ]
    ),
    dcc.Link('Conditions', href=app.get_relative_path('/')),
    dcc.Link('Historical', href=app.get_relative_path('/')),
    dcc.Link('Portal', href=app.get_relative_path('/')),
])


app.layout = ddk.App([

    ddk.Header([
        ddk.Logo(src=app.get_asset_url('logo.png')),
        ddk.Title(configuration),
        menu
    ]),

    ddk.Block(width=30, children=[
        ddk.ControlCard(controls),
        ddk.ControlCard(controls),
        ddk.ControlCard(controls),
    ]),

    ddk.Block(width=70, children=[

        ddk.Row([
            ddk.Card(width=50, children=dcc.Markdown(textwrap.dedent(
                '''
                Sed ut perspiciatis unde omnis iste natus
                voluptatem accusantium doloremque laudantium,
                totam rem aperiam, **expect similar results next week**
                ab illo inventore veritatis et quasi architecto
                beatae vitae dicta sunt explicabo.
                '''))
            ),

            ddk.DataCard(
                value='1.17',
                label='Power',
                trace_x=ddk.datasets.timeseries().x1,
                trace_y=ddk.datasets.timeseries().y1,
                width=25
            ),

            ddk.DataCard(
                value='5.4',
                label='Efficiency',
                trace_x=ddk.datasets.timeseries().x2,
                trace_y=ddk.datasets.timeseries().y2,
                width=25
            ),
        ]),

        ddk.Card(width=100, children=ddk.Graph(figure={
            'data': [{
                'x': [1, 2, 3, 4],
                'y': [4, 1, 6, 9],
                'line': {'shape': 'spline'}
            }]
        })),

        ddk.Card(width=50, children=ddk.Graph(figure={
            'data': [{
                'x': [1, 2, 3, 4],
                'y': [4, 1, 6, 9],
                'line': {'shape': 'spline'}
            }]
        })),

        ddk.Card(width=50, children=ddk.Graph(figure={
            'data': [{
                'x': [1, 2, 3, 4],
                'y': [4, 1, 6, 9],
                'line': {'shape': 'spline'}
            }]
        })),

    ])
])


if __name__ == '__main__':
    app.run_server(debug=True)
