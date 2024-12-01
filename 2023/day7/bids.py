CARD_VALUES = {
    "A": 12,
    "K": 11,
    "Q": 10,
    "J": 9,
    "T": 8,
    "9": 7,
    "8": 6,
    "7": 5,
    "6": 4,
    "5": 3,
    "4": 2,
    "3": 1,
    "2": 0,
}

CARD_VALUES_JOKER = {
    "A": 12,
    "K": 11,
    "Q": 10,
    "T": 9,
    "9": 8,
    "8": 7,
    "7": 6,
    "6": 5,
    "5": 4,
    "4": 3,
    "3": 2,
    "2": 1,
    "J": 0,
}


# parse the data file to get only the lines
def parse(filename):
    lines = []
    try:
        with open(filename, "r") as file:
            contents = file.readlines()
            lines = map(lambda n: n.rstrip(), contents)
            file.close()
    except OSError:
        print("Error in reading the file.")

    return list(lines)


# ways to score the hands for internal keeping
"""
  Five of a kind: 7
  Four of a kind: 6
  Full house: 5
  Three of a kind: 4
  Two pair: 3
  One pair: 2
  High card: 1
"""


# determine the type of the card, based on the above listing
def calculate_score(frequencies):
    if frequencies[0] == 5 or frequencies[0] == 4:
        return frequencies[0] + 2
    pairs = len(list(filter(lambda n: n == 2, frequencies)))
    has_three = 3 in frequencies
    if has_three and not pairs == 0:
        return 5
    elif has_three:
        return 4
    elif pairs == 2:
        return 3
    elif pairs == 1:
        return 2
    else:
        return 1


def score_joker(frequencies):
    jokers = frequencies[0]
    threes = len(list(filter(lambda n: n == 3, frequencies[1:])))
    pairs = len(list(filter(lambda n: n == 2, frequencies[1:])))
    singles = len(list(filter(lambda n: n == 1, frequencies[1:])))
    if jokers == 0:
        return calculate_score(sorted(frequencies, reverse=True))
    if (
        jokers == 5
        or jokers == 4
        or (jokers == 3 and pairs == 1)
        or (jokers == 2 and threes == 1)
    ):
        return 7
    elif jokers == 3:
        return 6
    if jokers == 2 and not singles == 3:
        return 6
    elif jokers == 2:
        return 4
    elif jokers == 1 and pairs == 2:
        return 5
    elif jokers == 1 and singles <= 1:
        return 6
    elif pairs == 2:
        return 5
    elif singles < 4:
        return 4
    else:
        return 2
    """
    if 4 in frequencies or any(x + jokers == 7 for x in frequencies[1:]):
        return 7
    elif any(x + jokers == 4 for x in frequencies[1:]):
        return 6
    
    if (not threes == 0) or pairs == 2 or (pairs == 1 and jokers >= 2):
        return 5
    elif pairs == 2 or 
    """


# compares which card is worth more
def is_larger(a, b):
    if a[1] > b[1]:
        return True
    elif a[1] < b[1]:
        return False
    else:
        i = 0
        while i < len(a[0]):
            if a[0][i] > b[0][i]:
                return True
            elif a[0][i] < b[0][i]:
                return False
            i += 1
        return False


def winnings_regular(lines):
    # stores cards, type, bid
    card_scores = []
    for hand in lines:
        split = hand.split()
        bid = int(split[1])
        cards = [CARD_VALUES[c] for c in split[0]]
        counts = [0] * 13
        for card in cards:
            counts[card] += 1
        hand_type = calculate_score(sorted(counts, reverse=True))
        # determine the appropriate position
        i = 0
        while i < len(card_scores):
            if is_larger((cards, hand_type), card_scores[i]):
                i += 1
            else:
                card_scores.insert(i, (cards, hand_type, bid))
                i = float("inf")
        if i == len(card_scores):
            card_scores.append((cards, hand_type, bid))

    winnings = 0
    i = 0
    while i < len(card_scores):
        winnings += card_scores[i][2] * (i + 1)
        i += 1
    return winnings


def main():
    lines = parse("day7/data.txt")
    winnings_normal = winnings_regular(lines)
    print(f"Total winnings: {winnings_normal}")
    card_gone_through = 0
    # stores cards, type, bid
    card_scores = []
    for hand in lines:
        split = hand.split()
        bid = int(split[1])
        cards = [CARD_VALUES_JOKER[c] for c in split[0]]
        counts = [0] * 13
        for card in cards:
            counts[card] += 1
        hand_type = score_joker(counts)
        # determine the appropriate position
        card_gone_through += 1
        i = 0
        while i < len(card_scores):
            if is_larger((cards, hand_type), card_scores[i]):
                i += 1
            else:
                card_scores.insert(i, (cards, hand_type, bid))
                i = float("inf")
        if i == len(card_scores):
            card_scores.append((cards, hand_type, bid))
    winnings = 0
    i = 0
    while i < len(card_scores):
        winnings += card_scores[i][2] * (i + 1)
        i += 1
    print(f"Winnings with joker cards: {winnings}")


# 246859611 too high
# 246073899 incorrect
# 246411915 incorrect
# 245840694 too low

main()
