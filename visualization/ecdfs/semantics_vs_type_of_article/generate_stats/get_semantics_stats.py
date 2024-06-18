# import libraries
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from visualization.get_json_dict import DATABASE


nltk.download('all', quiet=True)


def preprocess_text(text):
    """ Preprocess the text by tokenizing, removing stop words and lemmatizing.

    Args:
        text (str): The text to preprocess.

    Returns:
        str: The preprocessed text.
    """

    # Tokenize the text

    tokens = word_tokenize(text.lower())

    # Remove stop words

    filtered_tokens = [
        token for token in tokens if token not in stopwords.words('english')]

    # Lemmatize the tokens

    lemmatizer = WordNetLemmatizer()

    lemmatized_tokens = [lemmatizer.lemmatize(
        token) for token in filtered_tokens]

    # Join the tokens back into a string

    processed_text = ' '.join(lemmatized_tokens)

    return processed_text


def get_semantic_score(text: str):
    """ Get the sentiment score of the given text.

    Args:
        text (str): The text to analyze.

    Returns:
        float: The sentiment score of the text.
    """

    analyzer = SentimentIntensityAnalyzer()

    return analyzer.polarity_scores(preprocess_text(text))['compound']


def get_semantic_analysis():

    labels = []
    scores = []

    for i in range(len(DATABASE['articles']['fake-articles']['ids'])):
        labels.append('Fake')
        text = ' '.join([
            DATABASE['articles']['fake-articles']['titles'][i],
            DATABASE['articles']['fake-articles']['bodies'][i]
        ])

        score = get_semantic_score(text)

        scores.append(score)

    for i in range(len(DATABASE['articles']['real-articles']['ids'])):
        labels.append('Real')
        text = ' '.join([
            DATABASE['articles']['real-articles']['titles'][i],
            DATABASE['articles']['real-articles']['bodies'][i]
        ])

        score = get_semantic_score(text)

        scores.append(score)

    return labels, scores


def main():
    get_semantic_analysis()


if __name__ == "__main__":
    main()
