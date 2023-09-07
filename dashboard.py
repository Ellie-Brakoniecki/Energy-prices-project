import dash
from dash import html, dcc
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
import os

def to_datetime_first_day(quarter_str):
    year, qtr = quarter_str.split('_Q')
    first_month = (int(qtr) - 1) * 3 + 1  # First month of the quarter
    return pd.Timestamp(f'{year}-{first_month:02d}-01')

def convert_time_period_to_dt(merged_df):
    merged_df['Time_Period_dt'] = merged_df['Time_Period'].apply(to_datetime_first_day)
    merged_df.drop(columns=["Standardised_Quarter", "Time_Period"], inplace=True)
    reordered_columns = ['Time_Period_dt'] + [col for col in merged_df.columns if col != 'Time_Period_dt']
    merged_df_reordered= merged_df[reordered_columns]
    return merged_df_reordered

os.chdir("d:/Users/ellie.brakoniecki/Desktop/ONS/Module_10_project/Energy-prices-project/")
merged_df = pd.read_csv('merged_df.csv')
merged_df_dt = convert_time_period_to_dt(merged_df)
merged_df_dt['Timestamp'] = merged_df_dt['Time_Period_dt'].apply(lambda x: x.timestamp())

min_time = merged_df_dt['Timestamp'].min()
max_time = merged_df_dt['Timestamp'].max()
initial_value = [min_time, max_time]
unique_times = sorted(merged_df_dt['Timestamp'].unique())
# Create marks for the first and third quarters of each unique year (i.e. Jan 1st and Jul 1st)
marks = {int(timestamp): {'label': pd.to_datetime(timestamp, unit='s').strftime('%Y-%m')}
         for timestamp in unique_times if pd.to_datetime(timestamp, unit='s').month in [1, 7]}


app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Energy Prices and Unemployment Rate Dashboard"),
    
    html.Link(
        rel='stylesheet',
        href='/assets/dashboard.css' 
    ),
    
    dcc.Dropdown(
        id='sector-dropdown',
        options=[{'label': sector, 'value': sector} for sector in merged_df_dt.columns[3:]],
        value='Agriculture, forestry, fishing, mining, energy & water (A, B, D, E)',  # default value
        style={'width': '50%'}
    ),
    
    dcc.RangeSlider(
        id='time-slider',
        min=min_time,
        max=max_time,
        value=initial_value,
        marks=marks,
        step=None
    ),
    
    dcc.Graph(id='line-plot',         
            style={
            'width': '80%',                
            'border': '1px solid #ccc',  
            'box-shadow': '0 2px 4px rgba(0, 0, 0, 0.1)',  
        }),
])


@app.callback(
    Output('line-plot', 'figure'),
    [Input('sector-dropdown', 'value'),
     Input('time-slider', 'value')]
)
def update_graph(selected_sector, selected_years):
    start_date = pd.to_datetime(selected_years[0], unit='s')
    end_date = pd.to_datetime(selected_years[1], unit='s')
    
    filtered_df = merged_df_dt[(merged_df_dt['Time_Period_dt'] >= start_date) & 
                               (merged_df_dt['Time_Period_dt'] <= end_date)]
    
    fig = px.line(filtered_df, x='Time_Period_dt', y=selected_sector,
                  title=f"{selected_sector} - Unemployment Rate Over Time")
    
    return fig


if __name__ == '__main__':
    app.run_server(debug=True)
