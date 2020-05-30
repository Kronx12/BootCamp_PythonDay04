from FileLoader import FileLoader
import pandas as pd

def youngestFellah(data, y):
    tmp = data.loc[data['Year'] == y]
    tmp = tmp.sort_values(by=['Age'])
    return {'f':tmp.loc[tmp['Sex'] == 'F'].iloc[0].Age, 'm':tmp.loc[tmp['Sex'] == 'M'].iloc[0].Age}

if __name__ == "__main__":
    fl = FileLoader()
    data = fl.load("./athlete_events.csv")

    tmp = youngestFellah(data, 2004)
    print(tmp)