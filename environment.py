import numpy as np

class CliffWalkingEnv:
    def __init__(self, width=12, height=4):
        self.width = width
        self.height = height
        self.start_state = (3, 0)
        self.goal_state = (3, 11)
        self.cliff = [(3, i) for i in range(1, 11)]
        self.current_state = self.start_state
        
    def reset(self):
        self.current_state = self.start_state
        return self.current_state
    
    def step(self, action):
        """
        Actions: 0: Up, 1: Down, 2: Left, 3: Right
        """
        r, c = self.current_state
        if action == 0: # Up
            r = max(0, r - 1)
        elif action == 1: # Down
            r = min(self.height - 1, r + 1)
        elif action == 2: # Left
            c = max(0, c - 1)
        elif action == 3: # Right
            c = min(self.width - 1, c + 1)
            
        self.current_state = (r, c)
        
        if self.current_state == self.goal_state:
            return self.current_state, -1, True
        
        if self.current_state in self.cliff:
            self.current_state = self.start_state
            return self.current_state, -100, False
        
        return self.current_state, -1, False

    def get_all_states(self):
        return [(r, c) for r in range(self.height) for c in range(self.width)]
