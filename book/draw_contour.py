import matplotlib.pyplot as plt

def draw_contour():
    # 参数设置
    b = 1.0
    r = 3.0

    # 顶点坐标
    # z1 = b - ir
    # z2 = b + ir
    # z3 = -r + ir
    # z4 = -r - ir

    # 坐标点 (x, y)
    # 左侧围道逆时针方向: (b, -r) -> (b, r) -> (-r, r) -> (-r, -r) -> (b, -r)
    points1 = [
        (b, -r),  # b - ir
        (b, r),   # b + ir
        (-r, r),  # -r + ir
        (-r, -r), # -r - ir
        (b, -r)   # 回到起点
    ]

    x1 = [p[0] for p in points1]
    y1 = [p[1] for p in points1]

    # 右侧围道（原始逆时针方向）: (b, -r) -> (r, -r) -> (r, r) -> (b, r) -> (b, -r)
    # 现在要求反向，变为顺时针，但轮廓线仍沿原路径绘制（保持坐标点顺序不变），仅改变箭头方向
    points2 = [
        (b, -r),
        (r, -r),
        (r, r),
        (b, r),
        (b, -r)
    ]

    x2 = [p[0] for p in points2]
    y2 = [p[1] for p in points2]

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

    # --- 左侧围道 (ax1) ---
    # 绘制矩形轮廓
    ax1.plot(x1, y1, 'k-', linewidth=1.5)

    # 左侧围道箭头（保持原方向：逆时针）
    # 右侧边: (b, -r) -> (b, r) 向上
    ax1.arrow(b, 0, 0, 0.001, head_width=0.15, head_length=0.15, fc='k', ec='k', length_includes_head=True)
    # 顶部边: (b, r) -> (-r, r) 向左
    ax1.arrow((b-r)/2, r, -0.001, 0, head_width=0.15, head_length=0.15, fc='k', ec='k', length_includes_head=True)
    # 左侧边: (-r, r) -> (-r, -r) 向下
    ax1.arrow(-r, 0, 0, -0.001, head_width=0.15, head_length=0.15, fc='k', ec='k', length_includes_head=True)
    # 底部边: (-r, -r) -> (b, -r) 向右
    ax1.arrow((b-r)/2, -r, 0.001, 0, head_width=0.15, head_length=0.15, fc='k', ec='k', length_includes_head=True)

    # 标记顶点
    offset = 0.2
    ax1.text(b, -r - offset, '$b-\mathrm{i}r$', ha='center', va='top', fontsize=20)
    ax1.text(b, r + offset, '$b+\mathrm{i}r$', ha='center', va='bottom', fontsize=20)
    ax1.text(-r, r + offset, '$-r+\mathrm{i}r$', ha='center', va='bottom', fontsize=20)
    ax1.text(-r, -r - offset, '$-r-\mathrm{i}r$', ha='center', va='top', fontsize=20)

    # 设置坐标轴范围，留出一点边距
    margin = 1
    ax1.set_xlim(-r - margin, b + margin)
    ax1.set_ylim(-r - margin, r + margin)
    ax1.set_aspect('equal')
    ax1.axis('off')

    # 在图片下方添加标题 (a)
    ax1.text(0.5, -0.08, '(a)', transform=ax1.transAxes, ha='center', fontsize=18)

    # --- 右侧围道 (ax2) ---
    # 绘制矩形轮廓（路径不变）
    ax2.plot(x2, y2, 'k-', linewidth=1.5)

    # 右侧围道箭头 —— 全部反向，变为顺时针方向
    # 原底部边：向右 (b,-r)->(r,-r) ，反向为向左，箭头在底部中点向左
    ax2.arrow((b+r)/2, -r, -0.001, 0, head_width=0.15, head_length=0.15, fc='k', ec='k', length_includes_head=True)
    # 原右侧边：向上 (r,-r)->(r,r) ，反向为向下
    ax2.arrow(r, 0, 0, -0.001, head_width=0.15, head_length=0.15, fc='k', ec='k', length_includes_head=True)
    # 原顶部边：向左 (r,r)->(b,r) ，反向为向右
    ax2.arrow((b+r)/2, r, 0.001, 0, head_width=0.15, head_length=0.15, fc='k', ec='k', length_includes_head=True)
    # 原左侧边：向下 (b,r)->(b,-r) ，反向为向上
    ax2.arrow(b, 0, 0, 0.001, head_width=0.15, head_length=0.15, fc='k', ec='k', length_includes_head=True)

    # 标记顶点（与原来相同）
    ax2.text(b, -r - offset, '$b-\mathrm{i}r$', ha='center', va='top', fontsize=20)
    ax2.text(b, r + offset, '$b+\mathrm{i}r$', ha='center', va='bottom', fontsize=20)
    ax2.text(r, r + offset, '$r+\mathrm{i}r$', ha='center', va='bottom', fontsize=20)
    ax2.text(r, -r - offset, '$r-\mathrm{i}r$', ha='center', va='top', fontsize=20)

    # 设置坐标轴范围
    ax2.set_xlim(b - margin, r + margin)
    ax2.set_ylim(-r - margin, r + margin)
    ax2.set_aspect('equal')
    ax2.axis('off')

    # 在图片下方添加标题 (b)
    ax2.text(0.5, -0.08, '(b)', transform=ax2.transAxes, ha='center', fontsize=18)

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    draw_contour()