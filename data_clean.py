import os
import pickle
from load_bbc_articles import load_all_bbc_articles


def main():
    articles = load_all_bbc_articles()
    article_text = [a[1] for a in articles]

    # Clean stuff like the gensim quickstart tutorial
    with open('stopwords.txt', 'r') as f:
        stopwords = f.readlines()

    print(stopwords)


def load_articles():
    article_pickle = '.data/articles.p'
    if not os.path.isfile(article_pickle):
        with open(article_pickle, 'rb') as f:
            articles = pickle.load(f)
    else:
        articles = load_all_bbc_articles()
        with open(article_pickle, 'wb') as f:
            pickle.dump(articles, article_pickle)
    return articles

if __name__ == '__main__':
    main()
