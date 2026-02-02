import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams

# 设置中文字体和显示参数
rcParams['font.sans-serif'] = ['SimHei']
rcParams['axes.unicode_minus'] = False
plt.rcParams.update({'font.size': 20})

# 定义激励信号 chi_{[0,1]}(t)
def chi_01(t):
    return ((t >= 0) & (t <= 1)).astype(float)

# 定义响应公式
def response(t):
    chi = chi_01(t)
    u = (t >= 0).astype(float)
    min_t1 = np.minimum(t, 1)
    term = 0.5 * (1 - np.exp(-2 * min_t1)) * np.exp(-2 * (t - min_t1))
    return chi - u * term

# 时间范围
T = 3
N = 1000
t = np.linspace(-0.5, T, N)

# 计算激励和响应
e_t = chi_01(t)
y_t = response(t)

# 绘图
plt.figure(figsize=(14, 7))
plt.plot(t, e_t, label='激励 $e(t)=\chi_{[0,1]}(t)$', color='blue', linewidth=1.2)
plt.plot(t, y_t, label='响应 $y(t)$', color='orange', linewidth=1.2)
plt.xlabel('时间 t', fontsize=20)
plt.ylabel('幅度', fontsize=20)
plt.grid(True, alpha=0.3)
plt.legend(loc='upper right', fontsize=20)
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
plt.tight_layout()
plt.show()
