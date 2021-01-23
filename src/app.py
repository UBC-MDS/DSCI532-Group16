import dash
import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import altair as alt
import pandas as pd
from dash.dependencies import Input, Output
from vega_datasets import data


#Dash App Initialize
app = dash.Dash(__name__, external_stylesheets = [dbc.themes.BOOTSTRAP])
#Add Heroku server object
server = app.server



# Data Prep
state_map = alt.topo_feature(data.us_10m.url, 'states')

data = pd.read_csv('data/processed/processed_survey.csv')
#States dataframe for filter
df_states = data[['state_fullname', 'state']].drop_duplicates(subset=['state_fullname','state']).dropna()
df_states = df_states.sort_values(by='state_fullname')


SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "20rem",
    "padding": "2rem 1rem",
    "background-color": "#f8f9fa",
}

sidebar = html.Div(
    [
        html.H4("Filters", className="display-5"),
        html.Hr(),
        html.P(
            ""
        ),
        # State Filter
        html.Div([
                html.Label(['State Selection', 
                dcc.Dropdown(
                    id = 'state_selector',
                    options=[{'label': state_full, 'value': state_abbrev} 
                        for state_full, state_abbrev in list(zip(df_states.state_fullname, df_states.state))],
                        value='AL', multi=False)]),
            ], 
            style={"width": "100%"}),

        # Age Slider
        html.Label(['Age']),
        dcc.RangeSlider(id = 'age_slider', min = 18, max = 75, value = [18,75], 
            marks = {18:'18', 30:'30', 40:'40', 50:'50', 60:'60', 70:'70', 75:'75'}),

        # Gender Filter Checklist
        html.Label(['Gender']),
        dcc.Checklist(
            id = 'gender_checklist',
            options = [
                {'label' : 'Male', 'value' : 'Male'},
                {'label' : 'Female', 'value' : 'Female'},
                {'label' : 'Other', 'value' : 'Other'}],
            value = ['Male', 'Female', 'Other'],
            labelStyle = {'display': 'inline_block'}
        ),

        # Self-Employed Filter Checklist
        html.Label(['Self-Employed']),
        dcc.Checklist(
            id = 'self_emp_checklist',
            options = [
                {'label' : 'Yes', 'value' : 'Yes'},
                {'label' : 'No', 'value' : 'No'},
                {'label' : 'N/A', 'value' : 'N/A'}],
            value = ['Yes', 'No', 'N/A'],
            labelStyle = {'display': 'inline_block'}
            
        )

    ],
    style=SIDEBAR_STYLE,
)


CONTENT_STYLE = {
    "margin-left": "20rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}
content = html.Div([
           html.H2('Employee Mental Health Survey in the Tech Industry'),
            dbc.Tabs([
                # Tab 1
                dbc.Tab([

                    # Map plot
                    html.Iframe(
                        id = 'map_frame', 
                        style = {'border-width' : '0', 'width' : '100%', 'height': '400px'}),

                    #Options Barplot
                    html.Iframe(
                        id = 'options_barplot', 
                        style = {'border-width' : '0', 'width' : '100%', 'height': '200px'}),         

                    #Discuss mental issues with supervisor boxplot
                    html.Iframe(
                        id = 'iframe_discuss_w_supervisor', 
                        style = {'border-width' : '0', 'width' : '100%', 'height': '200px'}),            
                    

                    ],
                    label = 'HR Prototype v0.01'),


                #Tab 2
                #dbc.Tab('Other text', label = 'Tab Two')
            ])], 
            id="page-content", style=CONTENT_STYLE)


#Main Layout
app.layout = html.Div([
    
    #side bar div
    sidebar,

    #content div
    content,
 
])

@app.callback(
    Output('options_barplot', 'srcDoc'),
    Input('age_slider', 'value'),
    Input('state_selector','value'),
    Input('gender_checklist', 'value'),
    Input('self_emp_checklist', 'value'))
def plot_options_bar(age_chosen, state_chosen, gender_chosen, self_emp_chosen):
    chart = alt.Chart(data[(data['Age'] >= age_chosen[0]) 
    & (data['Age'] <= age_chosen[1]) 
    & (data['state'] == state_chosen )
    & (data['Gender'].isin(gender_chosen))
    & (data['self_employed'].isin(self_emp_chosen))], 
    title = "Do you know the options for mental health care your employer provides?").mark_bar().encode(
        x = alt.X('count()'),
        y = alt.Y('care_options', sort = '-x', title = ""))
    return chart.to_html()


@app.callback(
    Output('iframe_discuss_w_supervisor', 'srcDoc'),
    Input('age_slider', 'value'),
    Input('state_selector','value'),
    Input('gender_checklist', 'value'),
    Input('self_emp_checklist', 'value'))
def plot_discuss_w_supervisor(age_chosen, state_chosen, gender_chosen, self_emp_chosen):
    filtered_data = data[(data['Age'] >= age_chosen[0]) 
    & (data['Age'] <= age_chosen[1]) 
    & (data['state'] == state_chosen )
    & (data['Gender'].isin(gender_chosen))
    & (data['self_employed'].isin(self_emp_chosen))]
    supervisor_boxplot = alt.Chart(filtered_data, 
        title='Would employee be willing to discuss mental health issues with supervisor?').mark_boxplot().encode(
            x=alt.X('Age',  scale=alt.Scale(domain=[18, 80])), 
            y=alt.Y('supervisor',title='')                                
            )
    supervisor_means = (alt.Chart(filtered_data)).mark_circle(color='white').encode( x='mean(Age)', y='supervisor')
    chart = (supervisor_boxplot + supervisor_means)
    return chart.to_html()


map_click = alt.selection_multi()


@app.callback(
    Output('map_frame', 'srcDoc'),
    Input('age_slider', 'value'),
    Input('gender_checklist', 'value'),
    Input('self_emp_checklist', 'value'))
def plot_map(age_chosen, gender_chosen, self_emp_chosen):

    filtered_data = data[(data['Age'] >= age_chosen[0]) 
    & (data['Age'] <= age_chosen[1])
    & (data['Gender'].isin(gender_chosen))
    & (data['self_employed'].isin(self_emp_chosen))]

    frequencydf = filtered_data.groupby('id')['has_condition'].transform('sum')
    data['Mental_health_count'] = frequencydf
    
    map = (alt.Chart(state_map, 
        title = 'Frequency of mental health condition').mark_geoshape().transform_lookup(
        lookup='id',
        from_=alt.LookupData(data, 'id', ['Mental_health_count']))
        .encode(
        color='Mental_health_count:Q',
        opacity=alt.condition(map_click, alt.value(1), alt.value(0.2)),
        tooltip=['state:N', 'Mental_health_count:Q'])
        .add_selection(map_click)
        .project(type='albersUsa'))
    return map.to_html()

if __name__ == '__main__':
    app.run_server(debug = True)

