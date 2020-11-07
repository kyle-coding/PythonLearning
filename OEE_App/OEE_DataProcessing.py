import pandas as pd


class OEEData:

    def __init__(self):
        self.df = []  # This will be the raw dataframe from the csv file
        self.loc = 'OEE_data.csv'

    def get_data(self):
        self.df = pd.read_csv(self.loc)

    def display_raw_data(self):
        print(self.df.head())