import random
class cafeteria():
    def __init__(self, name, mean, std):
        self.name = name
        self.mean = mean
        self.std = std

    def happiness(self):
        return random.normalvariate(self.mean,self.std)

# instantiate cafeteria objects
c1_mean, c1_dev = 5, 3
c2_mean, c2_dev = 8, 5
c3_mean, c3_dev = 10, 7

c1 = cafeteria('c1', c1_mean, c1_dev)
c2 = cafeteria('c1', c2_mean, c2_dev)
c3 = cafeteria('c1', c3_mean, c3_dev)

#return the total happiness for exploitOnly for t trial(s)
def exploitOnly(t):
    totalHappiness = 0
    ### t trials
    for x in range (t):
        bestCafe = c1
        valuec1 = c1.happiness()
        valuec2 = c2.happiness()
        valuec3 = c3.happiness()
        totalHappiness += (valuec1 + valuec2 + valuec3)
        if(valuec2 > valuec1):
            bestCafe = c2
        if(valuec3 > valuec1):
            bestCafe = c3
        for days in range (297):
            totalHappiness += bestCafe.happiness()
    return totalHappiness/t

def exploreOnly(t):
    #TODO implement the exploreOnly algorithm
    return 0

def eGreedy(t,e):
    #TODO implement the eGreedy algorithm
    return 0

def simulate(t,ePercent):
    e = ePercent

    # expected Values
    optimumHappiness = c3_mean * 300
    exploreHappiness = 100 * c1_mean + 100 * c2_mean + 100 * c3_mean
    exploitHappiness = c3_mean + c2_mean + c1_mean + c3_mean * 297
    egreedyHappiness = (int)(c3_mean * ((100 - e) / 100) * 300 + c3_mean * ((e / 100) * 300) / 3 + c2_mean * (
                (e / 100) * 300) / 3 + c1_mean * ((e / 100) * 300) / 3)

    exploitResult = exploitOnly(t)
    #print(exploitResult)
    exploreResult = exploreOnly(t)
    greedyResult = eGreedy(t,e)
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

simulate(1000,12)



