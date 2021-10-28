import random
c1_Happiness = random.normalvariate(9,3)
c2_Happiness = random.normalvariate(7,5)
c3_Happiness = random.normalvariate(11,7)

c1_mean,c1_dev = 5,3
c2_mean,c2_dev = 8,5
c3_mean,c3_dev = 10,7

c1_averageHappiness = 0 #placeholder
c2_averageHappiness = 0 #placeholder
c3_averageHappiness = 0 #placeholder

e = 12

optimumHappiness = c3_mean * 300
exploreHappiness = 100 * c1_mean + 100 * c2_mean + 100 * c3_mean
exploitHappiness = c3_mean + c2_mean + c1_mean + c3_mean * 297
egreedyHappiness = (int)(c3_mean * ((100 - e) / 100) * 300 + c3_mean * ((e / 100) * 300) / 3 + c2_mean * ((e / 100) * 300) / 3 + c1_mean * ((e / 100) * 300) / 3)


def exploitOnly(t):
    #TODO implement the exploitOnly algorithm
    pass

def exploreOnly(t):
    #TODO implement the exploreOnly algorithm
    pass

def eGreedy(t):
    #TODO implement the eGreedy algorithm
    pass

def simulate(t):
    exploitOnly(t)
    exploreOnly(t)
    eGreedy(t)
    print("Optimum Happiness: " + (str)(optimumHappiness))
    print("\n----------------------------------------\nExplore Only Stats\n----------------------------------------")
    print("Expected Total Happiness: " + (str)(exploreHappiness))
    print("Expected Total Regret: " + (str)(optimumHappiness - exploreHappiness))
    print("Average Total Happiness: ")
    print("Average Total Regret: ")
    print("\n----------------------------------------\nExploit Only Stats\n----------------------------------------")
    print("Expected Total Happiness: " + (str)(exploitHappiness))
    print("Expected Total Regret: " + (str)(optimumHappiness - exploitHappiness))
    print("Average Total Happiness: ")
    print("Average Total Regret: ")
    print("\n----------------------------------------\neGreedy Stats\n----------------------------------------")
    print("Expected Total Happiness: " + (str)(egreedyHappiness))
    print("Expected Total Regret: " + (str)(optimumHappiness - egreedyHappiness))
    print("Average Total Happiness: ")
    print("Average Total Regret: ")

simulate(1)