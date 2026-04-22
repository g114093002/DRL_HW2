# 強化學習演算法比較實驗（HW2）對話紀錄導出

**日期**: 2026-04-22
**專案名稱**: Cliff Walking: Q-Learning vs SARSA
**參與者**: 使用者 (USER) & Antigravity (AI)

---

## 1. 需求分析與規格制定 (OpenSpec Phase)
**USER**: 請求實作 Q-Learning 與 SARSA，環境為 Cliff Walking，包含累積獎勵圖表、路徑視覺化、穩定性分析及理論比較。
**Antigravity**: 
- 初始化 OpenSpec 管理流程。
- 建立 `proposal.md`、`design.md` 與 `tasks.md`。
- 確定使用 Python 進行模擬，並開發 Web Dashboard 進行專業呈現。

## 2. 演算法實作與模擬 (Implementation Phase)
**Antigravity**:
- 實作 `environment.py`: 建立 4x12 網格與懸崖懲罰邏輯。
- 實作 `agents.py`: Q-Learning (Off-policy) 與 SARSA (On-policy) 核心。
- 實作 `simulator.py`: 執行 500 回合訓練並生成 `results.json` 數據。

## 3. 數據視覺化與報告生成 (Visualization Phase)
**Antigravity**:
- 開發基於 Vanilla CSS 與 Chart.js 的網頁儀表板。
- 展示兩種演算法在相同 ε-greedy 策略下的行為差異。
- 輸出靜態圖表 `reward_comparison.png`、`ql_path.png`、`sarsa_path.png` 供報告使用。

## 4. GitHub 部署與最終檢查 (Deployment Phase)
**USER**: 要求將專案推送到指定的 GitHub 儲存庫，並完善 README 內容，確保符合學術要求。
**Antigravity**:
- 初始化 Git 並推送至 `https://github.com/g114093002/DRL_HW2.git`。
- 根據作業要求修正 README，加入「五、理論比較與討論」與「六、結論」。
- 確認包含收斂速度、穩定性及應用場景建議。

---

## 核心結論總結

### 演算法比較
| 特性 | Q-Learning | SARSA |
| :--- | :--- | :--- |
| **策略本質** | 離策略 (Off-policy) - 注重目標最優 | 同策略 (On-policy) - 注重過程安全 |
| **路徑選擇** | 最短路徑 (13步)，存在高踩空風險 | 避險路徑 (17步)，確保整體穩定性 |
| **收斂波動** | 極高 (負回報次數多) | 較低 (學習曲線平穩) |

### 專家建議
- 在**模擬測試**中追求極限性能時，選用 **Q-Learning**。
- 在**實體部署**或具有**高度隨機性**的環境中，選用 **SARSA** 以確保系統安全。

---
*本文件由 Antigravity 自動生成，作為實驗報告之附件。*
