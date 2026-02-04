import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# 设置中文字体和图形参数
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['font.size'] = 20
plt.rcParams['axes.labelsize'] = 20
plt.rcParams['xtick.labelsize'] = 20
plt.rcParams['ytick.labelsize'] = 20
plt.rcParams['legend.fontsize'] = 20
plt.rcParams['figure.titlesize'] = 20
# 创建图形和子图 - 3行2列
fig, axes = plt.subplots(3, 2, figsize=(15, 15))
plt.subplots_adjust(hspace=0.4, wspace=0.3)

# 定义高斯函数作为带限信号
fs_continuous = 100000  # 连续信号采样频率
dt = 1.0 / fs_continuous
# 使用 endpoint=False 避免首尾重复采样点
t_continuous = np.linspace(-1, 1, int(fs_continuous * 2), endpoint=False)  # 对称时间轴

# 创建高斯函数（时域）
sigma = 0.2  # 高斯函数的标准差
gaussian_signal = np.exp(-t_continuous**2 / (2 * sigma**2))

# 计算高斯函数的频谱（频域也是高斯函数）
freq_continuous = np.fft.fftshift(np.fft.fftfreq(len(t_continuous), d=dt))
# 将 FFT 结果乘以采样间隔 dt，以近似连续时间傅里叶变换的幅度
spectrum = np.fft.fftshift(np.fft.fft(gaussian_signal)) * dt

# 图1：高斯信号的时域图像
axes[0, 0].plot(t_continuous, gaussian_signal, 'b-', linewidth=2)

axes[0, 0].set_title('原信号 - 时域')
axes[0, 0].grid(True, alpha=0.3)
axes[0, 0].set_xlim(-1, 1)

# 图2：高斯信号的频域图像（对称显示）
axes[0, 1].plot(freq_continuous, np.abs(spectrum), 'b-', linewidth=2)

axes[0, 1].set_title('原信号 - 频域')
axes[0, 1].grid(True, alpha=0.3)
axes[0, 1].set_xlim(-15, 15)

# 使用低采样频率（演示混叠）
# 将采样率减半以使失真更明显（从 4 Hz -> 2 Hz）
fs_low = 2  # 低于理想重建所需的采样频率
t_sampled = np.arange(-1, 1, 1/fs_low)
# 创建采样信号 - 高斯函数在采样点上的值
sampled_signal = np.exp(-t_sampled**2 / (2 * sigma**2))

# 图3：频域周期化并标出时域取样点
axes[1, 0].plot(t_continuous, gaussian_signal, 'b-', linewidth=2, alpha=0.5, label='原信号')
axes[1, 0].plot(t_sampled, sampled_signal, 'ro', markersize=6, label='采样点')

axes[1, 0].set_title(f'时域采样 (fs={fs_low}Hz)')
axes[1, 0].grid(True, alpha=0.3)
axes[1, 0].legend()
axes[1, 0].set_xlim(-1, 1)

# 图4：频域周期化，显示重叠（对称显示）并标注实际发生混叠的区域
axes[1, 1].plot(freq_continuous, np.abs(spectrum), 'b-', linewidth=2, label='原频谱')

# 绘制周期化的频谱（向左和向右平移），用于显示重叠
for n in range(-3, 4):
    if n != 0:
        shifted_freq = freq_continuous + n * fs_low
        axes[1, 1].plot(shifted_freq, np.abs(spectrum), 'r-', linewidth=1, alpha=0.45)

# 计算实际发生混叠的频率区间：用阈值检测原频谱与任意平移频谱同时有显著能量的区域
nyquist = fs_low / 2
threshold = 0.05 * np.max(np.abs(spectrum))
# 构建一个布尔掩码，标记所有发生实际重叠的位置
alias_mask = np.zeros_like(freq_continuous, dtype=bool)
for n in range(-3, 4):
    if n == 0:
        continue
    # 将平移谱在 freq_continuous 网格上取样（相当于在频率轴上把谱向左右平移）
    shifted_vals = np.interp(freq_continuous, freq_continuous - n * fs_low, np.abs(spectrum), left=0, right=0)
    overlap = (np.abs(spectrum) > threshold) & (shifted_vals > threshold)
    alias_mask = alias_mask | overlap

