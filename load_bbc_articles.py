import os
from config import bbc_articles

def load_articles_in_folder(type, dir_path):
    """ Returns a list of tuples (article type, local path, text)
    """
    articles = []
    for p in os.listdir(dir_path):
        if p.endswith('.txt'):
            with open(os.path.join(dir_path, p), 'r') as f:
                txt = f.read()
            articles.append((type, p, txt))
    return articles

def load_all_bbc_articles():
    articles = []
    for p in os.listdir(bbc_articles):
        if not p.endswith('.TXT'):
            articles += load_articles_in_folder(p, os.path.join(bbc_articles, p))
    print('\n'.join([a[1] + ' ' + a[0] for a in articles[:2000:250]]))
    return articles
