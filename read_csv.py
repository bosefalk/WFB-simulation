from pandas import read_csv

def win_percent():

    # Read the csv produced by wfb_simulation.py
    df = read_csv('results.csv')

    # Tbl records the number of wins, total is number of simulated battles
    tbl = df['Winner'].value_counts()
    total = df['Winner'].count()

    # Calculate percentage wins for each entry in tbl
    tbl = tbl/total * 100

    return(tbl)



