"""

    Author: Daniel Markusson
    

"""
import os
from visualization.tables.create_table import create_table
from visualization.tables.user_counts.generate_data.get_user_counts import get_user_counts


def create_user_counts_table():
    """ Create a table that shows the total number of users in the database, the total number of
        users who exclusively share fake articles, and the total number of users who exclusively 
        share real articles, along with that, large sharer counts of the same things are included.
    """
    user_counts = get_user_counts()
    independent_vars = ["", "All", "Fake", "Real",
                        "Large", "L. Fake", "L. Real"]
    dependent_vars = ["Counts"]
    values = [[user_counts["num-users"]],
              [user_counts["num-fake-users"]],
              [user_counts["num-real-users"]],
              [user_counts["num-large-sharers"]],
              [user_counts["num-large-fake-sharers"]],
              [user_counts["num-large-real-sharers"]]]
    create_table(os.path.join("users", "user_counts_table.png"), "User Counts",
                 independent_vars, dependent_vars, values)


if __name__ == "__main__":
    create_user_counts_table()
