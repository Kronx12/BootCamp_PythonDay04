from FileLoader import FileLoader

def howManyMedals(data, name):
    all_lines = data.loc[data['Name'] == name]
    all_lines = all_lines.loc[data['Medal'].notna()]
    all_lines = all_lines.drop(['Event','Sex', 'Name', 'Sport',
                                'Season', 'Weight', 'Age', 'Height',
                                'City', 'Team', 'NOC', 'Games', 'ID'], axis=1)
    res = {}
    for index, row in all_lines.iterrows():
        if row['Year'] not in res:
            res[row['Year']] = {'G': 0, 'S': 0, 'B': 0}
        if row['Medal'] == "Gold":
            res[row['Year']]['G'] += 1
        elif row['Medal'] == "Silver":
            res[row['Year']]['S'] += 1
        elif row['Medal'] == "Bronze":
            res[row['Year']]['B'] += 1
    return res

if __name__ == "__main__":
    loader = FileLoader()
    data = loader.load('athlete_events.csv')
    data_set = howManyMedals(data, 'Kjetil Andr Aamodt')
    print(data_set)