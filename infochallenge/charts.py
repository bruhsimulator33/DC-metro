import plotly.express as px 
import pandas as pd

# Load the CSV file
june19th = pd.read_csv('July_20_2024.csv', delimiter="\t", encoding='utf16')

# Calculate the 'total' ridership across all time periods for each row (station)
june19th["total"] = (
    pd.to_numeric(june19th["AM Peak (Open-9:30am)"]) + 
    pd.to_numeric(june19th["Midday (9:30am-3pm)"]) + 
    pd.to_numeric(june19th["PM Peak (3pm-7pm)"]) + 
    pd.to_numeric(june19th["Evening (7pm-12am)"]) + 
    pd.to_numeric(june19th["Late Night (12am-Close)"])
)

# Create a bar chart using Plotly, where each time period is represented as a separate bar
#fig = px.bar(june19th, x='Station Name', y= ['AM Peak (Open-9:30am)', 'Midday (9:30am-3pm)', 'PM Peak (3pm-7pm)', 'Evening (7pm-12am)', 'Late Night (12am-Close)', 'total'], barmode = 'group', title='Ridership Across Different Time Periods for Each Station')
fig = px.bar(june19th, x='Station Name', y= 'total', barmode = 'group', title='Ridership Across Different Time Periods for Each Station')
# Show the chart
fig.show()
