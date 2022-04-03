import pandas as pd

# Read the Table from the URL, clean the Table, Save it.
url = ('https://www.skysports.com/premier-league-table')
df = pd.read_html(url)
table = df[0].rename(columns = {'#':'Rank'}).drop('Last 6', axis=1).set_index('Rank')
print(table)

table.to_csv(r"../league_table.csv", header=True)