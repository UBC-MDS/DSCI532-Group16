import dash
import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_core_components as dcc

app = dash.Dash(__name__, external_stylesheets = [dbc.themes.BOOTSTRAP])
app.layout = html.Div([
    dbc.Tabs([
        # Tab 1
        dbc.Tab([
            # Age Slider
            html.H1('Age Slider'),
            dcc.RangeSlider(min = 0, max = 5, value = [2,3], 
            marks = {0: '0', 5: '5'})
            
            # Country Filter

            # State Filter

            # Gender Selection

            # Self Employed
            ], label = 'Tab One'),


        #Tab 2
        dbc.Tab('Other text', label = 'Tab Two')
    ])
])

if __name__ == '__main__':
    app.run_server(debug = True)

