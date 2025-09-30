import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from pytrends.request import TrendReq
import time

# SETUP PYTRENDS AND KEYWORD DEFINE
pytrends = TrendReq(hl='en-US', tz=360)
keyword = "cloud computing"

time.sleep(5)  # avoid 429

# DATA REQUEST
pytrends.build_payload([keyword], cat=0, timeframe='today 12-m', geo='', gprop='')

# country wise interest
region_data = pytrends.interest_by_region()
region_data = region_data.reset_index()   # ✅ geoName ko column banane ke liye
region_top15 = region_data.sort_values(by=keyword, ascending=False).head(15)

# --- BARPLOT ---
plt.figure(figsize=(10, 6))
sns.barplot(x=keyword, y="geoName", data=region_top15, palette="Blues_d")
plt.title(f"Top countries searching for '{keyword}'")
plt.xlabel("Interest")
plt.ylabel("Countries")
plt.show()

# --- WORLD MAP ---
fig = px.choropleth(
    region_data,                      # full data use karo world map ke liye
    locations="geoName",
    locationmode="country names",
    color=keyword,
    title=f"Search interest for '{keyword}' by country",
    color_continuous_scale="Blues"
)
fig.show()
# TIME WISE INTERESET

time_df= pytrends.interest_over_time()
plt.figure(figsize=(12,6))
plt.plot(time_df.index,time_df[keyword],marker='o',color='purple')
plt.title(f"search intrest over tine'{keyword}'")
plt.xlabel("Date")
plt.ylabel("Intrest")
plt.grid(True)
plt.show()
#MULTIPLE KEYWORD COMPARISION'
kw_list=["cloud computing","data science","machine learining"]
pytrends.build_payload(kw_list, cat=0, timeframe='today 12-m', geo='', gprop='')
compare_df=pytrends.interest_over_time()
plt.figure(figsize=(12,6))
for kw in kw_list:
    plt.plot(compare_df.index,compare_df[kw],label=kw)
plt.title("kewyword comparison overtime")
plt.xlabel("Date")
plt.ylabel("Intrest")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()