import card


class Deck:
    deck = []

    def __init__(self, size):
        halfDeck = size // 2

        for i in range(1, halfDeck + 1):
            practiceCard = card.Card(i, "L")
            self.deck.append(practiceCard)

        for i in range(1, halfDeck):
            practiceCard = card.Card(i, "R")
            self.deck.append(practiceCard)

    def shuffle(self):
        middleIndex = len(self.deck)
        left = self.deck[:middleIndex]
        right = self.deck[middleIndex:]

        self.deck.clear()

        for i in range(1, len(left)):
            self.deck.append(left[i])
            if i < len(right):
                self.deck.append(right[i])

    def print(self):
        for i in range(len(self.deck)):
            self.deck[i].print()
