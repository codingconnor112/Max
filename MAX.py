import copy
import pickle
import random
import sys
print(" Max testing intellegence")
print("a simple AI simulation")
print("made with python version "+sys.version)
file = open(r"test.info", mode = "rb")
try:
    testdict = pickle.load(file)
except EOFError:
    pass
file.close()
global agentnum
agentnum = int(input("agents for MAX"))
class Agent(object):
    def __init__(self, lineval):
        self.lineval = lineval
        self.score = 0
    def test(self, testsheet):
        answer = []
        for x in testsheet:
            if round(x) >= self.lineval:
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
            agentsnew = []
            for x in range(0, agents-1):
                agentsnew.append(copy.copy(self))
                agentsnew[len(agentsnew)].lineval += random.randint(-1, 1)
            agentsnew.append(self)
            return agentsnew
        else:
            try:
                return None
            finally:
                del self
    
iternum = int(input("iteration count"))
testque = list(testdict.keys())
testans = list(testdict.values())
agents=[Agent(random.randint(0, 100)), Agent(random.randint(0, 100)), Agent(random.randint(0, 100))]
for x in range(0, iternum):
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
            agents = r
print("done")
while True:
    hinputnum = int(input("number"))
    if random.choice(agents).lineval >= hinputnum:
        print("small number")
    else:
        print("big number")
