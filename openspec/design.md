# Design: Q-Learning vs SARSA Comparison System

## Architecture Overview
The system will be split into two main parts:
1. **Simulation Core (Python)**: Handles environment logic, agent training, and data collection.
2. **Analysis Dashboard (Web)**: A modern, premium UI to display results and discuss findings.

## Components

### 1. Simulation Core
- `environment.py`: `CliffWalkingEnv` class.
- `agents.py`: `BaseAgent`, `QLearningAgent`, and `SARSAAgent` classes.
- `simulator.py`: Logic to run multiple episodes, track rewards, and export final Q-tables and training logs to `results.json`.

### 2. Analysis Dashboard
- **Visuals**:
  - **Line Chart**: Reward vs. Episode (comparative).
  - **Grid Visualizer**: Shows the 4x12 grid with heatmaps of Q-values and the agents' chosen paths.
  - **Comparison Cards**: Side-by-side stats on convergence and stability.
- **Technology Stack**:
  - HTML5, CSS3 (Vanilla), JavaScript (ES6+).
  - Chart.js or D3.js for data visualization.
  - Premium dark theme with glassmorphism effects.

## Data Schema (`results.json`)
```json
{
  "episodes": 500,
  "q_learning": {
    "rewards": [...],
    "q_table": [...],
    "path": [...]
  },
  "sarsa": {
    "rewards": [...],
    "q_table": [...],
    "path": [...]
  }
}
```
