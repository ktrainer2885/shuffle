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

# The shuffle is just a basic split in half and recombining it with the let deck starting first.
    # Make the left and right deck switch places every other shuffle
    #make a method to shuffle multiple times
    # add the randomnessof shuffling. not 1 to 1, but 2 to 3 , 2 to  1, 5 to  3 etc
    # It is never a perfect shuffle of 1 card from left and right
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
