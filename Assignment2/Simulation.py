# This is for the simulation of gibbs samplin
from enum import Enum
from Assignment2.node import Node


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

amentities={AM.lots:0.3, AM.little:0.7}

neighborhood={NB.bad:0.4, NB.good:0.6}

size={SIZ.small:0.33,SIZ.medium:0.34,SIZ.large:0.33}

#children neighborhood
children={}
children[CHI.bad,NB.bad]=0.6
children[CHI.bad,NB.good]=0.3
children[CHI.good,NB.bad]=0.4
children[CHI.good,NB.bad]=0.7

#school children
school={}
school[SCH.bad,CHI.bad]=0.7
school[SCH.bad,CHI.good]=0.8
school[SCH.good,CHI.bad]=0.3
school[SCH.good,CHI.good]=0.2

#age location
age={}
age[AGE.old,LOC.good]=0.3
age[AGE.old,LOC.bad]=0.6
age[AGE.old,LOC.ugly]=0.9
age[AGE.new,LOC.good]=0.7
age[AGE.new,LOC.bad]=0.4
age[AGE.new,LOC.ugly]=0.1

#location amentities neighborhood
location={}
location[LOC.good,AM.lots,NB.bad]=0.3
location[LOC.good,AM.lots,NB.good]=0.8
location[LOC.good,AM.little,NB.bad]=0.2
location[LOC.good,AM.little,NB.good]=0.5
location[LOC.bad,AM.lots,NB.bad]=0.4
location[LOC.bad,AM.lots,NB.good]=0.15
location[LOC.bad,AM.little,NB.bad]=0.4
location[LOC.bad,AM.little,NB.good]=0.35
location[LOC.ugly,AM.lots,NB.bad]=0.35
location[LOC.ugly,AM.lots,NB.good]=0.35
location[LOC.ugly,AM.little,NB.bad]=0.35
location[LOC.ugly,AM.little,NB.good]=0.35

#price location age school size
price={}
price[PRI.cheap,LOC.good,AGE.new,SCH.bad,SIZ.small]=0.5
price[PRI.cheap,LOC.good,AGE.new,SCH.bad,SIZ.medium]=0.4
price[PRI.cheap,LOC.good,AGE.new,SCH.bad,SIZ.large]=0.35
price[PRI.cheap,LOC.good,AGE.new,SCH.good,SIZ.small]=0.4
price[PRI.cheap,LOC.good,AGE.new,SCH.good,SIZ.medium]=0.35
price[PRI.cheap,LOC.good,AGE.new,SCH.good,SIZ.large]=0.3
price[PRI.cheap,LOC.good,AGE.old,SCH.bad,SIZ.small]=0.45
price[PRI.cheap,LOC.good,AGE.old,SCH.bad,SIZ.medium]=0.4
price[PRI.cheap,LOC.good,AGE.old,SCH.bad,SIZ.large]=0.35
price[PRI.cheap,LOC.good,AGE.old,SCH.good,SIZ.small]=0.25
price[PRI.cheap,LOC.good,AGE.old,SCH.good,SIZ.medium]=0.2
price[PRI.cheap,LOC.good,AGE.old,SCH.good,SIZ.large]=0.1
price[PRI.cheap,LOC.bad,AGE.new,SCH.bad,SIZ.small]=0.7
price[PRI.cheap,LOC.bad,AGE.new,SCH.bad,SIZ.medium]=0.65
price[PRI.cheap,LOC.bad,AGE.new,SCH.bad,SIZ.large]=0.65
price[PRI.cheap,LOC.bad,AGE.new,SCH.good,SIZ.small]=0.55
price[PRI.cheap,LOC.bad,AGE.new,SCH.good,SIZ.medium]=0.5
price[PRI.cheap,LOC.bad,AGE.new,SCH.good,SIZ.large]=0.45
price[PRI.cheap,LOC.bad,AGE.old,SCH.bad,SIZ.small]=0.6
price[PRI.cheap,LOC.bad,AGE.old,SCH.bad,SIZ.medium]=0.55
price[PRI.cheap,LOC.bad,AGE.old,SCH.bad,SIZ.large]=0.5
price[PRI.cheap,LOC.bad,AGE.old,SCH.good,SIZ.small]=0.4
price[PRI.cheap,LOC.bad,AGE.old,SCH.good,SIZ.medium]=0.3
price[PRI.cheap,LOC.bad,AGE.old,SCH.good,SIZ.large]=0.3
price[PRI.cheap,LOC.ugly,AGE.new,SCH.bad,SIZ.small]=0.8
price[PRI.cheap,LOC.ugly,AGE.new,SCH.bad,SIZ.medium]=0.75
price[PRI.cheap,LOC.ugly,AGE.new,SCH.bad,SIZ.large]=0.75
price[PRI.cheap,LOC.ugly,AGE.new,SCH.good,SIZ.small]=0.65
price[PRI.cheap,LOC.ugly,AGE.new,SCH.good,SIZ.medium]=0.6
price[PRI.cheap,LOC.ugly,AGE.new,SCH.good,SIZ.large]=0.55
price[PRI.cheap,LOC.ugly,AGE.old,SCH.bad,SIZ.small]=0.7
price[PRI.cheap,LOC.ugly,AGE.old,SCH.bad,SIZ.medium]=0.64
price[PRI.cheap,LOC.ugly,AGE.old,SCH.bad,SIZ.large]=0.61
price[PRI.cheap,LOC.ugly,AGE.old,SCH.good,SIZ.small]=0.48
price[PRI.cheap,LOC.ugly,AGE.old,SCH.good,SIZ.medium]=0.41
price[PRI.cheap,LOC.ugly,AGE.old,SCH.good,SIZ.large]=0.37

