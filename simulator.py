import json
import numpy as np
from environment import CliffWalkingEnv
from agents import QLearningAgent, SARSAAgent

def run_experiment(agent_class, episodes=500):
    env = CliffWalkingEnv()
    states = env.get_all_states()
    agent = agent_class(states, 4)
    
    rewards_per_episode = []
    
    for e in range(episodes):
        state = env.reset()
        total_reward = 0
        done = False
        
        # Initial action for SARSA
        action = agent.choose_action(state)
        
        while not done:
            next_state, reward, done = env.step(action)
            next_action = agent.choose_action(next_state)
            
            agent.update(state, action, reward, next_state, next_action, done)
            
            state = next_state
            action = next_action
            total_reward += reward
            
            # Safety break for very long episodes during early learning
            if total_reward < -2000:
                break
        
        rewards_per_episode.append(total_reward)
        
    # Get optimal path (greedy)
    path = []
    state = env.reset()
    path.append(state)
    steps = 0
    while state != env.goal_state and steps < 100:
        action = np.argmax(agent.q_table[state])
        state, _, done = env.step(action)
        path.append(state)
        steps += 1
        
    # Convert Q-table to serializable format (list of dicts or nested list)
    q_table_serializable = {f"{s[0]},{s[1]}": agent.q_table[s].tolist() for s in states}
    
    return rewards_per_episode, q_table_serializable, path

def main():
    episodes = 500
    print(f"Running Q-Learning for {episodes} episodes...")
    ql_rewards, ql_qtable, ql_path = run_experiment(QLearningAgent, episodes)
    
    print(f"Running SARSA for {episodes} episodes...")
    sarsa_rewards, sarsa_qtable, sarsa_path = run_experiment(SARSAAgent, episodes)
    
    results = {
        "episodes": episodes,
        "q_learning": {
            "rewards": ql_rewards,
            "q_table": ql_qtable,
            "path": ql_path
        },
        "sarsa": {
            "rewards": sarsa_rewards,
            "q_table": sarsa_qtable,
            "path": sarsa_path
        }
    }
    
    with open('results.json', 'w') as f:
        json.dump(results, f)
    print("Results saved to results.json")

if __name__ == "__main__":
    main()
