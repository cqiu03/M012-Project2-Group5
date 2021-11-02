import random

H1 = 9
D1 = 3
H2 = 7
D2 = 5
H3 = 11
D3 = 7

def exploreOnly():
    HAPPY = 0
    for i in range(100):
        HAPPY = HAPPY + random.normalvariate(H1, D1)
        HAPPY = HAPPY + random.normalvariate(H2, D2)
        HAPPY = HAPPY + random.normalvariate(H3, D3)
    print("Explore Only: ", HAPPY)
    return (HAPPY)

exploreOnly()

