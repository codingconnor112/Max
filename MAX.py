import copy
import pickle
import random
import sys
print("MAX testing intelegence")
print("a simple AI simulation")
print("made with python version "+sys.version)
file = open(r"test.info", mode = "rb")
testdict = pickle.load(file)
file.close()
class Agent(object):
    def __init__(self, lineval):
        self.lineval = lineval
        self.score = 0
    def test(self, testsheet):
        answer = []
        for x in testsheet:
            if x >= self.lineval:
                answer.append(True)
            else:
                answer.append(False)
        return answer
    def reproduce(self, other):
        us=other
        usnums = []
        for x in us:
            usnums.append(x.score)
        if usnums.index(max(usnums)) == us.index(self):
            a=copy.copy(self)
            b=copy.copy(self)
            a.lineval += random.randint(0, 5)
            b.lineval += random.randint(-5, 0)
            return list((a, b, self))
        else:
            try:
                return None
            finally:
                del self
    
iternum = int(input("iteration count"))
testque = list(testdict.keys())
testans = list(testdict.values())
newagents=[Agent(random.randint(0, 100)), Agent(random.randint(0, 100)), Agent(random.randint(0, 100))]
for x in range(0, iternum):
    agents=newagents
    for i in agents:
        right = 0
        testresults = i.test(testque)
        for j in testresults:
            if j == testans[testresults.index(j)]:
                right += 1
        i.score = right
        r = i.reproduce(agents)
        if r != None:
            print("iteration "+str(x+1)+" sucessful")
            newagents = r
print("done")
while True:
    hinputnum = int(input("number"))
    if random.choice(agents).lineval >= hinputnum:
        print("small number")
    else:
        print("big number")
