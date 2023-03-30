from __future__ import annotations
from typing import Any, Optional
import csv
import random
# Comment out this line when you aren't using check_contracts
from python_ta.contracts import check_contracts
import tree
GAME_START_MOVE = '*'


def load_game_tree(games_file: dict) -> tree.GameTree:
    """Return a new game tree based on games_file.

    Preconditions:
        - games_file refers to a csv file in the format described on the assignment handout

    Implementation hints:
        - You can review Tutorial 4 for how we read CSV files in Python.
        - You can call tuple(s) to convert a string s into a tuple of characters.
        - You can *ignore* type errors that PyCharm might display if you're mixing str
          and tuple[str, ...] in a list.
        - We strongly recommend testing this function with the smaller "single_moves.csv"
          and "small_sample.csv" before jumping to "guesser_wins.csv".
          (All of these files are located under data/games.)
    """
    #  3-4 main bundles of genres  Will have to do it by hand.
    genres = games_file['Genres']

    Tree = tree.GameTree()
    set1 = set()
    set2 = set()
    set3 = set()
    Tree.add_subtree(tree.GameTree(set1))
    Tree.add_subtree(tree.GameTree(set2))
    Tree.add_subtree(tree.GameTree(set3))
    # make the first bundles to be a string of all many genres
