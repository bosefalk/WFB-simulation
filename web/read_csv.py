from pandas import read_csv

# Read the csv produced by wfb_simulation.py
df = read_csv('~/Projects/WFB-simulation/results.csv')

# Tbl records the number of wins, total is number of simulated battles
tbl = df['Winner'].value_counts()
total = df['Winner'].count()

# Calculate percentage wins for each entry in tbl
tbl = tbl/total * 100

print("Win %")
print(tbl)



