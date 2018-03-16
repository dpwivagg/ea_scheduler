# This is for the simulation of gibbs samplin
from enum import Enum
import random
from Assignment2.node import Node
from Assignment2.new_input import input_line

import matplotlib.pyplot as plt

# --------------------------------------This set up the CPT------------------------------------------------------------
class NB(Enum):
    identity = "neighborhood"
    good = 0
    bad = 1
    list = [good, bad]

class AM(Enum):
    identity = "amenities"
    lots = 0
    little = 1
    list = [lots, little]

class SIZ(Enum):
    identity = "size"
    small = 0
    medium = 1
    large=2
    list = [small, medium, large]

class LOC(Enum):
    identity = "location"
    good = 0
    bad = 1
    ugly = 2
    list = [good, bad, ugly]

class CHI(Enum):
    identity = "children"
    good = 0
    bad = 1
    list = [good, bad]

class SCH(Enum):
    identity = "school"
    good = 0
    bad = 1
    list = [good, bad]

class AGE(Enum):
    identity = "age"
    old = 0
    new = 1
    list = [old, new]

class PRI(Enum):
    identity = "price"
    cheap = 0
    ok = 1
    expensive = 2
    list = [cheap, ok, expensive]


def createTables():
    amentities={AM.lots.value:0.3, AM.little.value:0.7}

    neighborhood={NB.bad.value:0.4, NB.good.value:0.6}

    size={SIZ.small.value:0.33,SIZ.medium.value:0.34,SIZ.large.value:0.33}

    #children neighborhood
    children={}
    children[CHI.bad.value,NB.bad.value]=0.6
    children[CHI.bad.value,NB.good.value]=0.3
    children[CHI.good.value,NB.bad.value]=0.4
    children[CHI.good.value,NB.good.value]=0.7

    #school children
    school={}
    school[SCH.bad.value,CHI.bad.value]=0.7
    school[SCH.bad.value,CHI.good.value]=0.8
    school[SCH.good.value,CHI.bad.value]=0.3
    school[SCH.good.value,CHI.good.value]=0.2

    #age location
    age={}
    age[AGE.old.value,LOC.good.value]=0.3
    age[AGE.old.value,LOC.bad.value]=0.6
    age[AGE.old.value,LOC.ugly.value]=0.9
    age[AGE.new.value,LOC.good.value]=0.7
    age[AGE.new.value,LOC.bad.value]=0.4
    age[AGE.new.value,LOC.ugly.value]=0.1

    #location amentities neighborhood
    location={}
    location[LOC.good.value,AM.lots.value,NB.bad.value]=0.3
    location[LOC.good.value,AM.lots.value,NB.good.value]=0.8
    location[LOC.good.value,AM.little.value,NB.bad.value]=0.2
    location[LOC.good.value,AM.little.value,NB.good.value]=0.5
    location[LOC.bad.value,AM.lots.value,NB.bad.value]=0.4
    location[LOC.bad.value,AM.lots.value,NB.good.value]=0.15
    location[LOC.bad.value,AM.little.value,NB.bad.value]=0.4
    location[LOC.bad.value,AM.little.value,NB.good.value]=0.35
    location[LOC.ugly.value,AM.lots.value,NB.bad.value]=0.3
    location[LOC.ugly.value,AM.lots.value,NB.good.value]=0.05
    location[LOC.ugly.value,AM.little.value,NB.bad.value]=0.4
    location[LOC.ugly.value,AM.little.value,NB.good.value]=0.15

    #price location age school size
    price={}
    price[PRI.cheap.value,LOC.good.value,AGE.old.value,SCH.bad.value,SIZ.small.value]=0.5
    price[PRI.cheap.value,LOC.good.value,AGE.old.value,SCH.bad.value,SIZ.medium.value]=0.4
    price[PRI.cheap.value,LOC.good.value,AGE.old.value,SCH.bad.value,SIZ.large.value]=0.35
    price[PRI.cheap.value,LOC.good.value,AGE.old.value,SCH.good.value,SIZ.small.value]=0.4
    price[PRI.cheap.value,LOC.good.value,AGE.old.value,SCH.good.value,SIZ.medium.value]=0.35
    price[PRI.cheap.value,LOC.good.value,AGE.old.value,SCH.good.value,SIZ.large.value]=0.3
    price[PRI.cheap.value,LOC.good.value,AGE.new.value,SCH.bad.value,SIZ.small.value]=0.45
    price[PRI.cheap.value,LOC.good.value,AGE.new.value,SCH.bad.value,SIZ.medium.value]=0.4
    price[PRI.cheap.value,LOC.good.value,AGE.new.value,SCH.bad.value,SIZ.large.value]=0.35
    price[PRI.cheap.value,LOC.good.value,AGE.new.value,SCH.good.value,SIZ.small.value]=0.25
    price[PRI.cheap.value,LOC.good.value,AGE.new.value,SCH.good.value,SIZ.medium.value]=0.2
    price[PRI.cheap.value,LOC.good.value,AGE.new.value,SCH.good.value,SIZ.large.value]=0.1
    price[PRI.cheap.value,LOC.bad.value,AGE.old.value,SCH.bad.value,SIZ.small.value]=0.7
    price[PRI.cheap.value,LOC.bad.value,AGE.old.value,SCH.bad.value,SIZ.medium.value]=0.65
    price[PRI.cheap.value,LOC.bad.value,AGE.old.value,SCH.bad.value,SIZ.large.value]=0.65
    price[PRI.cheap.value,LOC.bad.value,AGE.old.value,SCH.good.value,SIZ.small.value]=0.55
    price[PRI.cheap.value,LOC.bad.value,AGE.old.value,SCH.good.value,SIZ.medium.value]=0.5
    price[PRI.cheap.value,LOC.bad.value,AGE.old.value,SCH.good.value,SIZ.large.value]=0.45
    price[PRI.cheap.value,LOC.bad.value,AGE.new.value,SCH.bad.value,SIZ.small.value]=0.6
    price[PRI.cheap.value,LOC.bad.value,AGE.new.value,SCH.bad.value,SIZ.medium.value]=0.55
    price[PRI.cheap.value,LOC.bad.value,AGE.new.value,SCH.bad.value,SIZ.large.value]=0.5
    price[PRI.cheap.value,LOC.bad.value,AGE.new.value,SCH.good.value,SIZ.small.value]=0.4
    price[PRI.cheap.value,LOC.bad.value,AGE.new.value,SCH.good.value,SIZ.medium.value]=0.3
    price[PRI.cheap.value,LOC.bad.value,AGE.new.value,SCH.good.value,SIZ.large.value]=0.3
    price[PRI.cheap.value,LOC.ugly.value,AGE.old.value,SCH.bad.value,SIZ.small.value]=0.8
    price[PRI.cheap.value,LOC.ugly.value,AGE.old.value,SCH.bad.value,SIZ.medium.value]=0.75
    price[PRI.cheap.value,LOC.ugly.value,AGE.old.value,SCH.bad.value,SIZ.large.value]=0.75
    price[PRI.cheap.value,LOC.ugly.value,AGE.old.value,SCH.good.value,SIZ.small.value]=0.65
    price[PRI.cheap.value,LOC.ugly.value,AGE.old.value,SCH.good.value,SIZ.medium.value]=0.6
    price[PRI.cheap.value,LOC.ugly.value,AGE.old.value,SCH.good.value,SIZ.large.value]=0.55
    price[PRI.cheap.value,LOC.ugly.value,AGE.new.value,SCH.bad.value,SIZ.small.value]=0.7
    price[PRI.cheap.value,LOC.ugly.value,AGE.new.value,SCH.bad.value,SIZ.medium.value]=0.64
    price[PRI.cheap.value,LOC.ugly.value,AGE.new.value,SCH.bad.value,SIZ.large.value]=0.61
    price[PRI.cheap.value,LOC.ugly.value,AGE.new.value,SCH.good.value,SIZ.small.value]=0.48
    price[PRI.cheap.value,LOC.ugly.value,AGE.new.value,SCH.good.value,SIZ.medium.value]=0.41
    price[PRI.cheap.value,LOC.ugly.value,AGE.new.value,SCH.good.value,SIZ.large.value]=0.37

    price[PRI.ok.value,LOC.good.value,AGE.old.value,SCH.bad.value,SIZ.small.value]=0.4
    price[PRI.ok.value,LOC.good.value,AGE.old.value,SCH.bad.value,SIZ.medium.value]=0.45
    price[PRI.ok.value,LOC.good.value,AGE.old.value,SCH.bad.value,SIZ.large.value]=0.45
    price[PRI.ok.value,LOC.good.value,AGE.old.value,SCH.good.value,SIZ.small.value]=0.3
    price[PRI.ok.value,LOC.good.value,AGE.old.value,SCH.good.value,SIZ.medium.value]=0.3
    price[PRI.ok.value,LOC.good.value,AGE.old.value,SCH.good.value,SIZ.large.value]=0.25
    price[PRI.ok.value,LOC.good.value,AGE.new.value,SCH.bad.value,SIZ.small.value]=0.4
    price[PRI.ok.value,LOC.good.value,AGE.new.value,SCH.bad.value,SIZ.medium.value]=0.45
    price[PRI.ok.value,LOC.good.value,AGE.new.value,SCH.bad.value,SIZ.large.value]=0.45
    price[PRI.ok.value,LOC.good.value,AGE.new.value,SCH.good.value,SIZ.small.value]=0.3
    price[PRI.ok.value,LOC.good.value,AGE.new.value,SCH.good.value,SIZ.medium.value]=0.25
    price[PRI.ok.value,LOC.good.value,AGE.new.value,SCH.good.value,SIZ.large.value]=0.2
    price[PRI.ok.value,LOC.bad.value,AGE.old.value,SCH.bad.value,SIZ.small.value]=0.299
    price[PRI.ok.value,LOC.bad.value,AGE.old.value,SCH.bad.value,SIZ.medium.value]=0.33
    price[PRI.ok.value,LOC.bad.value,AGE.old.value,SCH.bad.value,SIZ.large.value]=0.32
    price[PRI.ok.value,LOC.bad.value,AGE.old.value,SCH.good.value,SIZ.small.value]=0.35
    price[PRI.ok.value,LOC.bad.value,AGE.old.value,SCH.good.value,SIZ.medium.value]=0.35
    price[PRI.ok.value,LOC.bad.value,AGE.old.value,SCH.good.value,SIZ.large.value]=0.4
    price[PRI.ok.value,LOC.bad.value,AGE.new.value,SCH.bad.value,SIZ.small.value]=0.35
    price[PRI.ok.value,LOC.bad.value,AGE.new.value,SCH.bad.value,SIZ.medium.value]=0.35
    price[PRI.ok.value,LOC.bad.value,AGE.new.value,SCH.bad.value,SIZ.large.value]=0.4
    price[PRI.ok.value,LOC.bad.value,AGE.new.value,SCH.good.value,SIZ.small.value]=0.4
    price[PRI.ok.value,LOC.bad.value,AGE.new.value,SCH.good.value,SIZ.medium.value]=0.4
    price[PRI.ok.value,LOC.bad.value,AGE.new.value,SCH.good.value,SIZ.large.value]=0.3
    price[PRI.ok.value,LOC.ugly.value,AGE.old.value,SCH.bad.value,SIZ.small.value]=0.1999
    price[PRI.ok.value,LOC.ugly.value,AGE.old.value,SCH.bad.value,SIZ.medium.value]=0.24
    price[PRI.ok.value,LOC.ugly.value,AGE.old.value,SCH.bad.value,SIZ.large.value]=0.23
    price[PRI.ok.value,LOC.ugly.value,AGE.old.value,SCH.good.value,SIZ.small.value]=0.3
    price[PRI.ok.value,LOC.ugly.value,AGE.old.value,SCH.good.value,SIZ.medium.value]=0.33
    price[PRI.ok.value,LOC.ugly.value,AGE.old.value,SCH.good.value,SIZ.large.value]=0.37
    price[PRI.ok.value,LOC.ugly.value,AGE.new.value,SCH.bad.value,SIZ.small.value]=0.27
    price[PRI.ok.value,LOC.ugly.value,AGE.new.value,SCH.bad.value,SIZ.medium.value]=0.3
    price[PRI.ok.value,LOC.ugly.value,AGE.new.value,SCH.bad.value,SIZ.large.value]=0.32
    price[PRI.ok.value,LOC.ugly.value,AGE.new.value,SCH.good.value,SIZ.small.value]=0.42
    price[PRI.ok.value,LOC.ugly.value,AGE.new.value,SCH.good.value,SIZ.medium.value]=0.39
    price[PRI.ok.value,LOC.ugly.value,AGE.new.value,SCH.good.value,SIZ.large.value]=0.33

    price[PRI.expensive.value, LOC.good.value, AGE.old.value, SCH.bad.value, SIZ.small.value]=0.1
    price[PRI.expensive.value, LOC.good.value, AGE.old.value, SCH.bad.value, SIZ.medium.value]=0.15
    price[PRI.expensive.value, LOC.good.value, AGE.old.value, SCH.bad.value, SIZ.large.value]=0.2
    price[PRI.expensive.value, LOC.good.value, AGE.old.value, SCH.good.value, SIZ.small.value]=0.3
    price[PRI.expensive.value, LOC.good.value, AGE.old.value, SCH.good.value, SIZ.medium.value]=0.35
    price[PRI.expensive.value, LOC.good.value, AGE.old.value, SCH.good.value, SIZ.large.value]=0.45
    price[PRI.expensive.value, LOC.good.value, AGE.new.value, SCH.bad.value, SIZ.small.value]=0.15
    price[PRI.expensive.value, LOC.good.value, AGE.new.value, SCH.bad.value, SIZ.medium.value]=0.15
    price[PRI.expensive.value, LOC.good.value, AGE.new.value, SCH.bad.value, SIZ.large.value]=0.2
    price[PRI.expensive.value, LOC.good.value, AGE.new.value, SCH.good.value, SIZ.small.value]=0.45
    price[PRI.expensive.value, LOC.good.value, AGE.new.value, SCH.good.value, SIZ.medium.value]=0.55
    price[PRI.expensive.value, LOC.good.value, AGE.new.value, SCH.good.value, SIZ.large.value]=0.7
    price[PRI.expensive.value, LOC.bad.value, AGE.old.value, SCH.bad.value, SIZ.small.value]=0.001
    price[PRI.expensive.value, LOC.bad.value, AGE.old.value, SCH.bad.value, SIZ.medium.value]=0.02
    price[PRI.expensive.value, LOC.bad.value, AGE.old.value, SCH.bad.value, SIZ.large.value]=0.03
    price[PRI.expensive.value, LOC.bad.value, AGE.old.value, SCH.good.value, SIZ.small.value]=0.1
    price[PRI.expensive.value, LOC.bad.value, AGE.old.value, SCH.good.value, SIZ.medium.value]=0.15
    price[PRI.expensive.value, LOC.bad.value, AGE.old.value, SCH.good.value, SIZ.large.value]=0.15
    price[PRI.expensive.value, LOC.bad.value, AGE.new.value, SCH.bad.value, SIZ.small.value]=0.05
    price[PRI.expensive.value, LOC.bad.value, AGE.new.value, SCH.bad.value, SIZ.medium.value]=0.1
    price[PRI.expensive.value, LOC.bad.value, AGE.new.value, SCH.bad.value, SIZ.large.value]=0.1
    price[PRI.expensive.value, LOC.bad.value, AGE.new.value, SCH.good.value, SIZ.small.value]=0.2
    price[PRI.expensive.value, LOC.bad.value, AGE.new.value, SCH.good.value, SIZ.medium.value]=0.3
    price[PRI.expensive.value, LOC.bad.value, AGE.new.value, SCH.good.value, SIZ.large.value]=0.4
    price[PRI.expensive.value, LOC.ugly.value, AGE.old.value, SCH.bad.value, SIZ.small.value]=0.0001
    price[PRI.expensive.value, LOC.ugly.value, AGE.old.value, SCH.bad.value, SIZ.medium.value]=0.01
    price[PRI.expensive.value, LOC.ugly.value, AGE.old.value, SCH.bad.value, SIZ.large.value]=0.02
    price[PRI.expensive.value, LOC.ugly.value, AGE.old.value, SCH.good.value, SIZ.small.value]=0.05
    price[PRI.expensive.value, LOC.ugly.value, AGE.old.value, SCH.good.value, SIZ.medium.value]=0.07
    price[PRI.expensive.value, LOC.ugly.value, AGE.old.value, SCH.good.value, SIZ.large.value]=0.08
    price[PRI.expensive.value, LOC.ugly.value, AGE.new.value, SCH.bad.value, SIZ.small.value]=0.03
    price[PRI.expensive.value, LOC.ugly.value, AGE.new.value, SCH.bad.value, SIZ.medium.value]=0.06
    price[PRI.expensive.value, LOC.ugly.value, AGE.new.value, SCH.bad.value, SIZ.large.value]=0.07
    price[PRI.expensive.value, LOC.ugly.value, AGE.new.value, SCH.good.value, SIZ.small.value]=0.1
    price[PRI.expensive.value, LOC.ugly.value, AGE.new.value, SCH.good.value, SIZ.medium.value]=0.2
    price[PRI.expensive.value, LOC.ugly.value, AGE.new.value, SCH.good.value, SIZ.large.value]=0.3

    nodeNB = Node(NB.identity.value, NB.list.value, neighborhood)
    nodeAM = Node(AM.identity.value, AM.list.value, amentities)
    nodeSIZ = Node(SIZ.identity.value, SIZ.list.value, size)
    nodeLOC = Node(LOC.identity.value, LOC.list.value, location)
    nodeCHI = Node(CHI.identity.value, CHI.list.value, children)
    nodeSCH = Node(SCH.identity.value, SCH.list.value, school)
    nodeAGE = Node(AGE.identity.value, AGE.list.value, age)
    nodePRI = Node(PRI.identity.value, PRI.list.value, price)

    # --------------------------------------This set up the CPT------------------------------------------------------------

    # -----------------------------This set up the relationship------------------------------------------------------------
    # For Amenities child and parent
    nodeAM.addChild(nodeLOC)

    # For location child and parent
    nodeLOC.addParent(nodeAM)
    nodeLOC.addParent(nodeNB)
    nodeLOC.addChild(nodeAGE)
    nodeLOC.addChild(nodePRI)

    # For neighborhood child and parent
    nodeNB.addChild(nodeLOC)
    nodeNB.addChild(nodeCHI)

    # For children child and parent
    nodeCHI.addParent(nodeNB)
    nodeCHI.addChild(nodeSCH)

    # For schools child and parent
    nodeSCH.addParent(nodeCHI)
    nodeSCH.addChild(nodePRI)

    # For size child and parent
    nodeSIZ.addChild(nodePRI)

    # For age child and parent
    nodeAGE.addParent(nodeLOC)
    nodeAGE.addChild(nodePRI)

    # For price child and parent

    nodePRI.addParent(nodeLOC)
    nodePRI.addParent(nodeAGE)
    nodePRI.addParent(nodeSCH)
    nodePRI.addParent(nodeSIZ)
    # print(children[0,0])
    (queryNode,evidenceNodeList, iterations,drops) = input_line()
    print("Q:"+queryNode+" I:"+str(iterations)+" D:"+str(drops))
    nodeList = [nodeAM, nodeAGE, nodeSIZ, nodePRI, nodeSCH, nodeCHI, nodeLOC, nodeNB]
    actualList = list()
    ##

    for node in nodeList:
        print(node)
        if node.identity == queryNode:
            result = [0]*len(node.stateList)

            graphList = []
            for i in range(len(node.stateList)):
                graphList.append([])
            prob = [0]*len(node.stateList)
            print("result length:"+str(len(node.stateList)))
            actualList.append(node)
            qnode = node
            continue
        for key in evidenceNodeList.keys():
            if node.identity == key:
                node.isEvidence = True
                node.state = evidenceNodeList.get(key)
                continue
        if not node.isEvidence:
            actualList.append(node)

    pnode = None
    for i in range(drops):
        randIndex = random.randint(0,len(actualList)-1)
        cnode = actualList[randIndex]
        while cnode == pnode:
            randIndex = random.randint(0, len(actualList)-1)
            cnode = actualList[randIndex]
        cnode.getMBProbability()
        pnode = cnode
    ylist = list()
    for i in range(iterations-drops):
        randIndex = random.randint(0,len(actualList)-1)
        cnode = actualList[randIndex]
        while cnode == pnode:
            randIndex = random.randint(0, len(actualList)-1)
            cnode = actualList[randIndex]
        cnode.getMBProbability()
        result[qnode.state] = result[qnode.state] + 1
        sum = 0
        for a in result:
            sum = sum +a
        for a in range(len(result)):
            prob[a] = result[a] / sum
        for a in range(len(prob)):
            graphList[a].append(prob[a])
        ylist.append(i)
        pnode = cnode
    for i in range(len(graphList)):
        plt.plot(graphList[i], ylist, label="line "+str(i))
    for a in range(len(prob)):
        for b in graphList[a]:
            print (b)
        print("break")

    print("end here")
    # naming the x axis
    plt.xlabel('x - axis')
    # naming the y axis
    plt.ylabel('y - axis')
    # giving a title to my graph
    plt.title('Two lines on same graph!')
    # show a legend on the plot
    # plt.legend()
    # function to show the plot
    plt.show()
    print(result)




    # for i in range(drops):
    #     node = nodeList.random.ran






createTables()
# nodeLOC.getMBProbability()
# print(nodeLOC)
# nodeCHI.getMBProbability()




