from gensim import corpora
from load_bbc_articles import load_all_bbc_articles


def main():
    # Load texts from bbc articles
    articles = load_all_bbc_articles()
    full_texts = [a[2] for a in articles]
    # Remove stopwords
    with open('stopwords.txt', 'r') as f:
        stopwords = [w.strip() for w in f.readlines()]
    texts = [[w for w in text.lower().split() if w not in stopwords]
             for text in full_texts]
    # Compute dictionary and corpus and save for reuse
    dictionary = corpora.Dictionary(texts)
    dictionary.save('tmp/articles.dict')
    corpus = [dictionary.doc2bow(text) for text in texts]
    corpora.MmCorpus.serialize('tmp/articles.mm', corpus)


if __name__ == '__main__':
    main()
