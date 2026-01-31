import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams

rcParams["font.sans-serif"] = ["SimHei"]
rcParams["axes.unicode_minus"] = False


def main() -> None:
	fs = 4000.0
	T = 4.0
	t = np.linspace(0.0, T, int(T * fs), endpoint=False)

	f1, f2, f3, f4 = 2.0, 4.0, 6.0, 10.0
	f = (
		np.cos(2 * np.pi * f1 * t)
		+ np.cos(2 * np.pi * f2 * t)
		+ np.cos(2 * np.pi * f3 * t)
		+ np.cos(2 * np.pi * f4 * t)
	)

	win_width = 0.5
	tau = 2.0
	window = ((t >= tau - win_width / 2) & (t <= tau + win_width / 2)).astype(float)
	fs_win = f * window

	n_fft = 262144
	freqs = np.fft.rfftfreq(n_fft, d=1 / fs)

	F = np.abs(np.fft.rfft(f, n=n_fft)) * (1 / fs)
	F_win = np.abs(np.fft.rfft(fs_win, n=n_fft)) * (1 / fs)

	fig, axes = plt.subplots(2, 2, figsize=(10, 6))

	axes[0, 0].plot(t, f, color="C0")
	window_scale = 0.9 * np.max(np.abs(f))
	axes[0, 0].plot(t, window * window_scale, "--", color="C3", linewidth=1.2)

	axes[1, 0].plot(t, fs_win, color="C1")

	axes[0, 1].plot(freqs, F, color="C2")

	axes[1, 1].plot(freqs, F_win, color="C3")

	axes[0, 0].set_title("时域信号", fontsize=20)
	axes[0, 1].set_title("频域信号", fontsize=20)

	for ax in axes.flat:
		ax.set_xlabel("")
		ax.set_ylabel("")

	for ax in axes[:, 1]:
		ax.set_xlim(0, 20)

	plt.tight_layout()
	plt.show()


if __name__ == "__main__":
	main()
