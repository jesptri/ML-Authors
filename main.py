import pandas as pd

df = pd.read_csv("dataset/Gungor_2018_VictorianAuthorAttribution_data-train.csv", sep=",", encoding='latin-1')

df[:1000].to_csv("dataset/Gungor_train_reduced.csv", sep=",", encoding="latin-1", index=False)

#! uncomment when lines above have been run

# df = pd.read_csv("dataset/Gungor_train_reduced.csv", sep=",", encoding='latin-1')
# words = {}
# for line in df["text"]:
#     line = line.split(" ")
#     for word in line:
#         if not word in words:
#             words[word] = 0
#         words[word] += 1
# ret = []
# seil = 10000
# for key in words:
#     if words[key] > seil:
#         ret.append(key)
# print(ret)