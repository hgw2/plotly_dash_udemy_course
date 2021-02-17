#######
# Objective: Create a bubble chart that compares three other features
# from the mpg.csv dataset. Fields include: 'mpg', 'cylinders', 'displacement'
# 'horsepower', 'weight', 'acceleration', 'model_year', 'origin', 'name'
######

# Perform imports here:
import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd



# create a DataFrame from the .csv file:
cars = pd.read_csv("../data/mpg.csv")


# create data by choosing fields for x, y and marker size attributes

data = [go.Scatter(x=cars['horsepower'],
                y=cars['acceleration'],
                text =cars['name'],
                mode = 'markers', 
                marker =  dict(size = cars['weight']/100,
                                 color = cars['cylinders'],
                                 showscale = True))]






# create a layout with a title and axis labels
layout = go.Layout(title = 'Horsepower vs. Acceleration', 
                   xaxis=dict(title = "Horsepower"), 
                   yaxis=dict(title = 'Acceleration'), 
                   hovermode = 'closest')


fig = go.Figure(data = data, layout = layout)



# create a fig from data & layout, and plot the fig

pyo.plot(fig, filename='./plots/bubble_plot.html')