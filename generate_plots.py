import json
import matplotlib.pyplot as plt
import numpy as np

def generate_plots():
    with open('results.json', 'r') as f:
        data = json.load(f)
    
    episodes = data['episodes']
    ql_rewards = data['q_learning']['rewards']
    sarsa_rewards = data['sarsa']['rewards']
    
    # 1. Reward Plot
    plt.figure(figsize=(10, 6))
    plt.plot(ql_rewards, label='Q-Learning', alpha=0.6, color='#38bdf8')
    plt.plot(sarsa_rewards, label='SARSA', alpha=0.6, color='#818cf8')
    
    # Smooth the curves for better visualization
    def smooth(y, box_pts):
        box = np.ones(box_pts)/box_pts
        y_smooth = np.convolve(y, box, mode='same')
        return y_smooth
    
    plt.plot(smooth(ql_rewards, 10), color='#0284c7', linewidth=2)
    plt.plot(smooth(sarsa_rewards, 10), color='#4f46e5', linewidth=2)
    
    plt.title('Learning Performance: Q-Learning vs SARSA', fontsize=14)
    plt.xlabel('Episode')
    plt.ylabel('Total Reward')
    plt.ylim(-500, 0)
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.3)
    plt.savefig('reward_comparison.png', dpi=300, bbox_inches='tight')
    plt.close()

    # 2. Path Visualization function
    def plot_path(path, title, filename, color):
        grid = np.zeros((4, 12))
        fig, ax = plt.subplots(figsize=(12, 4))
        
        # Draw grid lines
        for x in range(13):
            ax.axvline(x, color='gray', lw=1, alpha=0.3)
        for y in range(5):
            ax.axhline(y, color='gray', lw=1, alpha=0.3)
            
        # Highlight Cliff
        for i in range(1, 11):
            ax.add_patch(plt.Rectangle((i, 0), 1, 1, color='#ef4444', alpha=0.2))
            ax.text(i+0.5, 0.5, 'CLIFF', ha='center', va='center', color='#ef4444', fontsize=8)
            
        # Start and Goal
        ax.add_patch(plt.Rectangle((0, 0), 1, 1, color='#38bdf8', alpha=0.4))
        ax.text(0.5, 0.5, 'START', ha='center', va='center', fontweight='bold')
        ax.add_patch(plt.Rectangle((11, 0), 1, 1, color='#22c55e', alpha=0.4))
        ax.text(11.5, 0.5, 'GOAL', ha='center', va='center', fontweight='bold')
        
        # Plot path
        path_x = [p[1] + 0.5 for p in path]
        path_y = [3 - p[0] + 0.5 for p in path] # Invert row for plot
        ax.plot(path_x, path_y, marker='o', color=color, linewidth=2, markersize=8, label='Optimal Path')
        
        ax.set_xlim(0, 12)
        ax.set_ylim(0, 4)
        ax.set_title(title, fontsize=14)
        ax.set_xticks([])
        ax.set_yticks([])
        plt.savefig(filename, dpi=300, bbox_inches='tight')
        plt.close()

    plot_path(data['q_learning']['path'], 'Q-Learning Optimal Path (Risky)', 'ql_path.png', '#38bdf8')
    plot_path(data['sarsa']['path'], 'SARSA Optimal Path (Safe)', 'sarsa_path.png', '#818cf8')
    print("Plots generated successfully.")

if __name__ == "__main__":
    import json as json_lib
    # Re-reading to fix the json.json_load typo if it happens
    with open('results.json', 'r') as f:
        data = json_lib.load(f)
    
    # Call the fixed logic inside the script scope
    generate_plots()
