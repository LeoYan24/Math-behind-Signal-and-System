import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.size'] = 20
plt.rcParams['legend.fontsize'] = 20
plt.rcParams['figure.titlesize'] = 20
# 频率范围
w = np.linspace(-np.pi, np.pi, 1000)
ymin, ymax = -0.2, 1.2  # 统一y轴范围

# 低通滤波器系统函数（理想）
H_low = np.where(np.abs(w) <= np.pi/3, 1, 0)
H_high = 1 - H_low  # 互补
H_band = np.where((np.abs(w) >= np.pi/3) & (np.abs(w) <= 2*np.pi/3), 1, 0)
H_stop = 1 - H_band  # 互补

plt.figure(figsize=(12, 8))

plt.subplot(2, 2, 1)
plt.plot(w, H_low, 'b')
plt.title('低通滤波器系统函数', fontproperties='SimHei')
plt.grid(True, alpha=0.3)
plt.xlim(-np.pi, np.pi)
plt.ylim(ymin, ymax)
plt.axhline(0, color='k', linewidth=0.8, alpha=0.5)
plt.axvline(0, color='k', linewidth=0.8, alpha=0.5)
plt.xticks([])
plt.yticks([])

plt.subplot(2, 2, 2)
plt.plot(w, H_high, 'r')
plt.title('高通滤波器系统函数', fontproperties='SimHei')
plt.grid(True, alpha=0.3)
plt.xlim(-np.pi, np.pi)
plt.ylim(ymin, ymax)
plt.axhline(0, color='k', linewidth=0.8, alpha=0.5)
plt.axvline(0, color='k', linewidth=0.8, alpha=0.5)
plt.xticks([])
plt.yticks([])

plt.subplot(2, 2, 3)
plt.plot(w, H_band, 'g')
plt.title('带通滤波器系统函数', fontproperties='SimHei')
plt.grid(True, alpha=0.3)
plt.xlim(-np.pi, np.pi)
plt.ylim(ymin, ymax)
plt.axhline(0, color='k', linewidth=0.8, alpha=0.5)
plt.axvline(0, color='k', linewidth=0.8, alpha=0.5)
plt.xticks([])
plt.yticks([])

plt.subplot(2, 2, 4)
plt.plot(w, H_stop, 'm')
plt.title('带阻滤波器系统函数', fontproperties='SimHei')
plt.grid(True, alpha=0.3)
plt.xlim(-np.pi, np.pi)
plt.ylim(ymin, ymax)
plt.axhline(0, color='k', linewidth=0.8, alpha=0.5)
plt.axvline(0, color='k', linewidth=0.8, alpha=0.5)
plt.xticks([])
plt.yticks([])

plt.tight_layout()
plt.show()
