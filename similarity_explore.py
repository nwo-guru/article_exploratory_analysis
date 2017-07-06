import os
from gensim import corpora, models, similarities
from config import articles_mm, articles_dict, articles_index
from data_clean import clean_text
from load_bbc_articles import load_all_bbc_articles


def main():
    dictionary = corpora.Dictionary.load(articles_dict)
    corpus = corpora.MmCorpus(articles_mm)
    lsi = models.LsiModel(corpus, id2word=dictionary, num_topics=300)
    index = similarities.MatrixSimilarity(lsi[corpus])

    #text = r'''
    #        Algeria hit by further gas riots\n\nAlgeria suffered a weekend of violent protests against government plans to raise gas prices, local press reports.\n\nDemonstrators in a number of regions blocked roads, attacked public buildings and overturned vehicles, newspapers including El Watan reported. The price of butane gas, a vital fuel for cooking, has risen to 200 dinars ($2.77) per canister from 170 dinars. Even before the hike, failing economic conditions had been fanning resentment in some of Algeria's poorest regions.\n\nDemonstrators took to the streets last week when the cost change was first announced, but police seemed to have restored order. According to local press reports, trouble flared up again on Saturday and carried on into Sunday. El Watan said that a number of hot spots centred on the villages and towns close to Bouira, about 100 kilometres (60 miles) south of the capital Algiers. Among the other main areas affected were the western Tiaret region and Sidi Ammar in the east of the country, Agence France Presse (AFP) reported. Riots also flared up in the Maghnia region close to the border with Morocco in the west, AFP said. Butane gas and fuel oil are used as the main source of fuel to heat homes and cook food in Algeria's remote mountain areas.
    #    '''

    text = '''
        'Commons hunt protest charges\n\nEight protesters who stormed the House of Commons chamber during a debate on the Hunting Bill have been charged with disorderly conduct.\n\nThe men were arrested in September after bursting into the chamber causing a hunting ban debate to be halted. Those charged included Otis Ferry, the 22-year-old son of rock star Bryan Ferry and Luke Tomlinson, 27, a close friend of princes William and Harry. They were charged under Section 5 of the Public Order Act, police said.\n\nFive of the eight men held an impromptu news conference outside Charing Cross Police Station on Monday evening, after the charges were formerly put to them. The men\'s solicitor Matthew Knight, said that at no time had it occurred to the men that they were committing a criminal offence.\n\n"There is no offence of trespassing in the House of Commons - it is not a criminal offence," he said. "If Parliament wanted to make entering the House of Commons chamber on foot a criminal offence it should have done so, but it can\'t do so retrospectively. "We are not prosecuted for that. We are prosecuted for a Public Order Act offence. We are not guilty of it." They will appear at Bow Street Magistrates\' Court on 21 December, a police spokesman said. Otis Ferry, a former Eton pupil and joint leader of the South Shropshire Hunt, said: "I have no regrets. "We have done nothing wrong beyond the obvious which was to stand up for our rights and not act like a sheep like the rest of the country." One of the men, David Redvers, 34, from Hartpury, Gloucestershire, said he and the other seven protesters would plead not guilty to the charges.\n\nThe other protesters are John Holliday, 37, a huntsman from Ledbury, Herefordshire, Robert Thame, 34, who plays polo with Princes Charles in Team Highgrove, auctioneer Andrew Elliot, 42, from Bromesberrow, near Ledbury, point-to-point jockey Richard Wakeham, 34, from York, and former royal chef Nick Wood, 41. The 15 September protest came on the same day as a huge pro-hunting demonstration in Parliament Square. Four of the men ran out from behind the speaker\'s chair while another wrestled past a doorkeeper from a different entrance. The five tried to confront MPs before they were bundled out of the chamber and later led away handcuffed by police. Three others had been intercepted by security staff as they tried to join the five in the chamber.\n\nSpeaker Michael Martin later said the men had used a forged letter to gain access to the House of Commons and had been helped to get close to the chamber by a parliamentary pass holder. In November, the use of the Parliament Act meant a total ban on hunting with dogs in England and Wales. However, many pro-hunt activists remained defiant after the law was passed, saying they would ignore the ban and continue to hunt. Last week, the Countryside Alliance said more than 250 hunts would meet legally the day after the ban on hunting with dogs comes into force. The alliance said the 19 February meets would show the new law was "impossibly difficult to determine" and open to different interpretations.\n'
    '''

    text = 'protests riots'

    cleaned_txt = clean_text(text)

    q1 = lsi[dictionary.doc2bow(cleaned_txt)]

    sims = index[q1]
    sims = sorted(enumerate(sims), key=lambda item: -item[1])
    articles = load_all_bbc_articles()
    for n in range(100):
        print(sims[n + 1][0], articles[sims[n + 1][0]])

if __name__ == '__main__':
    main()
