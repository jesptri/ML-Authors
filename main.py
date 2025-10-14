import pandas as pd

df = pd.read_csv("dataset/Gungor_2018_VictorianAuthorAttribution_data-train.csv", sep=",", encoding='latin-1')

df[:1000].to_csv("dataset/Gungor_train_reduced.csv", sep=",", encoding="latin-1", index=False)