import pandas as pd
import numpy as np
from collections import Counter

def build_tokenizer_file(input_file, output_file = "tokenizer.txt"):
    df = pd.read_csv(input_file, sep=",", encoding='latin-1')
    all_text = " ".join(df["text"].astype(str)) # create a single text from all lines
    words = all_text.split()
    counter = Counter(words) # count frequency for each word
    sorted_words = counter.most_common() # sort by frequency
    with open(output_file, "w", encoding="latin-1") as f:
        for i, (word, _) in enumerate(sorted_words):
            f.write(f"{word}>{i}\n")

def build_tokenizer_dic(input_file = "tokenizer.txt"):
    ret = {}
    with open(input_file, "r") as f:
        for line in f.readlines():
            line = line.strip().split(">")
            ret[line[0]] = int(line[1])
    return ret

def tokenize_sentence(sentence, tokenizer):
    return [tokenizer[word] for word in sentence.strip().split(" ")]

def tokenize_list(sentences, tokenizer):
    return np.array([tokenize_sentence(s, tokenizer) for s in sentences])

if __name__ == "main":
    build_tokenizer_file("dataset/Gungor_2018_VictorianAuthorAttribution_data-train.csv")