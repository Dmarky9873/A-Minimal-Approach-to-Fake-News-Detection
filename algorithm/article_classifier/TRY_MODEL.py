"""

    Author: Daniel Markussons

"""

import sys
import os
from rich.console import Console
import pandas as pd
import xgboost as xgb
from definitions import THEME, LOGO

CONSOLE = Console(theme=THEME)


def intro():
    """ Introduction to the user
    """
    os.system("clear")
    CONSOLE.print("[info]Loading model...[/info]")

    model = xgb.Booster()
    model.load_model('./algorithm/article_classifier/model.ubj')

    CONSOLE.print("[success]Model loaded![/success]\n\n")
    CONSOLE.print(LOGO, style="bright_white")
    while True:
        CONSOLE.print("[bold]{enter}: try model\nq: quit[/bold]")
        selection = input()
        if selection == "":
            CONSOLE.print("[info]Enter the number of shares: [/info]")
            shares = int(input())
            CONSOLE.print("[info]Enter the number of authors: [/info]")
            num_authors = int(input())
            CONSOLE.print("[info]Enter the sentiment score: [/info]")
            sentiment_score = float(input())
            CONSOLE.print("[info]Enter the length of the article: [/info]")
            length = int(input())
            predict(model, shares, num_authors, sentiment_score, length)
        elif selection.lower() == "q":
            sys.exit(0)


def predict(model: xgb.XGBClassifier, shares: int, num_authors: int, sentiment_score: float, length: int):
    """ Predicts if an article is fake or real

    Args:
        model (xgb.XGBClassifier): The model to use for prediction
        shares (int): The number of shares the article had
        num_authors (int): The number of authors of the article
        sentiment_score (float): The sentiment score of the article
        length (int): The length of the article
    """
    data = [[length, shares, num_authors, sentiment_score]]
    columns = [
        'length', 'shares', 'num_authors', 'sentiment-score'
    ]

    to_predict_df = pd.DataFrame(data=data, columns=columns)

    to_predict = xgb.DMatrix(to_predict_df)

    prediction = model.predict(to_predict)

    if round(prediction[0]) == 1:
        CONSOLE.print("[alert]The article is fake![/alert]")
    else:
        CONSOLE.print("[success]The article is real![/success]")


def main():
    """
        Main method to be run if this file is ran.
    """
    intro()


if __name__ == "__main__":
    main()
