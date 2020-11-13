#import chart_studio.plotly as py
from plotly.offline import plot 
from plotly.graph_objs import *
import json
#py.sign_in('username', 'api_key')

with open('Texas-counties.json') as response:
    Data = json.load(response)
    


data = Data['data']
print(data)

layout = Data['layout']


fig = Figure(data=data, layout=layout)
plot_url = plot(fig)