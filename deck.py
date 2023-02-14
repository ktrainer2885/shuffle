import card


class Deck:
    deck = []
    middleIndex = ""

    def __init__(self, size):
        halfDeck = (size // 2) + 1
        self.middleIndex = halfDeck -1

        for i in range(1, halfDeck):
            practiceCard = card.Card(i, "L")
            self.deck.append(practiceCard)

        for i in range(halfDeck, size + 1):
            practiceCard = card.Card(i, "R")
            self.deck.append(practiceCard)

    def shuffle(self):
        left = self.deck[:self.middleIndex]
        right = self.deck[self.middleIndex:]

        self.deck.clear()

        for i in range(len(left)):
            self.deck.append(left[i])
            if i < len(right):
                self.deck.append(right[i])

    def print(self):
        for i in range(len(self.deck)):
            self.deck[i].print()
