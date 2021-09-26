import copy
import random
from random import sample

# Consider using the modules imported above.
def dictToList(dict):
    result = []
    for key in dict:
        for bColor in range(dict[key]):
            result.append(key)
    return result

def listToDict(list):
    result = {}
    for x in list:
        if x in result:
            result[x] += 1
        else:
            result[x] = 1
    return result


class Hat:
    def __init__(self, **hatballs):
        self.contents = dictToList(hatballs)

    def draw(self, picks):
        drawList = []
        if picks > len(self.contents):
            return self.contents

        drawList = sample(self.contents,picks)

        for x in drawList:
            self.contents.remove(x)

        return drawList



def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    match = 0
    no_match = 0


    for x in range(num_experiments):
        toExperiment = {}
        endCheck = []

        expHat = copy.deepcopy(hat)
        toExperiment = listToDict(expHat.draw(num_balls_drawn))

        for key, value in toExperiment.items():
            try:
                if expected_balls[key] - value <= 0:
                    endCheck.append(True)
            except:
                pass

        if sum(endCheck) == len(expected_balls):
            match += 1
        else:
            no_match += 1

    return match/num_experiments
