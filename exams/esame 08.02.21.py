# %%
import pandas as pd
import matplotlib.pyplot as plot
import json
import plotly.express as px
# %%
df = pd.read_excel("census.xlsx")
df.set_index(df["ANNI"])


# %%
with open('../exams/regioni.geojson', encoding="utf-8") as f:
    regioni = json.load(f)
tdf = df.transpose() # trasposizione del df
col = tdf.iloc[0,:] # prende solo la prima riga
tdf = tdf.drop("ANNI")

col = pd.Series([int(x) for x in col]) # trasfrormare la lista in colonna e da float a int
tdf = tdf.rename(columns=col)



# %%
temp = tdf.copy()
temp["average"] = temp.mean(axis=1)
# %%

locations =pd.Series(tdf.index)


# 
# %%
fig = px.choropleth_mapbox(temp,
    geojson=regioni,
    locations=locations,
    featureidkey="properties.reg_name",
    mapbox_style="carto-positron",
    opacity=0.5,
    zoom=3.5,
    color="average", 
    color_continuous_scale="Inferno", 
    center = {"lat": 41, "lon": 12}, 
    hover_name=temp.index
)


# %%
fig.show()

# %%
locations
# %%
