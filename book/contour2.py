import numpy as np
import matplotlib.pyplot as plt

def draw_contour():
    b = 1.5
    r = 4
    R = np.sqrt(b**2 + r**2)

    # 角度
    theta_top = np.arctan2(r, b)
    theta_bottom = np.arctan2(-r, b)

    # 准备圆弧数据 (右侧圆弧)
    # 从 theta_bottom 逆时针画到 theta_top
    angles = np.linspace(theta_bottom, theta_top, 200)
    arc_x = R * np.cos(angles)
    arc_y = R * np.sin(angles)

    # 竖直线
    line_x = [b, b]
    line_y = [r, -r]

    plt.figure(figsize=(6, 6))
    
    # 绘制圆弧
    plt.plot(arc_x, arc_y, 'k', linewidth=1.5)
    
    # 绘制直线
    plt.plot(line_x, line_y, 'k', linewidth=1.5)

    # 标记点 b+ir, b-ir
    # plt.plot([b, b], [r, -r], 'ko', markersize=3)
    plt.text(b , r+0.2, r'$b+\mathrm{i}r$', fontsize=18)
    plt.text(b , -r-0.5, r'$b-\mathrm{i}r$', fontsize=18)
    
    # 绘制虚线连接原点和圆弧上一点
    mid_angle = theta_top / 2
    mid_x = R * np.cos(mid_angle)
    mid_y = R * np.sin(mid_angle)
    plt.plot([0, mid_x], [0, mid_y], 'k--', linewidth=1)
    # 标记半径 R，稍微偏移以避免重叠
    plt.text(mid_x / 2 - 0.2, mid_y / 2 + 0.2, r'$R$', fontsize=18)

    # 设置比例相等
    plt.axis('equal')
    
    # 显示坐标轴
    ax = plt.gca()
    ax.spines['left'].set_position('zero')
    ax.spines['bottom'].set_position('zero')
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    
    # 去掉坐标轴刻度
    ax.set_xticks([])
    ax.set_yticks([])

    plt.show()

if __name__ == "__main__":
    draw_contour()
