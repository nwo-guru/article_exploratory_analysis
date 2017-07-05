import os
import pickle
from gensim import corpora
from load_bbc_articles import load_all_bbc_articles


def main():
    # Load texts from bbc articles
    articles = load_all_bbc_articles()
    full_texts = [a[2] for a in articles]
    # Clean stuff like the gensim quickstart tutorial
    with open('stopwords.txt', 'r') as f:
        stopwords = [w.strip() for w in f.readlines()]
    # Remove stopwords
    texts = [[w for w in text.lower().split() if w not in stopwords]
             for text in full_texts]
    dictionary = corpora.Dictionary(texts)
    dictionary.save('/tmp/articles.dict')
    print(dictionary)



if __name__ == '__main__':
    main()
