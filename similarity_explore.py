import os
from gensim import corpora, models, similarities
from config import articles_mm, articles_dict, articles_index
from data_clean import clean_text
from load_bbc_articles import load_all_bbc_articles


def main():
    dictionary = corpora.Dictionary.load(articles_dict)
    corpus = corpora.MmCorpus(articles_mm)
    lsi = models.LsiModel(corpus, id2word=dictionary, num_topics=4)
    index = similarities.MatrixSimilarity(lsi[corpus])

    text = r'''
        Halo 2 sells five million copies\n\nMicrosoft is celebrating bumper sales of its Xbox sci-fi shooter, Halo 2.\n\nThe game has sold more than five million copies worldwide since it went on sale in mid-November, the company said. Halo 2 has proved popular online, with gamers notching up a record 28 million hours playing the game on Xbox Live. According to Microsoft, nine out of 10 Xbox Live members have played the game for an average of 91 minutes per session.\n\nThe sequel to the best-selling Need for Speed: Underground has inched ahead of the competition to take the top slot in the official UK games charts. The racing game moved up one spot to first place, nudging GTA: San Andreas down to second place. Halo 2 dropped one place to five, while Half-Life 2 fell to number nine. Last week's new releases, GoldenEye: Rogue Agent and Killzone, both failed to make it into the top 10, debuting at number 11 and 12 respectively.\n\nRecord numbers of Warcraft fans are settling in the games online world. On the opening day of the World of Warcraft massive multi-player online game more than 200,000 players signed up to play. On the evening of the first day more than 100,000 players were in the world, forcing Blizzard to add another 34 servers to cope with the influx. The online game turns the stand alone Warcraft games into a persistent world that players can inhabit not just visit\n\nEurope's gamers could be waiting until January to hear when they can get their mitts on Nintendo's handheld device, Nintendo DS, says gamesindustry.biz. David Yarnton, Nintendo UK general manager, told a press conference to look out for details in the New Year. Its US launch was on Sunday and it goes on sale in Japan on 2 December. Nintendo has a 95% share of the handheld gaming market and said it expected to sell around five million of the DS by March 2005.\n
        '''

    cleaned_txt = clean_text(text)

    q1 = lsi[dictionary.doc2bow(cleaned_txt)]

    sims = index[q1]
    sims = sorted(enumerate(sims), key=lambda item: -item[1])
    articles = load_all_bbc_articles()
    for n in range(100):
        print(sims[n + 1][0], articles[sims[n + 1][0]])

if __name__ == '__main__':
    main()
