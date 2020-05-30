import pandas as pd


class FileLoader:
    def load(self, path):
        return pd.read_csv(path)

    def display(self, df, n):
        if n >= 0:
            print(df.head(n))
        else:
            print(df.tail(abs(n)))

if __name__ == "__main__":
    fl = FileLoader()
    data = fl.load("./athlete_events.csv")

    fl.display(data, 5)
    fl.display(data, -5)
