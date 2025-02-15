from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

# Create the Dash app
app = Dash(__name__)

# Sample data for the bar chart
data = {
    'Fruits': ['Apples', 'Bananas', 'Cherries', 'Dates'],
    'Quantity': [10, 15, 7, 5]
}
df = pd.DataFrame(data)

# Create the bar chart using Plotly Express
fig = px.bar(df, x='Fruits', y='Quantity', title='Fruit Quantities')

# Define the layout of the app
app.layout = html.Div([
    dcc.Graph(
        id='bar-chart',  # Unique ID for the chart
        figure=fig       # Pass the figure to be displayed
    )
])

# Run the Dash app
if __name__ == '__main__':
    app.run_server(debug=True)
