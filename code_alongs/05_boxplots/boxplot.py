import plotly.offline as pyo
import plotly.graph_objs as go

y = [1, 14, 14, 15, 16, 18, 18, 19, 19, 20, 20, 23, 24, 26, 27, 27, 28, 29, 33, 54]

data = [go.Box(y=y, boxpoints="outliers", jitter=0.3, pointpos=0)]


# pyo.plot(data)


snodgrass = [0.209, 0.205, 0.196, 0.210, 0.202, 0.207, 0.224, 0.223, 0.220, 0.201]
twain = [0.225, 0.262, 0.217, 0.240, 0.230, 0.229, 0.235, 0.217]

data = [go.Box(y=snodgrass, name="Snodgrass"), go.Box(y=twain, name="Twain")]

pyo.plot(data)
