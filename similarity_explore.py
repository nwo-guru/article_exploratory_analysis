import os
from gensim import corpora, models, similarities
from config import articles_mm, articles_dict, articles_index


def main():

    index = load_index(articles_dict, articles_mm, articles_index)


def load_index(dictionary, mm, index_path):
    """ Load a matrix similarity index from a given dictionary and corpus
    """
    dictionary = corpora.Dictionary.load(dictionary)
    corpus = corpora.MmCorpus(mm)
    # 2-dimensional LSI space
    lsi = models.LsiModel(corpus, id2word=dictionary, num_topics=2)
    # Cache the index
    if not os.path.isfile(index_path):
        index = similarities.MatrixSimilarity(lsi[corpus])
        index.save(index_path)
    else:
        index = similarities.MatrixSimilarity.load(index_path)
    return index

if __name__ == '__main__':
    main()
