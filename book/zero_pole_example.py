import matplotlib.pyplot as plt
import numpy as np

# Create figure and axis
fig, ax = plt.subplots(figsize=(6, 6))

# Set up the plot limits and labels
ax.axhline(0, color='black', linewidth=1)
ax.axvline(0, color='black', linewidth=1)
ax.set_xlabel('Re(s)',fontsize=20)
ax.set_ylabel('Im(s)',fontsize=20)
ax.set_xticks([])
ax.set_yticks([])
# ax.grid(True, which='both', linestyle='--', alpha=0.6)
ax.set_xlim(-4, 2)
ax.set_ylim(-4, 4)
ax.set_aspect('equal')

# Poles and Zeros
# H(s) = 1 / ((s+1-3j)*(s+1+3j))
# Zeros: None
# Poles at s = -1 + 3j, s = -1 - 3j

poles_real = [-1, -1]
poles_imag = [3, -3]
zeros = []

# Plot Poles
# Use 'x' for poles
ax.plot(poles_real, poles_imag, 'rx', markersize=10, markeredgewidth=2, label='Pole')

# Plot Zeros
# Use 'o' for zeros
if zeros:
    ax.plot(zeros, [0]*len(zeros), 'bo', markersize=10, fillstyle='none', markeredgewidth=2, label='Zero')

# Identify overlapping pole and zero at -2
# Usually drawn as a pole with a circle around it or vice-versa
# Here just plotting both is fine, maybe offset slightly?
# The zero is usually drawn larger or the pole inside. Here they overlap.

# Add multiplicity label for the pole at -1


# Add label for pole/zero cancellation at -2 if needed, 
# but usually just show both symbols.
# With marker size 10, they will overlap.

# Save the plot
# import os
# if not os.path.exists('../Figures'):
#     os.makedirs('../Figures')


plt.legend(loc='upper right')
plt.tight_layout()
# plt.savefig('../Figures/zero_pole_example.pdf')
plt.show()
