import os

BBC_ARTICLES = '.data/bbc-fulltext/bbc'

def load_articles(type, dir_path):
    """ Returns a list of tuples (article type, local path, text)
    """
    articles = []
    for p in os.listdir(dir_path):
        if p.endswith('.txt'):
            with open(os.path.join(dir_path, p), 'r') as f:
                txt = f.read()
            articles.append((type, p, txt))
    return articles

def load_all():
    articles = []
    for p in os.listdir(BBC_ARTICLES):
        if not p.endswith('.TXT'):
            articles  += load_articles(p, os.path.join(BBC_ARTICLES, p))
    return articles
