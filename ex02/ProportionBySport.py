from FileLoader import FileLoader
import pandas as pd

def proportionBySport(data, y, s, g):
    tmp = data.loc[data['Year'] == y]
    tmp = tmp.loc[tmp['Sex'] == g]

    countAll = len(tmp.index)
    countSport = len(tmp.loc[tmp['Sport'] == s].index)

    return countSport * 100 / countAll

if __name__ == "__main__":
    fl = FileLoader()
    data = fl.load("./athlete_events.csv")

    tmp = proportionBySport(data, 2004, 'Tennis', 'M')
    print(tmp)