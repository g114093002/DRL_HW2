# DRL HW2: Cliff Walking - Q-Learning vs. SARSA

[![RL Comparison](https://img.shields.io/badge/Reinforcement_Learning-Q--Learning_vs._SARSA-blue.svg)](https://github.com/g114093002/DRL_HW2)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

本專案實作並深入比較了兩種經典的強化學習演算法：**Q-Learning** (Off-policy) 與 **SARSA** (On-policy)，並以經典的 **Cliff Walking** 網格環境作為實驗場景。

## 📍 環境描述
- **地圖大小**: 4x12
- **獎勵機制**:
  - 每走一步: -1
  - 掉入懸崖: -100 (並回到起點)
  - 到達終點: 回合結束
- **參數設定**:
  - $\epsilon = 0.1$
  - $\alpha = 0.1$
  - $\gamma = 0.9$
  - 訓練回合: 500 次

## 📈 學習表現與收斂分析

![Learning Curves](reward_comparison.png)

### 比較討論
| 特性 | Q-Learning | SARSA |
| :--- | :--- | :--- |
| **類型** | Off-policy (離策略) | On-policy (同策略) |
| **收斂穩定性** | 較低，訓練中頻繁掉入懸崖 | 較高，整體回報較平穩 |
| **策略偏向** | **冒險型**。追求理論最優路徑。 | **保守型**。追求實際運行中的安全性。 |
| **線上表現** | 較差 (因為會一直嘗試踩邊緣) | 較佳 (會與邊緣保持安全距離) |

## 🗺️ 最終策略路徑視覺化

### Q-Learning 最優路徑 (RISKY)
![Q-Learning Path](ql_path.png)
*Q-Learning 學習到了緊貼懸崖的最短路徑。由於它在更新時假設未來會採取最優行動 ($max Q$)，因此它忽略了隨機探索 ($\epsilon$) 可能導致掉入懸崖的風險。*

### SARSA 最優路徑 (SAFE)
![SARSA Path](sarsa_path.png)
*SARSA 選擇向上繞道。因為 SARSA 是同策略演算法，它在學習時會考慮到實際執行的 $\epsilon$-greedy 策略。如果走在懸崖邊緣，即使最優行動是向右，探索行為仍有 10% 的機率向下踩空，因此 SARSA 選擇了一條更穩健的路徑。*

## 🚀 如何運行
1. 安裝依賴:
   ```bash
   pip install numpy matplotlib
   ```
2. 執行訓練與繪圖:
   ```bash
   python simulator.py
   python generate_plots.py
   ```
3. 查看即時數據儀表板 (選用):
   - 直接打開 `dashboard/index.html`

## 📝 結論
1. **收斂速度**: Q-Learning 雖然能學到較短的路徑，但在訓練過程中累積的總懲罰遠大於 SARSA。
2. **穩定性**: SARSA 在存在隨機擾動時展現了更好的魯棒性 (Robustness)。
3. **場景選擇**: 
   - 如果環境容錯率高且追求效率，選擇 **Q-Learning**。
   - 如果是實體機器人或有昂貴代價的高風險環境，**SARSA** 是更安全的選擇。

---
Created by Antigravity for DRL HW2.
