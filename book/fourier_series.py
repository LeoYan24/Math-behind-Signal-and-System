import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.sans-serif'] = ['SimSun']
plt.rcParams['axes.unicode_minus'] = False

t = np.linspace(-3, 3, 600)

# 创建周期矩形脉冲
y1 = np.zeros_like(t)
pulse_positions = [-2, 0, 2]  # 脉冲中心位置
pulse_width = 1               # 脉冲宽度

for center in pulse_positions:
    mask = (t >= center - pulse_width/2) & (t <= center + pulse_width/2)
    y1[mask] = 1

# 加密频谱点数
w_dense = np.linspace(-2.5*np.pi, 2.5*np.pi, 100)  # 加密到100个点
Fk_dense = 0.5 * np.sinc(0.5 * w_dense)

# 为了对比，也画出连续的sinc函数
w_continuous = np.linspace(-2.5*np.pi, 2.5*np.pi, 1000)
sinc_continuous = 0.5 * np.sinc(0.5 * w_continuous)

# 计算相位谱（理论上sinc函数为实数，主值为0，但可展示arctan结果）
phase_dense = np.angle(Fk_dense)
phase_continuous = np.angle(sinc_continuous)

# 绘图
plt.figure(figsize=(12, 15))

plt.subplot(3, 1, 1)
plt.title('周期矩形脉冲函数', fontsize=20)
plt.grid(True, alpha=0.3)
plt.plot(t, y1, 'b-', linewidth=2)
plt.xlim(-3, 3)
plt.ylim(-0.2, 1.2)
plt.xticks([])
plt.yticks([])
plt.axhline(0, color='k', linewidth=0.8, alpha=0.5)
plt.axvline(0, color='k', linewidth=0.8, alpha=0.5)

plt.subplot(3, 1, 2)
plt.title('双边频谱', fontsize=20)
plt.grid(True, alpha=0.3)
# 绘制连续的sinc函数
plt.plot(w_continuous, sinc_continuous, 'g-', linewidth=1, alpha=0.7, label='连续sinc函数')
# 绘制加密的stem图
plt.stem(w_dense, Fk_dense, basefmt=" ")
plt.xlim(-2.5*np.pi, 2.5*np.pi)
plt.ylim(-0.2, 0.6)
plt.xticks([])
plt.yticks([])
plt.axhline(0, color='k', linewidth=0.8, alpha=0.5)
plt.axvline(0, color='k', linewidth=0.8, alpha=0.5)
plt.legend(fontsize=20)

plt.subplot(3, 1, 3)
plt.title('相频特性', fontsize=20)
plt.grid(True, alpha=0.3)
# 连续相位
plt.plot(w_continuous, phase_continuous, 'g-', linewidth=1, alpha=0.7, label='连续相位')
# 离散点相位
plt.stem(w_dense, phase_dense, basefmt=" ", linefmt='b-', markerfmt='bo', label='离散相位')
plt.xlim(-2.5*np.pi, 2.5*np.pi)
plt.ylim(-3.5, 3.5)
plt.xticks([])
plt.yticks([])
plt.axhline(0, color='k', linewidth=0.8, alpha=0.5)
plt.axvline(0, color='k', linewidth=0.8, alpha=0.5)
plt.legend(fontsize=20)

plt.tight_layout(rect=[0, 0.03, 1, 0.98])
plt.show()