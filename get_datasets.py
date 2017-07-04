""" Creates local ./data directory and downloads training data from the web
"""
import os
import urllib.request
import shutil

DATA_DIR = '.data'
# UCI News Aggregator Data Set, https://archive.ics.uci.edu/ml/datasets/News+Aggregator
NEWS_AGG_DATASET = 'https://archive.ics.uci.edu/ml/machine-learning-databases/00359/NewsAggregatorDataset.zip'


def main():
    # Make data dir
    if not os.path.isdir(DATA_DIR):
        os.mkdir(DATA_DIR)
    # Download news agg dataset zip
    zip_out = os.path.join(DATA_DIR, 'NewsAggregatorDataset.zip')
    if not os.path.isfile(zip_out):
        with urllib.request.urlopen(NEWS_AGG_DATASET) as response, open(zip_out, 'wb') as out_file:
            shutil.copyfileobj(response, out_file)

if __name__ == '__main__':
    main()
