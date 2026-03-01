import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def plot_solution_space(t0=1.0):
	# 参数与曲线定义
	t = np.linspace(-1.0, 3.0, 600)
	y = 0.8 * np.sin(1.2 * t)  # 平滑示意曲线分量
	z = 0.6 * np.cos(0.9 * t) + 0.15 * t

	y0 = 0.8 * np.sin(1.2 * t0)
	z0 = 0.6 * np.cos(0.9 * t0) + 0.15 * t0

	# 画布与三维坐标系
	fig = plt.figure(figsize=(8, 6))
	ax = fig.add_subplot(111, projection='3d')
	ax.view_init(elev=30, azim=-60)  # 斜上方视角

	# 坐标轴范围
	xmin, xmax = t.min() - 0.2, t.max() + 0.2
	ymin, ymax = y.min() - 0.5, y.max() + 0.5
	zmin, zmax = z.min() - 0.5, z.max() + 0.5
	ax.set_xlim(xmin, xmax)
	ax.set_ylim(ymin, ymax)
	ax.set_zlim(zmin, zmax)

	# 绘制三条坐标轴（仅横轴标注't'），并画出 x 轴的正方向箭头
	ax.plot([xmin, xmax], [0, 0], [0, 0], color='k', lw=1)  # x 轴
	ax.plot([0, 0], [ymin, ymax], [0, 0], color='k', lw=1)  # y 轴
	ax.plot([0, 0], [0, 0], [zmin, zmax], color='k', lw=1)  # z 轴
	ax.set_xlabel('')
	ax.set_ylabel('')
	ax.set_zlabel('')
	# 在 x 轴上绘制箭头表示正方向（与坐标轴线宽一致）
	dx = xmax - xmin
	arrow_len = 0.12 * dx
	ax.quiver(xmax - 0.06 * dx, 0, 0, arrow_len, 0, 0, color='k', arrow_length_ratio=0.3, linewidth=1)
	# 在箭头附近标注正方向集合 $\mathbb{R}$（微调位置以避免重合）
	arrow_label_x = (xmax - 0.06 * dx) + 1.3 * arrow_len
	arrow_label_y = -0.08 * (ymax - ymin)
	arrow_label_z = 0.02 * (zmax - zmin)
	ax.text(arrow_label_x, arrow_label_y, arrow_label_z, r'$\mathbb{R}$', fontsize=20, color='k')

	# 隐藏刻度与网格（不显示单位长度和刻度）
	ax.set_xticks([])
	ax.set_yticks([])
	ax.set_zticks([])
	ax.grid(False)

	# 绘制两个平面：yOz 平面（x=0）和截面 x = t0
	yy = np.linspace(ymin, ymax, 2)
	zz = np.linspace(zmin, zmax, 2)
	YY, ZZ = np.meshgrid(yy, zz)
	# yOz 平面（x = 0）——用于标注 $\mathbb{R}^n$
	XX_yOz = np.full_like(YY, 0.0)
	ax.plot_surface(XX_yOz, YY, ZZ, color='C0', alpha=0.18, linewidth=0, shade=False)
	# 截面 x = t0（用于表示 t = t0）
	XX_t0 = np.full_like(YY, t0)
	ax.plot_surface(XX_t0, YY, ZZ, color='C1', alpha=0.12, linewidth=0, shade=False)
	# 将标签放置到合适位置：在 yOz 平面放 $\mathbb{R}^n$，在原处放 t=t_0
	x_offset = 0.04 * (xmax - xmin)
	mid_y = 0.5 * (ymax + ymin)
	mid_z = 0.5 * (zmax + zmin)
	# 将标签放在平面外、靠近平面左下角以提高辨识度，统一字号为 20
	label_x_off = 0.02 * (xmax - xmin)
	label_y = ymin + 0.05 * (ymax - ymin)
	label_z = zmin + 0.05 * (zmax - zmin)
	ax.text(-label_x_off, label_y, label_z, r'$\mathbb{R}^n$', fontsize=20, color='C0')
	ax.text(t0 - label_x_off, label_y, label_z, r'$t=t_0$', fontsize=20, color='C1')

	# 绘制以 x 为自变量的平滑曲线
	ax.plot(t, y, z, color='C1', lw=2)

	# 标出与截面的交点并只标注 $(t_0,\mathbf{y}_0)$（不显示数值坐标）
	ax.scatter([t0], [y0], [z0], color='red', s=50)
	small_y_off = 0.02 * (ymax - ymin)
	small_z_off = 0.02 * (zmax - zmin)
	ax.text(t0 + 0.01 * (xmax - xmin), y0 + small_y_off, z0 + small_z_off, r'$(t_0,\mathbf{y}_0)$', fontsize=20,color='red')

	# 美化：去掉坐标轴底板/墙壁（尽量兼容不同 matplotlib 版本）
	try:
		ax.xaxis.pane.fill = False
		ax.yaxis.pane.fill = False
		ax.zaxis.pane.fill = False
	except Exception:
		pass
	try:
		# 兼容不同后端：将 pane 颜色设为透明，去掉背景墙
		ax.w_xaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
		ax.w_yaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
		ax.w_zaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
		# 也将轴背景设置为透明以防后端差异
		ax.set_facecolor((1.0, 1.0, 1.0, 0.0))
		fig.patch.set_alpha(0.0)
	except Exception:
		pass

	plt.tight_layout()
	plt.show()


if __name__ == '__main__':
	plot_solution_space(t0=1.0)

