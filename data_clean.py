from load_bbc_articles import load_all_bbc_articles

articles = load_all_bbc_articles()
article_text = [a[1] for a in articles]

# Clean stuff like the gensim quickstart tutorial
# https://radimrehurek.com/gensim/tut1.html
stoplist = set('')