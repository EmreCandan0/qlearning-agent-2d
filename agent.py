import random

class QLearningAgent:
    def __init__(self, actions, learning_rate=0.1, discount_factor=0.9, epsilon=0.2):
        self.q_table = {}  # {(state): {action: value}}
        self.actions = actions
        self.alpha = learning_rate
        self.gamma = discount_factor
        self.epsilon = epsilon

    def get_q_values(self, state):
        if state not in self.q_table:
            self.q_table[state] = {action: 0.0 for action in self.actions}
        return self.q_table[state]

    def choose_action(self, state):
        q_values = self.get_q_values(state)
        if random.random() < self.epsilon:
            return random.choice(self.actions)
        else:
            return max(q_values, key=q_values.get)

    def update_q(self, state, action, reward, next_state):
        q_values = self.get_q_values(state)
        next_q_values = self.get_q_values(next_state)
        best_future_q = max(next_q_values.values())
        current_q = q_values[action]

        new_q = current_q + self.alpha * (reward + self.gamma * best_future_q - current_q)
        self.q_table[state][action] = new_q

