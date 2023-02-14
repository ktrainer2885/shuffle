class Card:
    value = ""
    type = ""

    def __init__(self, value, type):
        self.value = value
        self.type = type

    def print(self):
        print("Value: " + str(self.value) + ", Type: " + self.type)
