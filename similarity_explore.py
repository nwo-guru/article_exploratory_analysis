import os
from gensim import corpora, models, similarities
from config import articles_mm, articles_dict, articles_index
from load_bbc_articles import load_all_bbc_articles


def main():
    dictionary = corpora.Dictionary.load(articles_dict)
    corpus = corpora.MmCorpus(articles_mm)
    lsi = models.LsiModel(corpus, id2word=dictionary, num_topics=2)
    index = similarities.MatrixSimilarity(lsi[corpus])

    q1 = make_query_vec(dictionary, lsi, 'ebbers')
    sims = index[q1]
    sims = sorted(enumerate(sims), key=lambda item: -item[1])
    articles = load_all_bbc_articles()
    for n in range(100):
        print(sims[n + 1][0], articles[sims[n + 1][0]])

def make_query_vec(dictionary, lsi, query_text):
    vec_bow = dictionary.doc2bow(query_text.lower().split())
    return lsi[vec_bow]

if __name__ == '__main__':
    main()