# 将 alias_mask 连续区间转为频率区间并标注
if np.any(alias_mask):
    mask = alias_mask.astype(int)
    diff = np.diff(mask)
    starts = np.where(diff == 1)[0] + 1
    ends = np.where(diff == -1)[0] + 1
    if mask[0] == 1:
        starts = np.r_[0, starts]
    if mask[-1] == 1:
        ends = np.r_[ends, len(mask)]
    for s, e in zip(starts, ends):
        fstart = freq_continuous[s]
        fend = freq_continuous[e - 1]
        axes[1, 1].axvspan(fstart, fend, alpha=0.25, color='red', label='混叠区域' if s == starts[0] else '')


axes[1, 1].set_title('频域周期化', fontsize=20)
axes[1, 1].grid(True, alpha=0.3)
axes[1, 1].set_xlim(-15, 15)


# 图5：利用采样点还原的失真信号
# 图5：利用采样点还原的失真信号
# 先绘制原信号（浅色）以便与重建信号对比
axes[2, 0].plot(t_continuous, gaussian_signal, color='blue', linewidth=1.2, alpha=0.35, label='原信号')
axes[2, 0].plot(t_sampled, sampled_signal, 'ro', markersize=6, label='采样点')

# 从采样点重建信号（使用sinc插值）
reconstructed_signal = np.zeros_like(t_continuous)
for i, t_val in enumerate(t_continuous):
    for j, (t_sample, sample_val) in enumerate(zip(t_sampled, sampled_signal)):
        # 使用 np.sinc，它本身处理 t_val==t_sample 的情况
        reconstructed_signal[i] += sample_val * np.sinc(fs_low * (t_val - t_sample))

axes[2, 0].plot(t_continuous, reconstructed_signal, 'r-', linewidth=2, label='重建信号')

axes[2, 0].set_title('失真重建', fontsize=20)
axes[2, 0].grid(True, alpha=0.3)

axes[2, 0].set_xlim(-1, 1)

# 图6：频域加窗处理（对称显示）
# 先计算周期化频域信号的总和（将所有平移谱在同一频率网格上相加）
periodized = np.zeros_like(freq_continuous)
Ncopy = 5
for n in range(-Ncopy, Ncopy + 1):
    shifted_vals = np.interp(freq_continuous, freq_continuous - n * fs_low, np.abs(spectrum), left=0, right=0)
    periodized += shifted_vals

# 绘制周期化总谱
axes[2, 1].plot(freq_continuous, periodized, color='gray', linewidth=1.2, alpha=0.6, label='周期化频谱总和')

# 也绘制每个副本以便直观看到构成（更浅的色）
for n in range(-Ncopy, Ncopy + 1):
    if n == 0:
        continue
    shifted_vals = np.interp(freq_continuous, freq_continuous - n * fs_low, np.abs(spectrum), left=0, right=0)
    axes[2, 1].plot(freq_continuous, shifted_vals, color='gray', linewidth=0.8, alpha=0.12)

# 绘制理想低通滤波器（窗函数），把窗函数按周期化谱峰值缩放以便可视化
window = np.zeros_like(freq_continuous)
window[(freq_continuous >= -nyquist) & (freq_continuous <= nyquist)] = 1
window_scale = np.max(periodized) if np.max(periodized) > 0 else 1.0
axes[2, 1].plot(freq_continuous, window * window_scale, 'g--', linewidth=1.5, label='理想低通(缩放)')

# 绘制加窗后的周期化频谱（真实幅度）
windowed_periodized = periodized * window
axes[2, 1].plot(freq_continuous, windowed_periodized, 'r-', linewidth=2, label='加窗后周期化谱')


axes[2, 1].set_title('频域加窗', fontsize=20)
axes[2, 1].grid(True, alpha=0.3)
axes[2, 1].set_xlim(-15, 15)


# 减小子图标题字体、增大间距以避免文字重叠
plt.tight_layout()

plt.show()

