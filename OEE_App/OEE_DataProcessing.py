import pandas as pd


class OEEData:

    def get_data(self):
        # Import the data from our csv file.
        self.df = pd.read_csv(self.loc, parse_dates=['Timestamp'])
        print("Types:")
        print(self.df.dtypes)

    def print_raw_data(self):
        print(self.df.head())

    def calculate_accumulated_time(self):
        # self.df['Timestamp'] = pd.to_datetime(self.df['Timestamp'], format='%m/%d/%Y %H:%M%S')
        self.df['calc_AccumulatedTime'] = self.df['Timestamp'].diff()
        print(self.df.head())

    def __init__(self):
        self.df = []  # This will be the raw dataframe from the csv file
        self.loc = 'OEE_data.csv'

        self.get_data()
        # self.print_raw_data()
        self.calculate_accumulated_time()

