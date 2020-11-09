import pandas as pd
import numpy as np
from datetime import date, timedelta, datetime

class OEEData:

    def get_data(self):
        # Import the data from our csv file.
        # Parse the timestamps as dates, and the run speeds as floats
        self.df = pd.read_csv(self.loc, parse_dates=['Timestamp'], dtype={'Run_Speed': np.float64})
        self.df = self.df.fillna("")
        print("Types:")
        print(self.df.dtypes)

    def print_raw_data(self):
        print(self.df.head())

    def calculate_accumulated_time(self):
        # calculate the accumulated time in each state:
        # .diff() calculates the difference between each row and the subsequent row,
        # and .shift(-1) shifts all the rows up 1
        self.calc_df['calc_TimeInCurrentState'] = self.calc_df['Timestamp'].diff().shift(-1)
        # print(self.calc_df.head())

    def get_day(self, day):
        next_day = day + timedelta(days=1)
        output = self.calc_df[
            (self.calc_df['Timestamp'] >= day) &
            (self.calc_df['Timestamp'] < next_day)
            ]
        print(output)

    def __init__(self):
        self.df = []  # This will be the raw dataframe from the csv file
        self.loc = 'OEE_data.csv'

        self.get_data()
        self.calc_df = self.df.copy()
        # self.print_raw_data()
        self.calculate_accumulated_time()
        
        specific_date = datetime(2020, 11, 6)
        print(specific_date)
        self.get_day(specific_date)
