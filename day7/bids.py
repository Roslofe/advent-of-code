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


def main():
    lines = parse("day7/data.txt")
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
    print(f"Total winnings: {winnings}")


main()
