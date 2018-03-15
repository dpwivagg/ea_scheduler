# This is the Node for Gibbs sampling
class Node:
    def __init__(self, identity, cpt):
        self.identity = identity
        self.cpt = cpt
        self.state = 0
        self.parents = {}  # The parent node list
        self.children = {} # The children node list
        self.isEvidence = False

    def
