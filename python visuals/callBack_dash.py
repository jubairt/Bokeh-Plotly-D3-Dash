import pandas as pd
import plotly.express as px
from dash import Dash, html, dcc, Input, Output

# Sample data
data = {
    'Fruits': ['apple', 'banana', 'grape'],
    'Price': [100, 200, 300]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Initialize the Dash app
app = Dash(__name__)

# Initial figure for the bar chart
fig = px.bar(df, x='Fruits', y='Price', title='Fruits Prices')

# App Layout
app.layout = html.Div([
    html.H1("Fruit Price Bar Chart"),
    
    # Dropdown to select fruit
    dcc.Dropdown(
        id='fruit-dropdown',
        options=[
            {'label': 'Apple', 'value': 'apple'},
            {'label': 'Banana', 'value': 'banana'},
            {'label': 'Grape', 'value': 'grape'}
        ],
        value='apple',  # Default value
        style={'width': '50%'}
    ),
    
    # Graph for the bar chart
    dcc.Graph(
        id='fruit-price-bar-chart',
        figure=fig
    )
])

# Callback to update the graph based on dropdown selection
@app.callback(
    Output('fruit-price-bar-chart', 'figure'),
    Input('fruit-dropdown', 'value')
)
def update_chart(selected_fruit):
    # Filter the DataFrame based on the selected fruit
    filtered_df = df[df['Fruits'] == selected_fruit]
    
    # Create a new figure with filtered data
    updated_fig = px.bar(filtered_df, x='Fruits', y='Price', title=f'{selected_fruit.capitalize()} Price')
    return updated_fig

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
