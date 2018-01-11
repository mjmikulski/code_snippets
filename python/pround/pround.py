from math import ceil
from random import random as r


def pround(x):
    """
    Probabilistic round.
    Applied on a sample preserves its mean if sample is enough big.

    """

    return ceil(x - r())