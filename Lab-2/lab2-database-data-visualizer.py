import plotly.express as px
import sqlite3
import pandas as pd
import plotly.graph_objects as go
import plotly.graph_objs as go
import plotly.offline
#pd.options.plotting.backend = "plotly";
from plotly.subplots import make_subplots
#from signal import signal, SIGPIPE, SIG_DFL
#signal(SIGPIPE,SIG_DFL)

#connect to database file
dbconnect = sqlite3.connect("sensorDB.db");
#If we want to access columns by name we need to set
#row_factory to sqlite3.Row class
dbconnect.row_factory = sqlite3.Row;
#now we create a cursor to work with db
cursor = dbconnect.cursor();
#execute simple select statement
cursor.execute('SELECT * FROM temps');

df = pd.DataFrame(cursor.fetchall(), columns = ['id', 'date', 'time', 'temperature', 'humidity', 'pressure']);
#print(df);
fig = make_subplots(specs=[[{"secondary_y": True}]]);
fig.add_trace(
    go.Scatter(x= df.iloc[:,2], y= df.iloc[:,3], name="temperature"),
    secondary_y=False,
    )
fig.add_trace(
    go.Scatter(x= df.iloc[:,2], y= df.iloc[:,4], name="humidity"),
    secondary_y=False,
    )
fig.add_trace(
    go.Scatter(x= df.iloc[:,2], y= df.iloc[:,5], name="pressure"),
    secondary_y=True,
    )
plotly.offline.plot(fig)
dbconnect.close();
