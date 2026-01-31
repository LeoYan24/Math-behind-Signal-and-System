import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft, fftfreq, fftshift
from matplotlib import rcParams
rcParams['font.sans-serif'] = ['SimHei']
rcParams['axes.unicode_minus'] = False 
# 设置参数
N = 2048  # 采样点数
t = np.linspace(-10, 10, N)  # 时间轴
dt = t[1] - t[0]

# 创建一个光滑的类三角波（使用多个高斯函数的叠加）
def create_smooth_triangular_wave(t):
    # 使用三个高斯函数叠加形成光滑的类三角波
    wave = np.exp(-t**2 / 0.3) * 1.2 

    
    # 添加一些高频成分以模拟真实波形
    wave += 0.2 * np.sin(8 * t) * np.exp(-t**2 / 4)
    
    # 标准化
    wave = wave / np.max(np.abs(wave))
    
    return wave

# 色散函数：模拟频率依赖的相位变化
def apply_dispersion(wave_t, t, dispersion_factor=0.5):
    # 傅里叶变换到频域
    wave_f = fft(wave_t)
    freq = fftfreq(len(t), dt)
    
    # 色散效应：相位随频率平方变化
    # 在色散介质中，不同频率分量传播速度不同
    dispersion = np.exp(1j * dispersion_factor * freq**2 * len(t) * 0.001)
    
    # 应用色散
    wave_f_dispersed = wave_f * dispersion
    
    # 回到时域
    wave_dispersed = np.real(np.fft.ifft(wave_f_dispersed))
    
    return wave_dispersed, wave_f, wave_f_dispersed, freq

# 创建初始波形
initial_wave = create_smooth_triangular_wave(t)

# 应用色散（展宽效应）
dispersed_wave, initial_freq_domain, dispersed_freq_domain, freq = apply_dispersion(
    initial_wave, t, dispersion_factor=2.0
)

# 计算频谱幅度
freq_magnitude_initial = np.abs(fftshift(initial_freq_domain))
freq_magnitude_dispersed = np.abs(fftshift(dispersed_freq_domain))
freq_shifted = fftshift(freq)

# 创建图形
plt.figure(figsize=(16, 12))

# 子图1: 初始波形
ax1 = plt.subplot(2, 3, 1)
plt.plot(t, initial_wave, 'b-', linewidth=2)
plt.title('初始波形', fontsize=20)
#plt.xlabel('时间', fontsize=12, fontproperties='SimHei')
#plt.ylabel('振幅', fontsize=12, fontproperties='SimHei')
plt.grid(True, alpha=0.3)
plt.axhline(y=0, color='k', linestyle='-', alpha=0.3)
plt.fill_between(t, 0, initial_wave, where=initial_wave>0, alpha=0.3, color='blue')

# 子图2: 展宽后的波形
ax2 = plt.subplot(2, 3, 4)
plt.plot(t, dispersed_wave, 'r-', linewidth=2)
plt.title('色散后波形 ', fontsize=20)
#plt.xlabel('时间', fontsize=12, fontproperties='SimHei')
#plt.ylabel('振幅', fontsize=12, fontproperties='SimHei')
plt.grid(True, alpha=0.3)
plt.axhline(y=0, color='k', linestyle='-', alpha=0.3)
plt.fill_between(t, 0, dispersed_wave, where=dispersed_wave>0, alpha=0.3, color='red')

# 子图3: 初始波形的频谱
ax3 = plt.subplot(2, 3, 2)
# 只显示主要频率成分
mask = (freq_shifted > -5) & (freq_shifted < 5)
plt.plot(freq_shifted[mask], freq_magnitude_initial[mask], 'b-', linewidth=2)
plt.title('初始幅度谱', fontsize=20)
#plt.xlabel('频率', fontsize=12, fontproperties='SimHei')
#plt.ylabel('幅度', fontsize=12, fontproperties='SimHei')
plt.grid(True, alpha=0.3)
plt.axhline(y=0, color='k', linestyle='-', alpha=0.3)
plt.fill_between(freq_shifted[mask], 0, freq_magnitude_initial[mask], alpha=0.3, color='blue')

# 子图4: 展宽后波形的频谱
ax4 = plt.subplot(2, 3, 5)
plt.plot(freq_shifted[mask], freq_magnitude_dispersed[mask], 'r-', linewidth=2)
plt.title('色散后幅度谱', fontsize=20)
#plt.xlabel('频率', fontsize=12, fontproperties='SimHei')
#plt.ylabel('幅度', fontsize=12, fontproperties='SimHei')
plt.grid(True, alpha=0.3)
plt.axhline(y=0, color='k', linestyle='-', alpha=0.3)
plt.fill_between(freq_shifted[mask], 0, freq_magnitude_dispersed[mask], alpha=0.3, color='red')


# 新增：相位谱（放在第二行）
phase_initial = np.angle(fftshift(initial_freq_domain))
phase_dispersed = np.angle(fftshift(dispersed_freq_domain))

# 子图5：初始波形相位谱
ax5 = plt.subplot(2, 3, 3)
plt.plot(freq_shifted[mask], phase_initial[mask], 'b-', linewidth=2)
plt.title('初始相位谱', fontsize=20)
#plt.xlabel('频率', fontsize=12, fontproperties='SimHei')
#plt.ylabel('相位 (弧度)', fontsize=12, fontproperties='SimHei')
plt.grid(True, alpha=0.3)

# 子图6：色散后波形相位谱
ax6 = plt.subplot(2, 3, 6)
plt.plot(freq_shifted[mask], phase_dispersed[mask], 'r-', linewidth=2)
plt.title('色散后相位谱', fontsize=20)
#plt.xlabel('频率', fontsize=12, fontproperties='SimHei')
#plt.ylabel('相位 (弧度)', fontsize=12, fontproperties='SimHei')
plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()
