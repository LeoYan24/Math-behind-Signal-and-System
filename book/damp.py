import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimSun']
plt.rcParams['axes.unicode_minus'] = False


t = np.linspace(0, 15, 1000)
L, C, E = 1.0, 1.0, 1.0
Rs = [3.0, 2.0, 1.0] # Over, Critical, Under
titles = ['过阻尼', '临界阻尼', '欠阻尼']

fig, axes = plt.subplots(1, 3, figsize=(12, 4))

for i, R in enumerate(Rs):
    if R**2 > 4*L/C: # Overdamped
        d = np.sqrt(R**2 - 4*L/C)
        r1, r2 = (-R + d)/(2*L), (-R - d)/(2*L)
        it = (E/(L*(r1-r2))) * (np.exp(r1*t) - np.exp(r2*t))
    elif R**2 == 4*L/C: # Critical
        r = -R/(2*L)
        it = (E/L) * t * np.exp(r*t)
    else: # Underdamped
        alpha = -R/(2*L)
        beta = np.sqrt(4*L/C - R**2)/(2*L)
        it = (E/(L*beta)) * np.exp(alpha*t) * np.sin(beta*t)
        
    axes[i].plot(t, it)
    axes[i].set_title(titles[i], fontsize=20)
    axes[i].grid(True)

plt.tight_layout()
plt.show()
