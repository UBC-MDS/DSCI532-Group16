import dash
import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import altair as alt
import pandas as pd
from dash.dependencies import Input, Output
from vega_datasets import data


state_map = alt.topo_feature(data.us_10m.url, 'states')

data = pd.read_csv('data/processed/processed_survey.csv')


app = dash.Dash(__name__, external_stylesheets = [dbc.themes.BOOTSTRAP])
app.layout = html.Div([
    html.H1('Mental Health Survey Dashboard'),
    dbc.Tabs([
        # Tab 1
        dbc.Tab([

            # Country Filter
            dbc.Row([
                dbc.Col([
            html.Label(['Country Selection', dcc.Dropdown(
                id = 'country_selector',
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
                id = 'state_selector',
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
            ]),
            # Map plot
            html.Iframe(
                id = 'map_frame', 
                style = {'border-width' : '0', 'width' : '100%', 'height': '400px'}),

            # Gender Selection

            # Self Employed

            #Options Barplot
            html.Iframe(
                id = 'options_barplot', 
                style = {'border-width' : '0', 'width' : '100%', 'height': '400px'}),
            
            # Age Slider
            html.H2('Age Slider'),
            dcc.RangeSlider(id = 'age_slider', min = 18, max = 75, value = [18,75], 
            marks = {18:'18', 20:'20', 30:'30', 40:'40', 50:'50', 60:'60', 70:'70', 75:'75'}),

            ], label = 'Tab One'),


        #Tab 2
        dbc.Tab('Other text', label = 'Tab Two')
    ])
])

@app.callback(
    Output('options_barplot', 'srcDoc'),
    Input('age_slider', 'value'))
def plot_options_bar(age_chosen):
    chart = alt.Chart(data[(data['Age'] >= age_chosen[0]) & (data['Age'] <= age_chosen[1])], 
    title = "Do you know the options for mental health care your employer provides?").mark_bar().encode(
        x = alt.X('count()'),
        y = alt.Y('care_options', sort = '-x', title = "Response"))
    return chart.to_html()

map_click = alt.selection_multi()

@app.callback(
    Output('map_frame', 'srcDoc'),
    Input('state_selector', 'value'))
def plot_map(state_chosen):
    map = (alt.Chart(state_map, 
        title = 'Frequency of mental health condition').mark_geoshape().transform_lookup(
        lookup='id',
        from_=alt.LookupData(data, 'stateID', ['has_condition']))
        .encode(
        color='has_condition:Q',
        opacity=alt.condition(map_click, alt.value(1), alt.value(0.2)),
        tooltip=['state:N', 'has_condition:Q'])
        .add_selection(map_click)
        .project(type='albersUsa'))
    return map.to_html()

if __name__ == '__main__':
    app.run_server(debug = True)

