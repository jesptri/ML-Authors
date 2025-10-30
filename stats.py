import pandas as pd

df = pd.read_csv("dataset/Gungor_2018_VictorianAuthorAttribution_data-train.csv", sep=",", encoding='latin-1')

with open("stats.txt", "w+") as f:
    authors = df["author"].unique()
    for author in authors:
        sentence_length = 0
        sentences_numbers = 0
        words_lengths = 0
        for line in df[df["author"] == author]["text"]:
            sentences_numbers += 1
            line = line.strip().split(" ")
            sentence_length += len(line)
            words_lengths += sum(list(map(lambda x : len(x), line)))
        f.write(f'Author {author}\n')
        f.write(f'Number of sentences {sentences_numbers}\n')
        f.write(f'Number of word per sentence {sentence_length / sentences_numbers:.3f}\n')
        f.write(f'Number of letter per word {words_lengths / sentence_length:.3f}\n')