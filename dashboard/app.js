document.addEventListener('DOMContentLoaded', async () => {
    const response = await fetch('../results.json');
    const data = await response.json();

    // 1. Render Learning Curves
    const ctx = document.getElementById('rewardChart').getContext('2d');
    new Chart(ctx, {
        type: 'line',
        data: {
            labels: Array.from({length: data.episodes}, (_, i) => i + 1),
            datasets: [
                {
                    label: 'Q-Learning',
                    data: data.q_learning.rewards,
                    borderColor: '#38bdf8',
                    backgroundColor: 'rgba(56, 189, 248, 0.1)',
                    borderWidth: 2,
                    pointRadius: 0,
                    tension: 0.2
                },
                {
                    label: 'SARSA',
                    data: data.sarsa.rewards,
                    borderColor: '#818cf8',
                    backgroundColor: 'rgba(129, 140, 248, 0.1)',
                    borderWidth: 2,
                    pointRadius: 0,
                    tension: 0.2
                }
            ]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            scales: {
                y: {
                    beginAtZero: false,
                    grid: { color: 'rgba(255, 255, 255, 0.05)' },
                    ticks: { color: '#94a3b8' },
                    min: -500 // Adjust based on data to show interesting part
                },
                x: {
                    grid: { display: false },
                    ticks: { color: '#94a3b8', maxTicksLimit: 10 }
                }
            },
            plugins: {
                legend: { labels: { color: '#f1f5f9' } }
            }
        }
    });

    // 2. Render Grids
    renderGrid('qlGrid', data.q_learning.path);
    renderGrid('sarsaGrid', data.sarsa.path);
});

function renderGrid(containerId, path) {
    const container = document.getElementById(containerId);
    const width = 12;
    const height = 4;
    const cliffPositions = [];
    for (let i = 1; i < 11; i++) cliffPositions.push(`3,${i}`);

    for (let r = 0; r < height; r++) {
        for (let c = 0; c < width; c++) {
            const cell = document.createElement('div');
            cell.className = 'cell';
            const posStr = `${r},${c}`;

            if (r === 3 && c === 0) cell.classList.add('start');
            else if (r === 3 && c === 11) cell.classList.add('goal');
            else if (cliffPositions.includes(posStr)) cell.classList.add('cliff');

            // Add path indicator
            const pathIndex = path.findIndex(p => p[0] === r && p[1] === c);
            if (pathIndex !== -1) {
                const dot = document.createElement('div');
                dot.className = `path-node ${containerId.includes('ql') ? 'path-ql' : 'path-sarsa'}`;
                cell.appendChild(dot);
            }

            container.appendChild(cell);
        }
    }
}
