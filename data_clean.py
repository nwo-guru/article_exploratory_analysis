from gensim import corpora
from load_bbc_articles import load_all_bbc_articles
from config import articles_dict, articles_mm

def main():
    # Load texts from bbc articles
    articles = load_all_bbc_articles()
    for a in articles:
        if 'protest' in a[2].lower():
            print(a)
    full_texts = [a[2] for a in articles]
    clean_and_save(full_texts)

def load_stopwords():
    with open('stopwords.txt', 'r') as f:
        stopwords = [w.strip() for w in f.readlines()]
    return stopwords

def clean_text(text, stopwords=None):
    if not stopwords:
        stopwords = load_stopwords()
    return [w for w in text.lower().split() if w not in stopwords]

def clean_and_save(full_texts):
    """ Clean and save a list of texts for later loading and processing
    """
    # Remove stopwords
    stopwords = load_stopwords()
    texts = [clean_text(text, stopwords) for text in full_texts]
    for n, text in enumerate(texts):
        if 'riot' in text:
            print(n, text)
    # Compute dictionary and corpus and save for reuse
    dictionary = corpora.Dictionary(texts)
    dictionary.save(articles_dict)
    corpus = [dictionary.doc2bow(text) for text in texts]
    corpora.MmCorpus.serialize(articles_mm, corpus)


if __name__ == '__main__':
    main()
