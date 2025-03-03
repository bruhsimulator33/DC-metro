import pandas as pd
import plotly.express as px
# june5=pd.read_csv ('June_05_2024.csv')
# june15=pd.read_csv ('June_05_2024.csv')
# print(june5)
# print(june15)
# summeravg= pd.merge(june5,june15,on='Station Name')
# print(summeravg)
june5=pd.read_csv('june5_2024updated.csv', delimiter="\t", encoding='utf16')
#june5["day"]= int(june5["AM Peak (Open-9:30am)"]+june5["Midday (9:30am-3pm)"]+june5["PM Peak (3pm-7pm)"]+june5["Evening (7pm-12am)"]+june5["Late Night (12am-Close)"])
#need to add the columns here and for every data set
print(june5)

june15=pd.read_csv('june15_2024_updated.csv', delimiter="\t", encoding='utf16')

print(june15)

june4=pd.read_csv('fourthofjuly.csv', delimiter="\t", encoding='utf16')

print(june15)

summeravg=pd.read_csv('tabsep.csv', delimiter="\t", encoding='utf16')

print(summeravg)

# px.histogram(summeravg, x='Station Name', y='Ridership', nbins=24, width=1000, height=600)