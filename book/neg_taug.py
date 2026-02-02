import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams

# 设置中文字体和显示参数
rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
rcParams['axes.unicode_minus'] = False    # 用来正常显示负号
plt.rcParams.update({'font.size': 20})

# 参数
omega_m = 1
omega_c = 5

t = np.linspace(0, 8 * np.pi, 2000)

# 激励信号 e(t)
et = np.cos(omega_m * t) * np.cos(omega_c * t)

# 响应 y(t)
# y(t) = cos(t)cos(10t) - 1/2 u(t)[(2cos(11t)+11sin(11t)-2e^{-2t})/125 + (2cos(9t)+9sin(9t)-2e^{-2t})/85]
def y_response(t):
    u = (t >= 0).astype(float)
    term1 = (np.cos(4 * t) + 2 * np.sin(4 * t) - np.exp(-2 * t)) / 10
    term2 = (np.cos(6 * t) + 3 * np.sin(6 * t) - np.exp(-2 * t)) / 20
    return np.cos(omega_m * t) * np.cos(omega_c * t) - 0.5 * u * (term1 + term2)

yt = y_response(t)

# 绘图

plt.figure(figsize=(14, 7))  # 放大图形

# 减少周期数（例如 0 到 3*pi）
t = np.linspace(0, 3 * np.pi, 1200)
et = np.cos(omega_m * t) * np.cos(omega_c * t)
yt = y_response(t)
envelope = np.abs(np.cos(omega_m * t))

# 绘制激励、响应和包络在同一张图，减小线宽
plt.plot(t, et, label='e(t) 激励', color='blue', alpha=0.7, linewidth=0.8)
plt.plot(t, yt, label='y(t) 响应', color='orange', alpha=0.7, linewidth=0.8)
plt.plot(t, envelope, 'r--', linewidth=0.7, label='包络')
plt.plot(t, -envelope, 'r--', linewidth=0.7)
plt.xlabel('时间 t', fontsize=20)
plt.ylabel('幅度', fontsize=20)
plt.grid(True, alpha=0.3)
plt.legend(loc='upper right', fontsize=20)

# 设置刻度字体大小
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)

plt.tight_layout()
plt.show()
