import pandas as pd
from rich_terminal import Rich_Terminal


def getDataFrames(showinfo=True):
    if showinfo:
        rt = Rich_Terminal()

    data = dict()
    buzzfeedDF_fake = pd.read_csv("./raw/BuzzFeed_fake_news_content.csv")
    buzzfeedDF_real = pd.read_csv("./raw/BuzzFeed_real_news_content.csv")
    politifactDF_fake = pd.read_csv("./raw/PolitiFact_fake_news_content.csv")
    politifactDF_real = pd.read_csv("./raw/PolitiFact_real_news_content.csv")
    if showinfo:
        print(rt.getString_MINIMAL(
            "Successfully retrieved both fake and real dataframes.") + " \nInformation:\n")
        print("BuzzFeed_real size: " +
              rt.getString_MAJOR(buzzfeedDF_real.size))
        print("BuzzFeed_fake size:", rt.getString_MAJOR(buzzfeedDF_fake.size))
        print("PolitiFact_real size:", rt.getString_MAJOR(politifactDF_real.size))
        print("PolitiFact_fake size:", rt.getString_MAJOR(politifactDF_fake.size))
        print(rt.PAGE_BREAK)

    realDFs = [buzzfeedDF_real, politifactDF_real]
    fakeDFs = [buzzfeedDF_fake, politifactDF_fake]

    data['real'] = pd.concat(realDFs)
    data['fake'] = pd.concat(fakeDFs)

    if showinfo:
        print(rt.getString_MINIMAL(
            "Successfully concatinated both fake and real dataframes.") + "\nInformation:\n")
        print("Dataframe_real size: " + rt.getString_MAJOR(data['real'].size))
        print("Dataframe_fake size: " + rt.getString_MAJOR(data['fake'].size))

    return data


if __name__ == '__main__':
    data = getData(showinfo=True)

    # print(data['real'].head())
    # print(data['fake'].head())
