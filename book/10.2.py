import matplotlib.pyplot as plt
import numpy as np
plt.rcParams['font.size'] = 20
plt.rcParams['legend.fontsize'] = 20
plt.rcParams['figure.titlesize'] = 20
plt.rcParams['font.sans-serif'] = ['SimSun']
plt.rcParams['axes.unicode_minus'] = False

t = np.linspace(-3, 3, 600)

# 创建周期矩形脉冲
y1 = np.zeros_like(t)
pulse_positions = [-2, 0, 2]
pulse_width = 1

for center in pulse_positions:
    mask = (t >= center - pulse_width/2) & (t <= center + pulse_width/2)
    y1[mask] = 1

# 频谱计算 - 加密采样
w_dense = np.linspace(-4*np.pi, 4*np.pi, 200)
Fk_dense = 0.5 * np.sinc(0.5 * w_dense)

# 计算相位谱
# 对于实偶函数，相位为0或π（当幅值为负时）
phase_dense = np.zeros_like(Fk_dense)
phase_dense[Fk_dense < 0] = np.pi  # 幅值为负时相位为π
phase_dense[Fk_dense == 0] = 0     # 零点相位为0

# 连续的sinc函数用于对比
w_continuous = np.linspace(-4*np.pi, 4*np.pi, 1000)
sinc_continuous = 0.5 * np.sinc(0.5 * w_continuous)

# 创建3个子图
fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(12, 12))

# 1. 时域信号
ax1.plot(t, y1, 'b-', linewidth=2)
ax1.set_title('周期矩形脉冲函数', fontsize=20)

ax1.grid(True, alpha=0.3)
ax1.set_xlim(-3, 3)

# 2. 幅频特性
# 绘制连续的sinc包络


# 绘制加密的离散频谱
markerline, stemlines, baseline = ax2.stem(w_dense, Fk_dense, linefmt='r-', 
                                          markerfmt='ro', basefmt='k-')
plt.setp(markerline, markersize=3, alpha=0.7)
plt.setp(stemlines, linewidth=0.5, alpha=0.6)

ax2.set_title('幅频特性', fontsize=20)
ax2.grid(True, alpha=0.3)
ax2.set_xlim(-4*np.pi, 4*np.pi)

# 3. 相频特性
markerline, stemlines, baseline = ax3.stem(w_dense, phase_dense, linefmt='b-', 
                                          markerfmt='bo', basefmt='k-')
plt.setp(markerline, markersize=3, alpha=0.7)
plt.setp(stemlines, linewidth=0.5, alpha=0.6)

ax3.set_title('相频特性', fontsize=20)
ax3.grid(True, alpha=0.3)
ax3.set_xlim(-4*np.pi, 4*np.pi)
ax3.set_ylim(-0.5, 3.5)

# 在相频图上添加相位标注
ax3.axhline(y=0, color='green', linestyle='--', alpha=0.7, label='相位 0')
ax3.axhline(y=np.pi, color='red', linestyle='--', alpha=0.7, label='相位 π')
ax3.legend(fontsize=20)

# 在所有图上标记关键频率点
for ax in [ax2, ax3]:
    ax.axvline(x=0, color='k', linestyle='-', alpha=0.5)
    for n in range(1, 5):
        ax.axvline(x=n*np.pi, color='gray', linestyle='--', alpha=0.3)
        ax.axvline(x=-n*np.pi, color='gray', linestyle='--', alpha=0.3)

plt.tight_layout()
plt.show()