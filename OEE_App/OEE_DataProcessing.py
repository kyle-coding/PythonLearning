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
        ret = self.calc_df[
            (self.calc_df['Timestamp'] >= day) &
            (self.calc_df['Timestamp'] < next_day)
            ]
        return ret

    def group_by_date(self):
        self.calc_df['calc_Day'] = self.calc_df['Timestamp'].dt.dayofyear  # Add a day-of-the-year column
        ret = self.calc_df.groupby(['calc_Day', 'OEE_Main', 'OEE_Subcategory', 'OEE_State'], as_index=False).sum()
        ret.rename(columns={'calc_TimeInCurrentState': 'calc_sumOfTime'})
        print(ret.columns)
        return ret

    def calc_total_available(self, data):
        ret = data[(data['OEE_Main'] == 'Available')]
        ret = ret.groupby(['calc_Day'], as_index=False).sum()
        ret = ret[['calc_Day', 'calc_TimeInCurrentState']]
        ret = ret.rename(columns={'calc_TimeInCurrentState': 'Total Time', 'calc_Day': 'Day of the Year'})
        ret['Total Time'] = ret['Total Time'].dt.total_seconds() / 3600.0  # convert the datetime to hours
        print(ret)
        return ret

    def __init__(self):
        self.df = []  # This will be the raw dataframe from the csv file
        self.loc = 'OEE_data.csv'

        self.get_data()
        self.calc_df = self.df.copy()
        self.calculate_accumulated_time()

        specific_date = datetime(2020, 11, 6)
        print(specific_date)
        spec_day = self.get_day(specific_date)

        self.data_totalAvailable = self.calc_total_available(self.group_by_date())
