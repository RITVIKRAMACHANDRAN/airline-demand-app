import pandas as pd

def get_demand_data(origin=None, destination=None, start_date=None, end_date=None):
    df = pd.read_csv("demand_data.csv")
    df["date"] = pd.to_datetime(df["date"])

    # 🔥 Fix: Convert to datetime for comparison
    if start_date and end_date:
        start_date = pd.to_datetime(start_date)
        end_date = pd.to_datetime(end_date)
        df = df[(df["date"] >= start_date) & (df["date"] <= end_date)]

    if origin:
        df = df[df["origin"] == origin]
    if destination:
        df = df[df["destination"] == destination]

    return df.sort_values("date")
