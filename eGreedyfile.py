def egreedy (e):
    caf1 = 9
    caf2 = 7
    caf3 = 11
    input(3)
    input(5)
    input(7)
    day1 = caf1
    day2 = caf2
    day3 = caf3
    100-e % 9
    e % 11
    var = day1 == input(3)
    var = day2 == input(5)
    var = day3 == input(7)
    if var == day1 == caf1:
        return input + caf1
    if var == day2 == caf2:
        return input + caf2
    if var == day3 == caf3:
        return input + caf3