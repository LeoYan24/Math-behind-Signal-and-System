import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams

# 设置中文字体和显示参数
rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
rcParams['axes.unicode_minus'] = False    # 用来正常显示负号

# 定义参数
omega_c = 10  # 载波角频率 (高频)
omega_m = 1   # 调制信号角频率 (低频)
t = np.linspace(0, 4*np.pi, 1000)  # 时间范围

# 计算信号
signal = 0.5 * (np.cos((omega_c + omega_m) * t) + np.cos((omega_c - omega_m) * t))

# 根据三角恒等式，这等价于 cos(omega_m * t) * cos(omega_c * t)
# 包络线就是 ±cos(omega_m * t)
envelope_upper = np.cos(omega_m * t)   # 上包络线
envelope_lower = - np.cos(omega_m * t)  # 下包络线

# 创建图形
plt.figure(figsize=(12, 8))

# 绘制信号
plt.plot(t, signal, 'b-', linewidth=1.5)

# 绘制包络线
plt.plot(t, envelope_upper, 'r--', linewidth=2)
plt.plot(t, envelope_lower, 'g--', linewidth=2)

# 设置图形属性

plt.grid(True, alpha=0.3)

# 调整坐标轴范围以更好显示
plt.ylim(-1.2, 1.2)

plt.tight_layout()
plt.show()
