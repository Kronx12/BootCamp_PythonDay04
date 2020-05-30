from FileLoader import FileLoader

class SpatioTemporalData:
    def __init__(self, data):
        self.data = data
        self.data = self.data.drop(['Event','Sex', 'Name', 'Sport',
                                    'Season', 'Weight', 'Age', 'Height',
                                    'Team', 'NOC', 'Games', 'ID', 'Medal'],
                                   axis=1)
        self.data = self.data.drop_duplicates('Year')

    def when(self, location):
        return self.data.loc[self.data['City'] == location].Year.tolist()

    def where(self, date):
        return self.data.loc[self.data['Year'] == date].City.tolist()

if __name__ == "__main__":
    loader = FileLoader()
    data = loader.load('athlete_events.csv')
    sp = SpatioTemporalData(data)
    print(sp.where(1896))
    print(sp.where(2016))
    print(sp.when('Athina'))
    print(sp.when('Paris'))
