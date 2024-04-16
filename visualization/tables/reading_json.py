"""


    Author: Daniel Markusson


"""
import simplejson as json
from file_retrieval import get_json_location

with open(get_json_location("cleaned_data"), encoding="UTF-8") as f:
    DATABASE = json.load(f)


def get_num_authors():
    authors = {}

    print("realones", DATABASE["articles"]["real-articles"]["authors"])
    print("fakeones", DATABASE["articles"]["fake-articles"]["authors"])


def main():
    get_num_authors()


if __name__ == "__main__":
    main()
