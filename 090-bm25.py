import numpy as np
from collections import Counter

def calculate_bm25_scores(corpus, query, k1=1.5, b=0.75):
    avgdl = sum([len(doc) for doc in corpus])/len(corpus)

    tf_dict = {}
    for i, sentence in enumerate(corpus):
        tf_dict[i] = {}
        for word in sentence:
            tf_dict[i][word] = tf_dict[i].get(word, 0) + 1

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
        idf_values[q] = np.log((1 + N)/(1 + df[q]))

    scores = []
    for i, doc in enumerate(corpus):
        score = 0
        doc_len = len(doc)
        for q in query:
            tf = tf_dict[i].get(q, 0) 
            numerator = tf * (k1 + 1)
            denominator = tf + k1 * (1 - b + b * doc_len/avgdl)
            score += idf_values[q] * numerator/denominator
        scores.append(round(score, 3))

    return scores