import plotly.figure_factory as ff
import csv
import pandas as pd

df = pd.read_csv("C:/Users/iliea/OneDrive/Desktop/Code/Python/Hw/Hw108/data2.csv")

fig = ff.create_distplot([df["Mobile Brand"].tolist()],["Brand"])
fig.show()