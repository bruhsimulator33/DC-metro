import plotly.express as px 
import pandas as pd


july27th = pd.read_csv('July_27_2024.csv', delimiter="\t", encoding='utf16')


df = pd.DataFrame(july27th)
# Convert the DataFrame into a long format
df_melted = df.melt(id_vars='Station Name', var_name='Time Period', value_name='Ridership')

# Create a bar chart
fig = px.bar(df_melted, x='Station Name', y='Ridership', color='Time Period', barmode='group', title='Ridership Across Different Time Periods for Each Station')

# Show the chart
fig.show()
