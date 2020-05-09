class Location():
    def __init__(self, name, slots, bag):
        self.name = name
        self.slots = slots
        self.tokens = []
        self.bag = bag

        self.populate()

    def populate(self):
        # For each slots in the location, 
        # get a token from the Bag.
        for i in range(0, self.slots):
            token = self.bag.draw_token()
            self.tokens.append(token)

    def __repr__(self):
        return "{} with items {}".format(self.name, self.tokens)