import dash
import dash_core_components as dcc
from dash import html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
import os

os.chdir("d:/Users/ellie.brakoniecki/Desktop/ONS/Module_10_project/Energy-prices-project/")
merged_df = pd.read_csv('merged_df.csv')

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Energy Prices and Unemployment Rate Dashboard"),
    
    dcc.Dropdown(
        id='sector-dropdown',
        options=[{'label': sector, 'value': sector} for sector in merged_df['Sector'].unique()],
        value='Manufacturing',  # default value
        style={'width': '50%'}
    ),
    
    dcc.RangeSlider(
        id='time-slider',
        min=merged_df['Year'].min(),
        max=merged_df['Year'].max(),
        value=[merged_df['Year'].min(), merged_df['Year'].max()],
        marks={str(year): str(year) for year in merged_df['Year'].unique()},
        step=None
    ),
    
    dcc.Graph(id='line-plot'),
])


@app.callback(
    Output('line-plot', 'figure'),
    [Input('sector-dropdown', 'value'),
     Input('time-slider', 'value')]
)
def update_graph(selected_sector, selected_years):
    filtered_df = merged_df[(merged_df['Sector'] == selected_sector) & 
                             (merged_df['Year'] >= selected_years[0]) & 
                             (merged_df['Year'] <= selected_years[1])]
    
    fig = px.line(filtered_df, x='Time_Period', y=['Unemployment_Rate', 'Electricity_Avg_Price', 'Gas_Avg_Price'],
                  title=f"{selected_sector} - Unemployment Rate and Energy Prices Over Time")
    
    return fig

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
