import numpy as np
import random

class BaseAgent:
    def __init__(self, states, actions, alpha=0.1, gamma=0.9, epsilon=0.1):
        self.q_table = {state: np.zeros(actions) for state in states}
        self.alpha = alpha
        self.gamma = gamma
        self.epsilon = epsilon
        self.actions = actions

    def choose_action(self, state):
        if random.random() < self.epsilon:
            return random.randint(0, self.actions - 1)
        else:
            return np.argmax(self.q_table[state])

    def update(self, state, action, reward, next_state, next_action, done):
        pass

class QLearningAgent(BaseAgent):
    def update(self, state, action, reward, next_state, next_action, done):
        best_next_action = np.argmax(self.q_table[next_state])
        td_target = reward + (self.gamma * self.q_table[next_state][best_next_action] if not done else 0)
        td_error = td_target - self.q_table[state][action]
        self.q_table[state][action] += self.alpha * td_error

class SARSAAgent(BaseAgent):
    def update(self, state, action, reward, next_state, next_action, done):
        td_target = reward + (self.gamma * self.q_table[next_state][next_action] if not done else 0)
        td_error = td_target - self.q_table[state][action]
        self.q_table[state][action] += self.alpha * td_error
