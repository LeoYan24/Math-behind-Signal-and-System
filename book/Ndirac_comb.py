import matplotlib.pyplot as plt
import numpy as np

# 设置图形
fig = plt.figure(figsize=(14, 6))
gs = fig.add_gridspec(1, 2, width_ratios=[1, 1.5])

# --- 左图：二维格点 (u=(1,2), v=(2,1)) ---
ax1 = fig.add_subplot(gs[0])

# 定义基向量
u = np.array([1, 2])
v = np.array([2, 1])

# 生成格点系数
k_range = 4
n = np.arange(-k_range, k_range + 1)
m = np.arange(-k_range, k_range + 1)
N, M = np.meshgrid(n, m)

# 计算格点坐标
X_lat = N * u[0] + M * v[0]
Y_lat = N * u[1] + M * v[1]

# 绘制格点 (进行简单的视场裁剪)
view_lim = 8
mask = (np.abs(X_lat) <= view_lim) & (np.abs(Y_lat) <= view_lim)
ax1.scatter(X_lat[mask], Y_lat[mask], color='black', s=20, zorder=5)

# 绘制二维坐标轴
ax1.plot([-view_lim - 1, view_lim + 1], [0, 0], 'k-', lw=1)
ax1.plot([0, 0], [-view_lim - 1, view_lim + 1], 'k-', lw=1)

# 标出基向量
ax1.quiver(0, 0, u[0], u[1], angles='xy', scale_units='xy', scale=1, color='red', width=0.008)
ax1.quiver(0, 0, v[0], v[1], angles='xy', scale_units='xy', scale=1, color='red', width=0.008)
ax1.text(u[0] + 0.2, u[1] + 0.2, 'u', color='red', fontsize=12, fontweight='bold')
ax1.text(v[0] + 0.2, v[1] + 0.2, 'v', color='red', fontsize=12, fontweight='bold')

# 设置二维图属性
padding = 1
ax1.set_xlim(-view_lim - padding, view_lim + padding)
ax1.set_ylim(-view_lim - padding, view_lim + padding)
ax1.set_aspect('equal')
ax1.axis('off')

# --- 右图：三维狄拉克梳状分布 ---
ax = fig.add_subplot(gs[1], projection='3d')

# 定义网格范围（稀疏）
data_range = 2
x = np.arange(-data_range, data_range + 1, 1)
y = np.arange(-data_range, data_range + 1, 1)
X, Y = np.meshgrid(x, y)

# 展平数据用于绘制
X_flat = X.flatten()
Y_flat = Y.flatten()
Z_flat = np.zeros_like(X_flat)

# 定义方向向量（仅Z方向有值，模拟冲激）
U = np.zeros_like(X_flat)
V = np.zeros_like(X_flat)
W = np.ones_like(X_flat) * 0.5  # 箭头短一些

# 1. 标出xy平面上的格点
ax.scatter(X_flat, Y_flat, Z_flat, color='black', s=10, alpha=0.6)

# 2. 绘制箭头（二维狄拉克梳状分布）
ax.quiver(X_flat, Y_flat, Z_flat, U, V, W, 
          color='blue', 
          arrow_length_ratio=0.4, # 箭头头部比例
          linewidth=1.5)

# 3. 画出三个坐标轴（手动绘制以替代默认坐标轴）
axis_len = data_range + 1
ax.plot([-axis_len, axis_len], [0, 0], [0, 0], 'k-', lw=1) # X轴
ax.plot([0, 0], [-axis_len, axis_len], [0, 0], 'k-', lw=1) # Y轴
ax.plot([0, 0], [0, 0], [-0.5, 1.5], 'k-', lw=1)           # Z轴

# 4. 坐标轴不进行标注 (关闭默认坐标轴显示)
ax.set_axis_off()
ax.set_xlim(-axis_len, axis_len)
ax.set_ylim(-axis_len, axis_len)
ax.set_zlim(-0.5, 1.5)
ax.set_box_aspect((1, 1, 0.35)) # 进一步压扁Z轴，减少空白

# 5. 设置适当观察角度，确保箭头不重合
ax.view_init(elev=35, azim=25)
ax.dist = 4.5  # 拉近视距，减少空白
plt.subplots_adjust(left=0.05, right=0.98, wspace=0.02)

plt.show()
