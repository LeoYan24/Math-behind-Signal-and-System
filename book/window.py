import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams
rcParams['font.sans-serif'] = ['SimHei']
rcParams['axes.unicode_minus'] = False 

def main() -> None:
	t = np.linspace(-0.5, 0.5, 1000)

	rect = (np.abs(t) <= 0.25).astype(float)
	tri = np.clip(1 - np.abs(t) / 0.25, 0, 1)

	sigma = 0.1
	gauss = np.exp(-(t ** 2) / (2 * sigma ** 2))

	n = t.size
	hamming = np.hamming(n)

	fig, axes = plt.subplots(2, 2, figsize=(8, 6))

	axes[0, 0].plot(t, rect, color="C0")
	axes[0, 0].set_title("矩形窗")

	axes[0, 1].plot(t, tri, color="C1")
	axes[0, 1].set_title("三角窗")

	axes[1, 0].plot(t, gauss, color="C2")
	axes[1, 0].set_title("高斯窗")

	axes[1, 1].plot(t, hamming, color="C3")
	axes[1, 1].set_title("汉明窗")

	for ax in axes.flat:
		ax.set_xlabel("")
		ax.set_ylabel("")

	plt.tight_layout()
	plt.show()


if __name__ == "__main__":
	main()
