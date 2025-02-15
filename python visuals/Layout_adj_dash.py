import pandas as pd
import plotly.express as px
from dash import Dash, html, dcc

data = {
    'Fruits':['apple','banana','grape'],
    'Price':[100,200,300]
}

df = pd.DataFrame(data)

app = Dash(__name__)

bar_chart = px.bar(df, x = 'Fruits', y = 'Price', title = 'Fruits Prices')
pie_chart = px.pie(df, names = 'Fruits', values = 'Price', title = 'Fruit Prices')

app.layout = html.Div([
    html.Div([
        dcc.Graph(
        id = 'bar-chart',
        figure = bar_chart
    )
        
    ], style = {'flex':1}),
    html.Div([
        dcc.Graph(
        id = 'pie_chart',
        figure = pie_chart
    )
    ], style = {'flex':1})
], style={'display':'flex','justify-content':'space-between'})

if __name__ == '__main__':
    app.run_server(debug = True)