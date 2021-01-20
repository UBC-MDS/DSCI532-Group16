import dash
import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_core_components as dcc

app = dash.Dash(__name__, external_stylesheets = [dbc.themes.BOOTSTRAP])
app.layout = html.Div([
    html.H1('Mental Health Survey Dashboard'),
    dbc.Tabs([
        # Tab 1
        dbc.Tab([
            # Age Slider
            html.H1('Age Slider'),
            dcc.RangeSlider(min = 0, max = 5, value = [2,3], 
            marks = {0: '0', 5: '5'}),
            
            # Country Filter
            dbc.Row([
                dbc.Col([
            html.Label(['Country Selection', dcc.Dropdown(
                options=[
                    {'label': 'United States', 'value': 'United States'},
                    {'label': 'Canada', 'value': 'Canada'}],
                    value='United States', multi=True)]),
                ], md=3)
            ]),
            # State Filter
            dbc.Row([
                dbc.Col([
            html.Label(['State Selection', dcc.Dropdown(
                options=[
                    {'label': 'Alabama', 'value': 'AL'},
                    {'label': 'Alaska', 'value': 'AK'},
                    {'label': 'Arizona', 'value': 'AZ'},
                    {'label': 'Arkansas', 'value': 'AR'},
                    {'label': 'California', 'value': 'CA'},
                    {'label': 'Colorado', 'value': 'CO'},
                    {'label': 'Connecticut', 'value': 'CT'},
                    {'label': 'Delaware', 'value': 'DE'},
                    {'label': 'Florida', 'value': 'FL'},
                    {'label': 'Georgia', 'value': 'GA'},
                    {'label': 'Hawaii', 'value': 'HI'},
                    {'label': 'Idaho', 'value': 'ID'},
                    {'label': 'Illinois', 'value': 'IL'},
                    {'label': 'Indiana', 'value': 'IN'},
                    {'label': 'Iowa', 'value': 'IA'},
                    {'label': 'Kansas', 'value': 'KS'},
                    {'label': 'Kentucky', 'value': 'KY'},
                    {'label': 'Louisiana', 'value': 'LA'},
                    {'label': 'Maine', 'value': 'ME'},
                    {'label': 'Maryland', 'value': 'MD'},
                    {'label': 'Massachusetts', 'value': 'MA'},
                    {'label': 'Michigan', 'value': 'MI'},
                    {'label': 'Minnesota', 'value': 'MN'},
                    {'label': 'Mississippi', 'value': 'MS'},
                    {'label': 'Missouri', 'value': 'MO'},
                    {'label': 'Montana', 'value': 'MT'},
                    {'label': 'Nebraska', 'value': 'NE'},
                    {'label': 'Nevada', 'value': 'NV'},
                    {'label': 'New Hampshire', 'value': 'NH'},
                    {'label': 'New Jersey', 'value': 'NJ'},
                    {'label': 'New Mexico', 'value': 'NM'},
                    {'label': 'New York', 'value': 'NY'},
                    {'label': 'North Carolina', 'value': 'NC'},
                    {'label': 'North Dakota', 'value': 'ND'},
                    {'label': 'Ohio', 'value': 'OH'},
                    {'label': 'Oklahoma', 'value': 'OK'},
                    {'label': 'Oregon', 'value': 'OR'},
                    {'label': 'Pennsylvania', 'value': 'PA'},
                    {'label': 'Rhode Island', 'value': 'RI'},
                    {'label': 'South Carolina', 'value': 'SC'},
                    {'label': 'South Dakota', 'value': 'SD'},
                    {'label': 'Tennessee', 'value': 'TN'},
                    {'label': 'Texas', 'value': 'TX'},
                    {'label': 'Utah', 'value': 'UT'},
                    {'label': 'Vermont', 'value': 'VT'},
                    {'label': 'Virginia', 'value': 'VA'},
                    {'label': 'Washington', 'value': 'WA'},
                    {'label': 'West Virginia', 'value': 'WV'},
                    {'label': 'Wisconsin', 'value': 'WI'},
                    {'label': 'Wyoming', 'value': 'WY'}],
                    value='AL', multi=True)]),
                ], md=3)
            ])
            # Gender Selection

            # Self Employed
            ], label = 'Tab One'),


        #Tab 2
        dbc.Tab('Other text', label = 'Tab Two')
    ])
])

if __name__ == '__main__':
    app.run_server(debug = True)

