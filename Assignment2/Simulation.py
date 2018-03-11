# This is for the simulation of gibbs samplin
from enum import Enum
class NB(Enum):
    bad=0
    good=1

class AM(Enum):
    lots=1
    little=0



amentities={AM.lots:0.3, AM.little:0.7}
neighborhood={NB.bad:0.4, NB.good:0.6}
size={'small':0.33,'medium':0.34,'large':0.33}

#
# #children neighborhood
# children={}
# children['bad','bad']=0.6
# children['bad','good']=0.3
# children['good','bad']=0.4
# children['good','bad']=0.7
# print(children)
#
# #school children
# school={}
# school['bad','bad']=0.7
# school['bad','good']=0.8
# school['good','bad']=0.3
# school['good','good']=0.2
#
# #age location
# age={}
# age['old','good']=0.3
# age['old','bad']=0.6
# age['old','ugly']=0.9
# age['new','good']=0.7
# age['new','bad']=0.4
# age['new','ugly']=0.1
#
# #location amentities neighborhood
# location={}
# location['good','lots','bad']=0.3
# location['good','lots','good']=0.8
# location['good','little','bad']=0.2
# location['good','little','good']=0.5
# location['bad','lots','bad']=0.4
# location['bad','lots','good']=0.15
# location['bad','little','bad']=0.4
# location['bad','little','good']=0.35
# location['bad','Alots','Nbad']=0.4
