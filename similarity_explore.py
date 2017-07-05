from gensim import corpora, models, similarities


def main():
    dictionary = corpora.Dictionary.load('tmp/articles.dict')
    corpus = corpora.MmCorpus('tmp/articles.mm')
    # 2-dimensional LSI space
    lsi = models.LsiModel(corpus, id2word=dictionary, num_topics=2)


if __name__ == '__main__':
    main()
