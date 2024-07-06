from visualization.get_json_dict import DATABASE
from readability import Readability, exceptions


def get_readability_analysis():
    """ Get the sentiment analysis of the articles in the DATABASE.

    Returns:
        tuple: A tuple containing the labels and scores of the articles.
    """

    labels = []
    scores = []

    for i in range(len(DATABASE['articles']['fake-articles']['ids'])):
        try:
            labels.append('Fake')
            text = ' '.join([
                DATABASE['articles']['fake-articles']['titles'][i],
                DATABASE['articles']['fake-articles']['bodies'][i]
            ])
            r = Readability(text)

            score = r.coleman_liau().score

            scores.append(score)
        except exceptions.ReadabilityException as _:
            continue

    for i in range(len(DATABASE['articles']['real-articles']['ids'])):
        try:
            labels.append('Real')
            text = ' '.join([
                DATABASE['articles']['real-articles']['titles'][i],
                DATABASE['articles']['real-articles']['bodies'][i]
            ])

            r = Readability(text)

            score = r.coleman_liau().score

            scores.append(score)
        except exceptions.ReadabilityException as _:
            continue

    return labels, scores
