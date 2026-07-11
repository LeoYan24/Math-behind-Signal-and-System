import numpy as np
import matplotlib.pyplot as plt

# 设置参数（去掉0.95）
a_values = [0.2, 0.5, 0.8]
Omega = np.linspace(-1.2 * np.pi, 1.2 * np.pi, 1000)

plt.figure(figsize=(10, 6))
for a in a_values:
    S = 1 / (2* np.pi *(1 - 2 * a * np.cos(Omega) + a**2))
    plt.plot(Omega, S, label=f"a={a}")

# 竖直虚线标记 -π 和 π
vline_kwargs = dict(color='gray', linestyle='--', linewidth=1.5, alpha=0.5)
plt.axvline(-np.pi, **vline_kwargs)
plt.axvline(np.pi, **vline_kwargs)

# 文本标注 -π 和 π
ymin, ymax = plt.ylim()
offset = (ymax - ymin) * 0.05
plt.text(-np.pi, ymax - offset, r'$-\pi$', fontsize=18, color='gray',
         ha='right', va='top', backgroundcolor='w')
plt.text(np.pi, ymax - offset, r'$\pi$', fontsize=18, color='gray',
         ha='left', va='top', backgroundcolor='w')

plt.xlabel(r'$\Omega$ (rad)', fontsize=18)
plt.ylabel(r'$S_x(\Omega)$', fontsize=18)
plt.xticks(fontsize=18)
plt.yticks(fontsize=18)
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend(fontsize=18)
plt.tight_layout()
plt.show()