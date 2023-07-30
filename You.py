import pandas as pd
import plotly.express as px
import statistics 


dataOne = pd.read_csv("Copy+of+data+-+data (2).csv")
scattergraph1 = px.scatter(dataOne, x = "date", y = "cases", color = "country")