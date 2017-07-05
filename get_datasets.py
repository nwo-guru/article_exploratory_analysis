""" Create local ./data directory and download training data from the web
"""
import os
import zipfile
import shutil
from urllib.request import urlopen

DATA_DIR = 'data'
# UCI News Aggregator Data Set, https://archive.ics.uci.edu/ml/datasets/News+Aggregator
NEWS_AGG_DATASET = 'https://archive.ics.uci.edu/ml/machine-learning-databases/00359/NewsAggregatorDataset.zip'
BBC_FULLTEXT = 'http://mlg.ucd.ie/files/datasets/bbc-fulltext.zip'

def main():
    # Make data dir
    if not os.path.isdir(DATA_DIR):
        os.mkdir(DATA_DIR)
    # Download news agg dataset zip
    zip_out = os.path.join(DATA_DIR, 'bbc-fulltext.zip')
    if not os.path.isfile(zip_out):
        with urlopen(BBC_FULLTEXT) as response, open(zip_out, 'wb') as out_file:
            shutil.copyfileobj(response, out_file)
    # Unzip the data
    unzipped_dir = os.path.join(DATA_DIR, 'bbc-fulltext')
    if not os.path.isdir(unzipped_dir):
        with zipfile.ZipFile(zip_out, 'r') as z_file:
            z_file.extractall(unzipped_dir)


if __name__ == '__main__':
    main()