price[PRI.ok,LOC.good,AGE.new,SCH.bad,SIZ.small]=0.4
price[PRI.ok,LOC.good,AGE.new,SCH.bad,SIZ.medium]=0.45
price[PRI.ok,LOC.good,AGE.new,SCH.bad,SIZ.large]=0.45
price[PRI.ok,LOC.good,AGE.new,SCH.good,SIZ.small]=0.3
price[PRI.ok,LOC.good,AGE.new,SCH.good,SIZ.medium]=0.3
price[PRI.ok,LOC.good,AGE.new,SCH.good,SIZ.large]=0.25
price[PRI.ok,LOC.good,AGE.old,SCH.bad,SIZ.small]=0.4
price[PRI.ok,LOC.good,AGE.old,SCH.bad,SIZ.medium]=0.45
price[PRI.ok,LOC.good,AGE.old,SCH.bad,SIZ.large]=0.45
price[PRI.ok,LOC.good,AGE.old,SCH.good,SIZ.small]=0.3
price[PRI.ok,LOC.good,AGE.old,SCH.good,SIZ.medium]=0.25
price[PRI.ok,LOC.good,AGE.old,SCH.good,SIZ.large]=0.2
price[PRI.ok,LOC.bad,AGE.new,SCH.bad,SIZ.small]=0.299
price[PRI.ok,LOC.bad,AGE.new,SCH.bad,SIZ.medium]=0.33
price[PRI.ok,LOC.bad,AGE.new,SCH.bad,SIZ.large]=0.32
price[PRI.ok,LOC.bad,AGE.new,SCH.good,SIZ.small]=0.35
price[PRI.ok,LOC.bad,AGE.new,SCH.good,SIZ.medium]=0.35
price[PRI.ok,LOC.bad,AGE.new,SCH.good,SIZ.large]=0.4
price[PRI.ok,LOC.bad,AGE.old,SCH.bad,SIZ.small]=0.35
price[PRI.ok,LOC.bad,AGE.old,SCH.bad,SIZ.medium]=0.35
price[PRI.ok,LOC.bad,AGE.old,SCH.bad,SIZ.large]=0.4
price[PRI.ok,LOC.bad,AGE.old,SCH.good,SIZ.small]=0.4
price[PRI.ok,LOC.bad,AGE.old,SCH.good,SIZ.medium]=0.4
price[PRI.ok,LOC.bad,AGE.old,SCH.good,SIZ.large]=0.3
price[PRI.ok,LOC.ugly,AGE.new,SCH.bad,SIZ.small]=0.1999
price[PRI.ok,LOC.ugly,AGE.new,SCH.bad,SIZ.medium]=0.24
price[PRI.ok,LOC.ugly,AGE.new,SCH.bad,SIZ.large]=0.23
price[PRI.ok,LOC.ugly,AGE.new,SCH.good,SIZ.small]=0.3
price[PRI.ok,LOC.ugly,AGE.new,SCH.good,SIZ.medium]=0.33
price[PRI.ok,LOC.ugly,AGE.new,SCH.good,SIZ.large]=0.37
price[PRI.ok,LOC.ugly,AGE.old,SCH.bad,SIZ.small]=0.27
price[PRI.ok,LOC.ugly,AGE.old,SCH.bad,SIZ.medium]=0.3
price[PRI.ok,LOC.ugly,AGE.old,SCH.bad,SIZ.large]=0.32
price[PRI.ok,LOC.ugly,AGE.old,SCH.good,SIZ.small]=0.42
price[PRI.ok,LOC.ugly,AGE.old,SCH.good,SIZ.medium]=0.39
price[PRI.ok,LOC.ugly,AGE.old,SCH.good,SIZ.large]=0.33

