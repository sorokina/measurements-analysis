import pandas as pd
import os


def main():

    absolute_path = '/mnt/data/measurements.csv'
    
    df = pd.read_csv(absolute_path, delimiter=";", header='infer')

    # Perform data transformation and cleansing operations
    df['grid_purchase'] = df["grid_purchase"].fillna(0)
    df["direct_consumption"] = df["direct_consumption"].fillna(0)

    df[['grid_purchase', 'grid_feedin', 'direct_consumption']] = df[
        ['grid_purchase', 'grid_feedin', 'direct_consumption']].replace(regex=[r'\D+'], value="0")
    df = df.astype({"serial": "str", "grid_purchase": "int", "grid_feedin": "int", "direct_consumption": "int"})

    df['date'] = pd.to_datetime(df['date'])
    
    df['timestamp'] = pd.to_datetime(df['timestamp'])

    # After cleansing, calculate the total grid_purchase and grid_feedin over all
    # batteries for each hour of the day.
    df['time_hour'] = pd.DatetimeIndex(df['timestamp']).hour

    df_sum = df.groupby(by=["time_hour"]).sum(numeric_only=True)

    # Add a column to your dataframe that indicates the hour with the highest  grid_feedin of the day (e. g. a Boolean value)

    df_sum = df_sum.reset_index()
    df_sum['peak_hour'] = df_sum['time_hour'] == df_sum['grid_purchase'].idxmax()

    absolute_path_output = '/mnt/data/CaseStudyOutput.csv'

    # Write the transformed data to an output file in CSV format.

    df_sum.to_csv(absolute_path_output, sep='\t')


if __name__ == "__main__":
    main()





