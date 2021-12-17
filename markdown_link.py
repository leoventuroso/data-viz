# %%
from pprint import pprint
l = [
    "#Bar-Chart-\(column-chart\)",
    "#Dot-plot",
    "#Connected-dot-plot-\(barbell-chart,-dumb-bell-chart\)",
    "#Pictogram-\(isotype-chart,-pictorial-bar-chart,-stacked-shape-chart,-tally-chart\)",
    "#Bubble-chart-\(circle-packing-diagram\)",
    "#Radar-chart-\(star-chart,-spider-diagram,-web-chart\)",
    "#Polar-chart-\(coxcomb-plot,-area-plot\)",
    "#Range-chart-\(span-chart,-floating-bar-chart,-barometer-chart\)",
    "#Box-and-whisker-plot-\(boxplot\)"
]
nl = []
# %%
for i in l:
    lnk = i.lower()
    txt = i[1:].replace('-', " ")
    print(f"- [{txt}]({lnk})")

# %%