price[PRI.expensive,LOC.good,AGE.new,SCH.bad,SIZ.small]=0.1
price[PRI.expensive,LOC.good,AGE.new,SCH.bad,SIZ.medium]=0.15
price[PRI.expensive,LOC.good,AGE.new,SCH.bad,SIZ.large]=0.2
price[PRI.expensive,LOC.good,AGE.new,SCH.good,SIZ.small]=0.3
price[PRI.expensive,LOC.good,AGE.new,SCH.good,SIZ.medium]=0.35
price[PRI.expensive,LOC.good,AGE.new,SCH.good,SIZ.large]=0.45
price[PRI.expensive,LOC.good,AGE.old,SCH.bad,SIZ.small]=0.15
price[PRI.expensive,LOC.good,AGE.old,SCH.bad,SIZ.medium]=0.15
price[PRI.expensive,LOC.good,AGE.old,SCH.bad,SIZ.large]=0.2
price[PRI.expensive,LOC.good,AGE.old,SCH.good,SIZ.small]=0.45
price[PRI.expensive,LOC.good,AGE.old,SCH.good,SIZ.medium]=0.55
price[PRI.expensive,LOC.good,AGE.old,SCH.good,SIZ.large]=0.7
price[PRI.expensive,LOC.bad,AGE.new,SCH.bad,SIZ.small]=0.001
price[PRI.expensive,LOC.bad,AGE.new,SCH.bad,SIZ.medium]=0.02
price[PRI.expensive,LOC.bad,AGE.new,SCH.bad,SIZ.large]=0.03
price[PRI.expensive,LOC.bad,AGE.new,SCH.good,SIZ.small]=0.1
price[PRI.expensive,LOC.bad,AGE.new,SCH.good,SIZ.medium]=0.15
price[PRI.expensive,LOC.bad,AGE.new,SCH.good,SIZ.large]=0.15
price[PRI.expensive,LOC.bad,AGE.old,SCH.bad,SIZ.small]=0.05
price[PRI.expensive,LOC.bad,AGE.old,SCH.bad,SIZ.medium]=0.1
price[PRI.expensive,LOC.bad,AGE.old,SCH.bad,SIZ.large]=0.1
price[PRI.expensive,LOC.bad,AGE.old,SCH.good,SIZ.small]=0.2
price[PRI.expensive,LOC.bad,AGE.old,SCH.good,SIZ.medium]=0.3
price[PRI.expensive,LOC.bad,AGE.old,SCH.good,SIZ.large]=0.4
price[PRI.expensive,LOC.ugly,AGE.new,SCH.bad,SIZ.small]=0.0001
price[PRI.expensive,LOC.ugly,AGE.new,SCH.bad,SIZ.medium]=0.01
price[PRI.expensive,LOC.ugly,AGE.new,SCH.bad,SIZ.large]=0.02
price[PRI.expensive,LOC.ugly,AGE.new,SCH.good,SIZ.small]=0.05
price[PRI.expensive,LOC.ugly,AGE.new,SCH.good,SIZ.medium]=0.07
price[PRI.expensive,LOC.ugly,AGE.new,SCH.good,SIZ.large]=0.08
price[PRI.expensive,LOC.ugly,AGE.old,SCH.bad,SIZ.small]=0.03
price[PRI.expensive,LOC.ugly,AGE.old,SCH.bad,SIZ.medium]=0.06
price[PRI.expensive,LOC.ugly,AGE.old,SCH.bad,SIZ.large]=0.07
price[PRI.expensive,LOC.ugly,AGE.old,SCH.good,SIZ.small]=0.1
price[PRI.expensive,LOC.ugly,AGE.old,SCH.good,SIZ.medium]=0.2
price[PRI.expensive,LOC.ugly,AGE.old,SCH.good,SIZ.large]=0.3

nodeNB = Node(NB.identity, NB.list, neighborhood)
nodeAM = Node(AM.identity, AM.list, amentities)
nodeSIZ = Node(SIZ.identity, SIZ.list, size)
nodeLOC = Node(LOC.identity, LOC.list, location)
nodeCHI = Node(CHI.identity, CHI.list, children)
nodeSCH = Node(SCH.identity, SCH.list, school)
nodeAGE = Node(AGE.identity, AGE.list, age)
nodePRI = Node(PRI.identity, PRI.list, price)

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
nodePRI.addParent(nodeAGE)
nodePRI.addParent(nodeLOC)
nodePRI.addParent(nodeSIZ)
nodePRI.addParent(nodeSCH)
