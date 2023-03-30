from __future__ import annotations
from typing import Any, Optional
import csv
import random
# Comment out this line when you aren't using check_contracts
from python_ta.contracts import check_contracts

GAME_START_MOVE = '*'


class GameNode:
    """
    A GameNode class that represents a game.

    Instance Attributes:
        - name: the name of the Game
        - rating: the rating of the game represented as a number.
        - mature: defines if the game for mature audiences or not
        - achievements: Are there any achievements in the game?
        - min_req: the minimum requirements for the game
        - rec_req: the recommended requirements for the game
        - price: the price of the game as a float.
    """
    name: str
    rating: int
    mature: bool
    achievements: bool
    min_req: str
    rec_req: str
    price: float


class GameTree:
    """A decision tree for our project.

    There are 2 types of nodes:
        - Game Node
        - a usual node represented as a simple string.
        - a "bundle" node which is a set of genres

    Instance Attributes:
        - node: the node, a root which is either a parameter or a game in our decision tree

    Representation Invariants:

    """
    node: str | GameNode

    # Private Instance Attributes:
    #  - _subtrees: The subtrees. str refers to the name of the game
    _subtrees: dict  # dict[str | tuple[str, ...], GameTree]

    def __init__(self, node: GameNode | str = GAME_START_MOVE) -> None:
        """Initialize a new game tree.
        Note that this initializer uses optional arguments.
        """
        self.node = node
        self._subtrees = {}

    def get_subtrees(self) -> list[GameTree]:
        """Return the subtrees of this game tree."""
        return list(self._subtrees.values())

    def find_subtree_by_move(self, move: str | tuple[str, ...]) -> Optional[GameTree]:
        """Return the subtree corresponding to the given move.

        Return None if no subtree corresponds to that move.
        """
        if move in self._subtrees:
            return self._subtrees[move]
        else:
            return None

    def __len__(self) -> int:
        """Return the number of items in this tree."""
        # Note: no "empty tree" base case is necessary here.
        # Instead, the only implicit base case is when there are no subtrees (sum returns 0).
        return 1 + len(self._subtrees)

    def __str__(self) -> str:
        """Return a string representation of this tree.
        """
        return self._str_indented(0)

    def _str_indented(self, depth: int) -> str:
        """Return an indented string representation of this tree.

        The indentation level is specified by the <depth> parameter.

        You MAY change the implementation of this method (e.g. to display different instance attributes)
        as you work on this assignment.

        Preconditions:
            - depth >= 0
        """

    def add_subtree(self, subtree: GameTree) -> None:
        """Add a subtree to this game tree."""
        self._subtrees[subtree.node] = subtree






if __name__ == '__main__':
    import doctest

    doctest.testmod(verbose=True)

    # When you are ready to check your work with python_ta, uncomment the following lines.
    # (In PyCharm, select the lines below and press Ctrl/Cmd + / to toggle comments.)
    # You can use "Run file in Python Console" to run PythonTA,
    # and then also test your methods manually in the console.
    # import python_ta
    # python_ta.check_all(config={
    #     'max-line-length': 120
    # })
