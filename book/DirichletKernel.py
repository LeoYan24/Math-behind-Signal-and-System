import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.sans-serif'] = ['SimSun']
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['font.size'] = 20
plt.rcParams['axes.labelsize'] = 20
plt.rcParams['xtick.labelsize'] = 20
plt.rcParams['ytick.labelsize'] = 20
plt.rcParams['legend.fontsize'] = 20
plt.rcParams['figure.titlesize'] = 20
# 定义狄利克雷核函数
def dirichlet_kernel(x, N):
    """狄利克雷核: D_N(x) = sin((N+1/2)x) / sin(x/2)"""
    if np.allclose(x, 0):
        return 2*N + 1  # 在x=0处的极限值
    return np.sin((N + 0.5) * x) / np.sin(x / 2)

# 定义包络函数
def envelope_function(x, N):
    """包络函数: 1/|sin(x/2)|"""
    return 1 / np.abs(np.sin(x / 2))

# 参数设置
N = 10  # 核的阶数
x = np.linspace(-3*np.pi, 3*np.pi, 2000)
x = x[~np.isclose(x, 0)]  # 移除零点附近避免除零

# 计算狄利克雷核和包络
D_N = dirichlet_kernel(x, N)
envelope_upper = envelope_function(x, N)
envelope_lower = -envelope_upper

# 创建图形
plt.figure(figsize=(14, 10))

# 绘制狄利克雷核
plt.plot(x, D_N, 'b-', linewidth=1.5, alpha=0.8, label=f'狄利克雷核')

# 绘制包络线
plt.plot(x, envelope_upper, 'r--', linewidth=2, alpha=0.7, label='包络: 1/|sin(x/2)|')
plt.plot(x, envelope_lower, 'r--', linewidth=2, alpha=0.7)

# 填充包络区域
plt.fill_between(x, envelope_lower, envelope_upper, color='red', alpha=0.1)

# 标记主瓣和旁瓣
main_lobe_mask = (x > -2*np.pi/(2*N+1)) & (x < 2*np.pi/(2*N+1))
plt.fill_between(x[main_lobe_mask], D_N[main_lobe_mask], 0, color='blue', alpha=0.2, label='主瓣')

# 设置图形属性
plt.title(f'狄利克雷核及其包络特性', fontsize=20, fontweight='bold')

plt.grid(True, alpha=0.3)
plt.legend(fontsize=20)

# 设置坐标轴范围
plt.ylim(-3*N, 3*N)
plt.xlim(-3*np.pi, 3*np.pi)

# 标记关键点
plt.axhline(y=0, color='k', linewidth=0.5)
plt.axvline(x=0, color='k', linewidth=0.5)

# 标记包络的奇点
for k in range(-3, 4):
    if k != 0:
        plt.axvline(x=2*k*np.pi, color='orange', linestyle=':', alpha=0.5, 
                   label='包络奇点' if k == 1 else "")

plt.tight_layout()
plt.show()