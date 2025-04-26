import numpy as np

def compute_tf_idf(corpus, query):
    tf_dict = {}
    for i, sentence in enumerate(corpus):
        tf_dict[i] = {}
        for word in sentence:
            tf_dict[i][word] = tf_dict[i].get(word, 0) + 1
    
    tf_values = []
    for i, sentence in enumerate(corpus):
        tf_row = []
        for q in query:
            tf = tf_dict[i].get(q, 0) / len(sentence)
            tf_row.append(tf)
        tf_values.append(tf_row)
    
    df = {}
    for q in query:
        count = 0
        for i in range(len(corpus)):
            if q in tf_dict[i]:
                count += 1
        df[q] = count
    
    N = len(corpus)
    idf_values = {}
    for q in query:
        idf_values[q] = np.log((N + 1) / (df[q] + 1)) + 1

    tf_idf_values = []
    for i in range(len(corpus)):
        tf_idf_row = []
        for j, q in enumerate(query):
            tf_idf = tf_values[i][j] * idf_values[q]
            tf_idf_row.append(tf_idf)
        tf_idf_values.append(tf_idf_row)

    return tf_idf_values