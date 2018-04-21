

class Workspace:

    """
        hubs is an object mapping names of spaces to their capacities
    """
    def __init__(self, hubs):
        self.hubCapacities = hubs
        self.hubUsage = [0 for _ in range(len(hubs))]

    def incrementHub(name):
        self.hubUsage[name] += 1

    def decrementHub(name):
        self.hubUsage[name] -= 1

    # loads the usage of a particular hub
    def loadUsage(name, usage):
        self.hugUsage[name] = usage

    # loads the usage of all hubs, give as an object {name: usage}
    def loadAllUsage(usages):
        for hub in usages:
            if hub in self.hubUsages:
                self.hubUsages[hub] = usages[hub]

    # returns the name of the hub with the most open spaces
    def bestHub():
        best = None
        maxSpaces = None
        for name in self.hubUsage:
            openSpots = self.hubCapacities[name] - self.hubUsage[name]
            if not best or openSpots > maxSpaces:
                best = name
                maxSpaces = openSpots
        return best

    # returns the name of the hub best fitting the number of desired open spots
    def bestFit(numDesired):
        best =  None
        bestDifference = None
        for name in self.hubUsage:
            openSpots = self.hubCapacities[name] - self.hubUsage[name]
            difference = openSpots - numDesired
            if not best or (openSpots >= numDesired and difference < bestDifference):
                best = name
                bestDifference = difference
        return best
