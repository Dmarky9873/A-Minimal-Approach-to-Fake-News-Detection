"""


    Author: Daniel Markusson


"""


import os
from definitions import ROOT_DIR


def get_json_location(name="cleaned_data"):
    """
        TODO: Document
    """
    if ".json" not in name:
        name = str(name) + ".json"

    path = os.path.join(ROOT_DIR, name)

    if os.path.exists(path):
        return path

    raise FileNotFoundError(f"JSON file {name} does not exist.")
