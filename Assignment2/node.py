# This is the Node for Gibbs sampling
import random
class Node:
    def __init__(self, identity, stateList, cpt):
        self.identity = identity
        self.cpt = cpt
        self.state = 0
        self.stateList = stateList
        self.parents = []  # The parent node list
        self.children = [] # The children node list
        self.isEvidence = False

    def addParent(self,parent):
        self.parents.append(parent)

    def addChild(self,child):
        self.children.append(child)

    def getNormalProbabilty(self):
        p = 1
        if len(self.parents) == 1:
            a = self.parents[0].state
            p = self.cpt[self.state,a]
        if len(self.parents) == 2:
            a = self.parents[0].state
            b = self.parents[1].state
            p = self.cpt[self.state, a, b]
        if len(self.parents) == 3:
            a = self.parents[0].state
            b = self.parents[1].state
            c = self.parents[2].state
            p = self.cpt[ self.state,a, b, c]
        if len(self.parents) == 4:
            a = self.parents[0].state
            b = self.parents[1].state
            c = self.parents[2].state
            d = self.parents[3].state
            p = self.cpt[self.state, a, b, c, d]
        return p

    def getMBProbability(self): ##This is for the gibbs sampling which will go through its markov blanket and find the probability
        weight = []
        pSum = 0
        for i in range(len(self.stateList)):
            s = i
            self.state = s ##This will run through all states to find their probability
            p = self.getNormalProbabilty()
            print(p)
            for child in self.children:
                print(str(p)+"*"+str(child.getNormalProbabilty()))
                p = p * child.getNormalProbabilty()

            print("\n")
            weight.append(p) ## this will sets the probability for all states
            pSum = pSum + p
        ratio = 1 / pSum
        for i in range(len(weight)):## run through the
            weight[i] = weight[i] * ratio
            print(self.identity + " State:" + str(self.stateList[i]) + " Probability:" + str(weight[i]))
        self.state = random.choices(self.stateList, weights=weight, k=1)












