# Proposal: HW2 - Q-Learning vs SARSA in Cliff Walking

## Objective
Implement and compare two classic reinforcement learning algorithms, Q-Learning and SARSA, in the "Cliff Walking" environment. Analyze their learning behaviors, convergence characteristics, and strategy differences.

## Environment: Cliff Walking
- **Grid Size**: 4x12
- **State Space**: All grid positions (0-47).
- **Action Space**: Up, Down, Left, Right.
- **Rewards**:
  - Step: -1
  - Cliff: -100 (and return to Start)
  - Goal: Episode ends.
- **Start**: Bottom-left (3, 0)
- **Goal**: Bottom-right (3, 11)
- **Cliff**: Bottom row between Start and Goal (3, 1-10)

## Algorithmic Requirements
- **Algorithms**: Q-Learning (Off-policy), SARSA (On-policy).
- **Policy**: ε-greedy (ε = 0.1).
- **Learning Rate (α)**: 0.1.
- **Discount Factor (γ)**: 0.9.
- **Episodes**: 500+.

## Deliverables
1. **Source Code**: Python implementation of environment and agents.
2. **Dashboard**: A professional web-based report visualizing:
   - Learning curves (Reward per episode).
   - Final optimal paths discovered by both agents.
   - Comparative analysis of risk and stability.
3. **Report**: Comprehensive discussion on theoretical differences and experimental findings.
