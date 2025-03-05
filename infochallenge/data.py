import pandas as pd
import plotly.express as px
#https://stackoverflow.com/questions/67905780/removing-comma-from-values-in-column-csv-file-using-python-pandas used to learn how to replace commas\
#deleted all commas in original CSV's to remove confusion and only have values seperated by tab

# need to add the columns here and for every data set
june5=pd.read_csv('June_5_2024.csv', delimiter="\t", encoding='utf16')
june5["total"]= pd.to_numeric(june5["AM Peak (Open-9:30am)"]) + pd.to_numeric(june5["Midday (9:30am-3pm)"]) + pd.to_numeric(june5["PM Peak (3pm-7pm)"]) + pd.to_numeric(june5["Evening (7pm-12am)"]) + pd.to_numeric(june5["Late Night (12am-Close)"])
sorted5=june5.sort_values('total')
print(sorted5)


june15=pd.read_csv('June_15_2024.csv', delimiter="\t", encoding='utf16')
june15["total"]= pd.to_numeric(june15["AM Peak (Open-9:30am)"]) + pd.to_numeric(june15["Midday (9:30am-3pm)"]) + pd.to_numeric(june15["PM Peak (3pm-7pm)"]) + pd.to_numeric(june15["Evening (7pm-12am)"]) + pd.to_numeric(june15["Late Night (12am-Close)"])
sorted15=june15.sort_values('total')
print(sorted15)


fourthjuly=pd.read_csv('July_04_2024.csv', delimiter="\t", encoding='utf16')
fourthjuly["total"]= pd.to_numeric(fourthjuly["AM Peak (Open-9:30am)"]) + pd.to_numeric(fourthjuly["Midday (9:30am-3pm)"]) + pd.to_numeric(fourthjuly["PM Peak (3pm-7pm)"]) + pd.to_numeric(fourthjuly["Evening (7pm-12am)"]) + pd.to_numeric(fourthjuly["Late Night (12am-Close)"])
sorted4th=fourthjuly.sort_values('total')
print(sorted4th)

fathersday=pd.read_csv('June_16_2024.csv', delimiter="\t", encoding='utf16')
fathersday["total"]= pd.to_numeric(fathersday["AM Peak (Open-9:30am)"]) + pd.to_numeric(fathersday["Midday (9:30am-3pm)"]) + pd.to_numeric(fathersday["PM Peak (3pm-7pm)"]) + pd.to_numeric(fathersday["Evening (7pm-12am)"]) + pd.to_numeric(fathersday["Late Night (12am-Close)"])
sortedfather=fathersday.sort_values('total')
print(sortedfather)

juneteenth=pd.read_csv('June_19_2024.csv', delimiter="\t", encoding='utf16')
juneteenth["total"]= pd.to_numeric(juneteenth["AM Peak (Open-9:30am)"]) + pd.to_numeric(juneteenth["Midday (9:30am-3pm)"]) + pd.to_numeric(juneteenth["PM Peak (3pm-7pm)"]) + pd.to_numeric(juneteenth["Evening (7pm-12am)"]) + pd.to_numeric(juneteenth["Late Night (12am-Close)"])
sortedjuneteenth=juneteenth.sort_values('total')
print(sortedjuneteenth)

OliviaRodrigo=pd.read_csv('July_20_2024.csv', delimiter="\t", encoding='utf16')
OliviaRodrigo["total"]= pd.to_numeric(OliviaRodrigo["AM Peak (Open-9:30am)"]) + pd.to_numeric(OliviaRodrigo["Midday (9:30am-3pm)"]) + pd.to_numeric(OliviaRodrigo["PM Peak (3pm-7pm)"]) + pd.to_numeric(OliviaRodrigo["Evening (7pm-12am)"]) + pd.to_numeric(OliviaRodrigo["Late Night (12am-Close)"])
sortedOliviaRodrigo=OliviaRodrigo.sort_values('total')
print(sortedOliviaRodrigo)

LukeCombs=pd.read_csv('July_27_2024.csv', delimiter="\t", encoding='utf16')
LukeCombs["total"]= pd.to_numeric(LukeCombs["AM Peak (Open-9:30am)"]) + pd.to_numeric(LukeCombs["Midday (9:30am-3pm)"]) + pd.to_numeric(LukeCombs["PM Peak (3pm-7pm)"]) + pd.to_numeric(LukeCombs["Evening (7pm-12am)"]) + pd.to_numeric(LukeCombs["Late Night (12am-Close)"])
sortedLukeCombs=LukeCombs.sort_values('total')
print(sortedLukeCombs)

summer=pd.read_csv('allsummer.csv', delimiter="\t", encoding='utf16')
summer["summer average"]= pd.to_numeric(summer["AM Peak (Open-9:30am)"]) + pd.to_numeric(summer["Midday (9:30am-3pm)"]) + pd.to_numeric(summer["PM Peak (3pm-7pm)"]) + pd.to_numeric(summer["Evening (7pm-12am)"]) + pd.to_numeric(summer["Late Night (12am-Close)"])
sortedsummer=summer.sort_values('summer average')
print(sortedsummer)
#already has average daily entries we just need to make graphs

# px.histogram(summeravg, x='Station Name', y='Ridership', nbins=24, width=1000, height=600)