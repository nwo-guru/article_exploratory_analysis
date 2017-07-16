import gensim
from config import articles_mm, articles_dict


def main():
    dictionary = gensim.corpora.Dictionary.load(articles_dict)
    corpus = gensim.corpora.MmCorpus(articles_mm)
    lda = gensim.models.ldamodel.LdaModel(corpus=corpus, id2word=dictionary,
                                          num_topics=100, update_every=1,
                                          chunksize=10000, passes=1)
    lda.print_topics(100)
    lda.save('tmp/lda')

if __name__ == '__main__':
    main()
