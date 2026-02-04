import numpy as np
import matplotlib.pyplot as plt

# 设置参数
a_values = [0.2, 0.5, 0.8, 0.95]
Omega = np.linspace(-1.2 * np.pi, 1.2 * np.pi, 1000)

plt.figure(figsize=(10, 6))
for a in a_values:
    X = 1 / (1 - a * np.exp(-1j * Omega))
    plt.plot(Omega, np.abs(X), label=f"a={a}")


# 添加竖直虚线表示 -π 和 π，颜色调浅
vline_kwargs = dict(color='gray', linestyle='--', linewidth=1.5, alpha=0.5)
plt.axvline(-np.pi, **vline_kwargs)
plt.axvline(np.pi, **vline_kwargs)

# 标注 -π 和 π，避免与曲线和图例重叠
ymin, ymax = plt.ylim()
offset = (ymax - ymin) * 0.05
plt.text(-np.pi, ymax - offset, r'$-\pi$', fontsize=20, color='gray', ha='right', va='top', backgroundcolor='w')
plt.text(np.pi, ymax - offset, r'$\pi$', fontsize=20, color='gray', ha='left', va='top', backgroundcolor='w')

plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
plt.legend(fontsize=20)
# 无标题
plt.tight_layout()
plt.show()
