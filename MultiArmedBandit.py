import random
class Cafeteria():
    # set up instance variables for the cafeteria class
    def __init__(self, name, mean, std):
        self.name = name
        self.mean = mean
        self.std = std
        self.happiness = 0
        self.visitedTimes = 0

    # adds the values of happiness to that specific cafeteria when visited
    def generateHappiness(self):
        randomGenerated = random.normalvariate(self.mean,self.std)
        self.happiness += randomGenerated
        self.visitedTimes += 1

    # helper function that returns the happiness level of the cafeteria
    def getHappiness(self):
        return self.happiness

    # compares the 3 cafeteria and returns the cafeteria with the highest average happiness
    # level
    def compareHappiness(self, x, y):
        bestCafe = self
        if (bestCafe.happiness/bestCafe.visitedTimes < x.happiness/x.visitedTimes):
            bestCafe = x
        if (bestCafe.happiness/bestCafe.visitedTimes < y.happiness/y.visitedTimes):
            bestCafe = y
        return bestCafe


# define the basic characteristic of each cafeteria
# c1 should always be the cafeteria with the lowest mean
# c3 should always be the cafeteria with the highest mean
c1_mean, c1_dev = 9, 3
c2_mean, c2_dev = 7, 5
c3_mean, c3_dev = 11, 7

# return the total happiness for exploreOnly for 1 trial
def exploreOnly():
        # Instantiate cafeteria objects
        c1 = Cafeteria('c1', c1_mean, c1_dev)
        c2 = Cafeteria('c2', c2_mean, c2_dev)
        c3 = Cafeteria('c3', c3_mean, c3_dev)
        for days in range(100):
            # generate happiness
            c1.generateHappiness()
            c2.generateHappiness()
            c3.generateHappiness()
        # returns the total happiness for 1 trial
        return (c1.getHappiness()+c2.getHappiness()+c3.getHappiness())

# return the total happiness for exploitOnly for 1 trial
def exploitOnly():
        # Instantiate cafeteria objects
        c1 = Cafeteria('c1', c1_mean, c1_dev)
        c2 = Cafeteria('c2', c2_mean, c2_dev)
        c3 = Cafeteria('c3', c3_mean, c3_dev)
        # generate the happiness for the first 3 days
        c1.generateHappiness()
        c2.generateHappiness()
        c3.generateHappiness()
        # selects the best cafeteria based on the first 3 days
        bestCafe = c1.compareHappiness(c2,c3)
        for days in range(297):
            # use the same cafeteria for the rest of the 297 days
            bestCafe.generateHappiness()
        # add the the happiness of this trial
        return (c1.getHappiness() + c2.getHappiness() + c3.getHappiness())

# return the total happiness for egreedy for t trial(s)
def eGreedy(e):
    # Instantiate cafeteria objects
    c1 = Cafeteria('c1', c1_mean, c1_dev)
    c2 = Cafeteria('c2', c2_mean, c2_dev)
    c3 = Cafeteria('c3', c3_mean, c3_dev)
    cafeList = [c1, c2, c3]
    # visit each of the three cafeteria for the first 3 days
    c1.generateHappiness()
    c2.generateHappiness()
    c3.generateHappiness()
    for days in range (297):
        # generate a random number between 0 and 100
        r = random.random()
        # random selection of cafeteria
        if r < e:
            randCafe = cafeList[(int)(random.random()*3)]
            randCafe.generateHappiness()
        else:
        # selection based on the average happiness of the cafeteria that the agent have experienced
            bestCafe = c3.compareHappiness(c2,c1)
            bestCafe.generateHappiness()
    # add the total happiness of the trial to the result list
    return (c1.getHappiness() + c2.getHappiness() + c3.getHappiness())

def simulate(t,ePercent):
    # e set the e value
    e = ePercent / 100
    # expected Values
    optimumHappiness = c3_mean * 300
    exploreHappiness = 100 * c1_mean + 100 * c2_mean + 100 * c3_mean
    exploitHappiness = c3_mean + c2_mean + c1_mean + c3_mean * 297
    egreedyHappiness = (int)(c3_mean * (1-e) * 300 + c3_mean * e/3 * 300 + c2_mean * (e /3) * 300 + c1_mean * (e / 3) * 300)

    # calculates the average of each function
    exploitResult = 0
    exploreResult = 0
    greedyResult = 0
    # runs the functions t trials
    for trial in range(t):
        exploitResult += exploitOnly()
        exploreResult += exploreOnly()
        greedyResult += eGreedy(e)
    exploreResult /= t
    exploitResult /= t
    greedyResult /= t

    # prints out out the necessary information to the console
    print('----------------------------------------')
    print("Optimum Happiness: " + (str)(optimumHappiness))
    print('----------------------------------------')
    print("----------------------------------------\nExplore Only Stats\n----------------------------------------")
    print("Expected Total Happiness: " + (str)(exploreHappiness))
    print("Expected Total Regret: " + (str)(optimumHappiness - exploreHappiness))
    print("Average Total Happiness: " + (str)(exploreResult))
    print("Average Total Regret: " + (str)(optimumHappiness - exploreResult))
    print("\n----------------------------------------\nExploit Only Stats\n----------------------------------------")
    print("Expected Total Happiness: " + (str)(exploitHappiness))
    print("Expected Total Regret: " + (str)(optimumHappiness - exploitHappiness))
    print("Average Total Happiness: " + (str)(exploitResult))
    print("Average Total Regret: " + (str)(optimumHappiness - exploitResult))
    print("\n----------------------------------------\neGreedy Stats\n----------------------------------------")
    print("Expected Total Happiness: " + (str)(egreedyHappiness))
    print("Expected Total Regret: " + (str)(optimumHappiness - egreedyHappiness))
    print("Average Total Happiness: " + (str)(greedyResult))
    print("Average Total Regret: " + (str)(optimumHappiness - greedyResult))

# simulate(p1,p2) runs the simulation p1 number of times with the e value of p2
simulate(1000,12)




