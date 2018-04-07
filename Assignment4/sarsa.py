import random

class Sarsa:
    def __init__(self, epsilon, alpha, actions):
        self.q = {}
        self.epsilon = epsilon
        self.alpha = alpha
        self.gamma = 0.7
        self.actions = actions


    def updateQ(self, state1, action1, reward, state2, action2):
        q_current = self.q.get((state1, action1))
        q_next = self.q.get((state2, action2))

        self.q[(state1, action1)] = q_current + self.alpha*(reward + self.gamma*q_next - q_current)


    def choose_action(self, state):
        if random.random() < self.epsilon:
            action = random.choice(self.actions)
        else:
            q = [self.getQ(state, a) for a in self.actions]
            maxQ = max(q)
            count = q.count(maxQ)
            if count > 1:
                best = [i for i in range(len(self.actions)) if q[i] == maxQ]
                i = random.choice(best)
            else:
                i = q.index(maxQ)

            action = self.actions[i]

        return action

