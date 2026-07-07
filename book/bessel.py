import numpy as np
import matplotlib.pyplot as plt
from scipy.special import jv

# 设置全局字体大小
plt.rcParams.update({'font.size': 18})

# 创建2x2子图
fig, axes = plt.subplots(2, 2, figsize=(12, 10))
n_values = [0, 1, 2, 3]

# 定义正半轴x范围（0 到 20）
x = np.linspace(0, 20, 500)

for idx, n in enumerate(n_values):
    ax = axes[idx // 2, idx % 2]
    # 第一类贝塞尔函数 J_n(x)
    J_n = jv(n, x)
    ax.plot(x, J_n, linewidth=2)

    ax.set_xlabel('$x$')
    ax.set_ylabel(f'$J_{{{n}}}(x)$')
    ax.grid(True, linestyle='--', alpha=0.6)
    ax.set_xlim(0, 20)

plt.tight_layout()
plt.show()