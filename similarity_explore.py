import os
from gensim import corpora, models, similarities
from config import articles_mm, articles_dict, articles_index
from load_bbc_articles import load_all_bbc_articles


def main():
    dictionary = corpora.Dictionary.load(articles_dict)
    corpus = corpora.MmCorpus(articles_mm)
    lsi = models.LsiModel(corpus, id2word=dictionary, num_topics=2)
    index = load_index(corpus, lsi, articles_index)

    q1 = make_query_vec(dictionary, lsi, 'the stock market is for cool teens')
    sims = index[q1]
    sims = sorted(enumerate(sims), key=lambda item: -item[1])
    articles = load_all_bbc_articles()
    print(sims[0][0])
    print(articles[sims[0][0]])
    print(sims)
    print()

def make_query_vec(dictionary, lsi, query_text):
    vec_bow = dictionary.doc2bow(query_text.lower().split())
    return lsi[vec_bow]

def load_index(corpus, lsi, index_path):
    """ Load a matrix similarity index from a given dictionary and corpus
    """
    if not os.path.isfile(index_path):
        index = similarities.MatrixSimilarity(lsi[corpus])
        index.save(index_path)
    else:
        index = similarities.MatrixSimilarity.load(index_path)
    return index

if __name__ == '__main__':
    main()
