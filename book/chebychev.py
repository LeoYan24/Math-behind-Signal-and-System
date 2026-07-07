import numpy as np
import matplotlib.pyplot as plt

plt.rcParams.update({'font.size': 18})

fig, axes = plt.subplots(2, 2, figsize=(12, 10))
n_values = [2, 3, 4, 5]

# 范围包含 |x|>1 的部分
x = np.linspace(-1.5, 1.5, 500)

def chebyshev_T(n, x):
    """用递推关系计算第一类切比雪夫多项式 T_n(x)"""
    if n == 0:
        return np.ones_like(x)
    elif n == 1:
        return x
    else:
        T_prev2 = np.ones_like(x)   # T_0
        T_prev1 = x                 # T_1
        for _ in range(2, n+1):
            T = 2 * x * T_prev1 - T_prev2
            T_prev2, T_prev1 = T_prev1, T
        return T_prev1

for idx, n in enumerate(n_values):
    ax = axes[idx // 2, idx % 2]
    T_n = chebyshev_T(n, x)
    ax.plot(x, T_n, linewidth=2)

    ax.set_xlabel('$x$')
    ax.set_ylabel(f'$T_{{{n}}}(x)$')
    ax.grid(True, linestyle='--', alpha=0.6)
    ax.set_xlim(-1.5, 1.5)

plt.tight_layout()
plt.show()