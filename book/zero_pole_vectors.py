import matplotlib.pyplot as plt
import numpy as np

# Define points
zeros = [1+0j]           # zero at 1
poles = [-2+0j, -3+0j]   # poles at -2 and -3
endpoint = 0+5j          # vector endpoint at 5i

# Create plot
fig, ax = plt.subplots(figsize=(6,6))

# Plot axes
ax.axhline(0, color='black', linewidth=1)
ax.axvline(0, color='black', linewidth=1)

# Plot zeros and poles
ax.plot([z.real for z in zeros], [z.imag for z in zeros], 'bo', markersize=10, markeredgewidth=2, fillstyle='none', label='Zero')
ax.plot([p.real for p in poles], [p.imag for p in poles], 'rx', markersize=10, markeredgewidth=2, label='Pole')

# Plot endpoint (no legend entry)
ax.plot(endpoint.real, endpoint.imag, 'k^', markersize=8)

# Draw vectors from each zero/pole to endpoint
for z in zeros:
    # zero vectors in blue
    ax.annotate('', xy=(endpoint.real, endpoint.imag), xytext=(z.real, z.imag),
                arrowprops=dict(arrowstyle='->', color='blue', linewidth=1.8))
for p in poles:
    # pole vectors in red
    ax.annotate('', xy=(endpoint.real, endpoint.imag), xytext=(p.real, p.imag),
                arrowprops=dict(arrowstyle='->', color='red', linewidth=1.8))

# Labels and appearance
# increase axis label font size
ax.set_xlabel('Re(s)', fontsize=18)
ax.set_ylabel('Im(s)', fontsize=18)
# hide numeric ticks but keep axis lines
ax.set_xticks([])
ax.set_yticks([])
ax.set_aspect('equal')

# Set limits to include all points comfortably
all_re = [z.real for z in zeros] + [p.real for p in poles] + [endpoint.real]
all_im = [z.imag for z in zeros] + [p.imag for p in poles] + [endpoint.imag]
pad_re = (max(all_re) - min(all_re)) * 0.5 + 1
pad_im = (max(all_im) - min(all_im)) * 0.2 + 1
ax.set_xlim(min(all_re)-pad_re, max(all_re)+pad_re)
ax.set_ylim(min(all_im)-pad_im, max(all_im)+pad_im)

ax.legend(loc='upper right', fontsize=14)
plt.tight_layout()
plt.show()
