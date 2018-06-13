from itertools import *

# Score categories
# Change the values as you see fit
YACHT = 12
ONES = 1
TWOS = 2
THREES = 3
FOURS = 4
FIVES = 5
SIXES = 6
FULL_HOUSE = 7
FOUR_OF_A_KIND = 8
LITTLE_STRAIGHT = 9
BIG_STRAIGHT = 10
CHOICE = 11


def score(dice, category):
    dice.sort()
    result = 0

    if category < 7:

        for index, num in enumerate(dice):
            if dice[index] == category:
                result += category

    elif category == 7:

        s = set(dice)
        if len(s) == 2:
            for num in dice:
                result += num

    elif category == 8:

        if dice[0] == dice[3] or dice[1] == dice[4]:
            result += 4 * dice[2]

    elif category == 9:

        s = set(dice)
        if len(s) == 5 and dice[0] == 1 and dice[4] != 6:
            result = 30

    elif category == 10:

        s = set(dice)
        if len(s) == 5 and dice[0] == 2:
            result = 30

    elif category == 11:

        for num in dice:
            result += num

    elif category == 12:

        group = groupby(dice)
        if next(group, True) and not next(group, False):
            result = 50

    return result













