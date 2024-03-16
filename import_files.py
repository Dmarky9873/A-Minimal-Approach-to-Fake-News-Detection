import pandas as pd


def getData():
    data = dict()
    data['real'] = pd.read_csv("./raw/BuzzFeed_real_news_content.csv")
    data['fake'] = pd.read_csv("./raw/BuzzFeed_fake_news_content.csv")

    return data


if __name__ == '__main__':
    data = getData()

    print(data['real'].head())
    print(data['fake'].head())
