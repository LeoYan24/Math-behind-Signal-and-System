import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams

rcParams["font.sans-serif"] = ["SimHei"]
rcParams["axes.unicode_minus"] = False


def main() -> None:
	fs = 4000.0
	t = np.linspace(0.0, 4.0, int(4 * fs), endpoint=False)

	f1 = 2.0
	f2 = 4.0
	f3 = 6.0
	f4 = 10.0

	window = ((t > 0.0) & (t <= 4.0)).astype(float)

	s1_full = (
		np.cos(2 * np.pi * f1 * t)
		+ np.cos(2 * np.pi * f2 * t)
		+ np.cos(2 * np.pi * f3 * t)
		+ np.cos(2 * np.pi * f4 * t)
	)
	s1 = s1_full * window

	s2 = np.zeros_like(t)
	mask1 = (t > 0.0) & (t <= 1.0)
	mask2 = (t > 1.0) & (t <= 2.0)
	mask3 = (t > 2.0) & (t <= 3.0)
	mask4 = (t > 3.0) & (t <= 4.0)
	s2[mask1] = np.cos(2 * np.pi * f1 * t[mask1])
	s2[mask2] = np.cos(2 * np.pi * f2 * t[mask2])
	s2[mask3] = np.cos(2 * np.pi * f3 * t[mask3])
	s2[mask4] = np.cos(2 * np.pi * f4 * t[mask4])
	s2 *= window

	s3 = np.zeros_like(t)
	s3[mask1] = np.cos(2 * np.pi * f4 * t[mask1])
	s3[mask2] = np.cos(2 * np.pi * f3 * t[mask2])
	s3[mask3] = np.cos(2 * np.pi * f2 * t[mask3])
	s3[mask4] = np.cos(2 * np.pi * f1 * t[mask4])
	s3 *= window

	n = t.size
	n_fft = 26214400
	freqs = np.fft.rfftfreq(n_fft, d=1 / fs)

	fig, axes = plt.subplots(3, 2, figsize=(10, 7), sharex="col")

	axes[0, 0].plot(t, s1, color="C0")

	axes[1, 0].plot(t, s2, color="C1")

	axes[2, 0].plot(t, s3, color="C2")

	for i, s in enumerate([s1, s2, s3]):
		spectrum = np.abs(np.fft.rfft(s, n=n_fft)) * (1 / fs)
		axes[i, 1].plot(freqs, spectrum, color="C3")
		axes[i, 1].set_xlim(0, 20)

	axes[0, 0].set_title("时域信号", fontsize=20)
	axes[0, 1].set_title("频域信号", fontsize=20)

	for ax in axes.flat:
		ax.set_xlabel("")
		ax.set_ylabel("")

	plt.tight_layout()
	plt.show()


if __name__ == "__main__":
	main()
