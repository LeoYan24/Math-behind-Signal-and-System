import numpy as np
import matplotlib.pyplot as plt

from matplotlib import rcParams
# 设置中文字体和全局字体大小
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['font.size'] = 20
plt.rcParams['axes.labelsize'] = 20
plt.rcParams['xtick.labelsize'] = 20
plt.rcParams['ytick.labelsize'] = 20
plt.rcParams['legend.fontsize'] = 20
plt.rcParams['figure.titlesize'] = 20

# 创建图形
plt.figure(figsize=(12, 8))

# 定义原高频余弦信号
f_original = 5.0  # 高频信号频率
t_continuous = np.linspace(0, 2, 1000)  # 连续时间轴
continuous_signal = np.cos(2 * np.pi * f_original * t_continuous)  # 连续高频余弦信号

# 使用低采样率进行采样
fs_low = 6  # 低采样频率（低于奈奎斯特频率）
t_sampled = np.arange(0, 2, 1/fs_low)
sampled_signal = np.cos(2 * np.pi * f_original * t_sampled)

# 计算混叠后的低频信号频率（根据采样定理）
f_alias = abs(fs_low - f_original)  # 混叠频率
alias_signal = np.cos(2 * np.pi * f_alias * t_continuous)  # 混叠后的信号

# 绘制原信号（浅色）
plt.plot(t_continuous, continuous_signal, 'lightblue', linewidth=2, alpha=0.7, label='原高频信号 (5Hz)')

# 绘制采样点
plt.plot(t_sampled, sampled_signal, 'ro', markersize=8, label='采样点')

# 绘制混叠信号
plt.plot(t_continuous, alias_signal, 'red', linewidth=2, linestyle='--', label='混叠低频信号 (1Hz)')

# 添加连接采样点的虚线

# 设置图形属性
plt.xlabel('时间 (s)', fontsize=20)
plt.ylabel('幅度', fontsize=20)
plt.grid(True, alpha=0.3)
plt.legend(loc='upper right', fontsize=20)
plt.xlim(0, 2)
plt.ylim(-1.2, 1.2)


# 添加采样频率信息


plt.tight_layout()
plt.show()