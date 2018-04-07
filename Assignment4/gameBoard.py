

class boardObject():
    def __init__(self, type, currentUtility, reward):
        self.type = type
        self.currentUtility = currentUtility
        self.reward = reward

    def getType(self):
        return self.type

    def getCurrentUtility(self):
        return self.currentUtility

    def getReward(self):
        return self.reward

    


