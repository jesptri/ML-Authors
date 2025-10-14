import pandas as pd

df = pd.read_csv("dataset/Gungor_2018_VictorianAuthorAttribution_data-train.csv", sep=",", encoding='latin-1')

words = {}
for line in df["text"]:
    line = line.strip().split(" ")
    for word in line:
        if word not in words:
            words[word] = 0
        words[word] += 1
    
l = [(k, words[k]) for k in words]
l.sort(key=lambda x : x[1], reverse=True)

with open("tokenizer.txt", "w+") as f:
    for i in range(len(l)):
        f.write(f"{l[i][0]}>{i}\n")

    

