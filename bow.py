from scipy.sparse import csr_matrix

def bow_list(sentences, tokenizer):
    data, row_ind, col_ind = [], [], []
    for i, sentence in enumerate(sentences):
        for word in sentence.strip().split():
            if word in tokenizer:
                data.append(1)
                row_ind.append(i)
                col_ind.append(tokenizer[word])
    return csr_matrix((data, (row_ind, col_ind)), shape=(len(sentences), len(tokenizer)))
