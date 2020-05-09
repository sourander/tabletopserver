from games.raiders.modules.location import Location

class Board():
    def __init__(self, location_pool, bag):
        self.location_pool = location_pool
        self.locations = []
        self.bag = bag

        self.populate_locations()

    def populate_locations(self):
        for loc in self.location_pool:
            name, slots = self.location_pool[loc]

            # Initialize the location and add it to list
            this_location = Location(name, slots, self.bag)

            # Append the location also to the list so that we can access it easier
            self.locations.append(this_location)

    def report(self):
        for i, loc in enumerate(self.locations):
            name = loc.name
            
            line_to_print = name + ": \t"
            
            gaps_list = [6, 12, 17, 20, 23]

            if i in gaps_list:
                print(" ")

            # Create a list of token names 
            # e.g. ['Valkyrie', 'Gold']
            tokens = []
            for token in loc.tokens:
                tokens.append(token.name)

            # Find all unique names and count them
            uniques = set(tokens)
            for unique in uniques:
                c = tokens.count(unique)
                addition = "{}x {}    ".format(c, unique)
                line_to_print = line_to_print + addition

            print(line_to_print)
            
    def get_locations(self, split):
        """
        Returns all locations in format:
        locations = [ 
                      { "Fortress": ["Gold, "Cows"] },
                      { "name": [tokens] } 
                    ]
        """

        locations_container = []

        for i, stop in enumerate(split):
            locations = []

            if i == 0:
                start = 0
            else:
                start = sum(split[:i])
                stop = start + stop

            print(f"Iteration {i}. Start:{start}, Stop:{stop}")

            batch = self.locations[start:stop]

            print(len(batch))

            for loc in batch:
                location = { loc.name: loc.tokens}
                locations.append(location)

            locations_container.append(locations)

        return locations_container
            
        