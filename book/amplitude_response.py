import numpy as np
import matplotlib.pyplot as plt

# Define frequency range
omega = np.linspace(0, 10, 1000)

# Define system function parameters
# H(s) = K * s / ((s+1)^2 * (s+3))
# For magnitude plot, K acts as a scaling factor, set K=1 for simplicity unless specified
K = 1

# Calculate magnitude response |H(j*omega)| for a first-order low-pass filter
# Use H(s) = K * wc / (s + wc) so that DC gain = K
wc = 2.0  # cutoff frequency (rad/s)
H_jw = K * wc / (1j * omega + wc)
magnitude = np.abs(H_jw)

# Create the plot
plt.figure(figsize=(8, 6))
plt.plot(omega, magnitude, 'b-', linewidth=2)
#plt.title(r'Amplitude Frequency Response $|H(j\omega)|$', fontsize=14)
plt.xlabel(r'$\omega$ (rad/s)', fontsize=12)
plt.ylabel(r'$|H(j\omega)|$', fontsize=12)
# plt.grid(True, which='both', linestyle='--', alpha=0.6)
plt.xticks([])
plt.yticks([])
plt.xlim(0, 10)

# Mark the peak if desired
# peak_idx = np.argmax(magnitude)
# peak_omega = omega[peak_idx]
# peak_mag = magnitude[peak_idx]
# plt.plot(peak_omega, peak_mag, 'ro')
# plt.annotate(f'Peak: ({peak_omega:.2f}, {peak_mag:.2f})', 
#              xy=(peak_omega, peak_mag), 
#              xytext=(peak_omega+1, peak_mag),
#              arrowprops=dict(facecolor='black', shrink=0.05))

plt.tight_layout()

# Save the plot
# import os
# script_dir = os.path.dirname(os.path.abspath(__file__))
# figures_dir = os.path.join(script_dir, '../Figures')
# if not os.path.exists(figures_dir):
#     os.makedirs(figures_dir)
    
# output_path = os.path.join(figures_dir, 'amplitude_response.pdf')
# plt.savefig(output_path)
# print(f"Figure saved to {output_path}")

# Show the plot
plt.show()
