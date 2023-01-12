import pandas as pd

data = pd.read_csv(
    "/usr/local/google/home/bumaschny/synthea/src/main/resources/providers/hospitals.csv"
)

print(len(data.index))

data = data.loc[data["state"] == "MA"]


data.to_csv(
    '/usr/local/google/home/bumaschny/synthea/src/main/resources/providers/hospitals_verily.csv')

print(len(data.index))