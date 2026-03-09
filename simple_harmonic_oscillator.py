import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

# Initial parameters
m0 = 1.0
k0 = 4.0
b0 = 0.5
F0 = 0.5
omega_d0 = 2.0

t = np.linspace(0, 20, 2000)

fig, ax = plt.subplots(figsize=(10, 6))
plt.subplots_adjust(bottom=0.35)

l1, = ax.plot(t, 0.5 * np.cos(np.sqrt(k0/m0) * t), label='Undamped', alpha=0.7)
l2, = ax.plot(t, 0.5 * np.exp(-b0*t/(2*m0)) * np.cos(np.sqrt((k0/m0) - (b0/(2*m0))**2) * t), label='Damped', alpha=0.7)
l3, = ax.plot(t, (F0/m0) / np.sqrt(((k0/m0) - omega_d0**2)**2 + (b0*omega_d0/m0)**2) * np.cos(omega_d0 * t - np.pi/2), label='Forced', alpha=0.7)

ax.set_xlabel('Time (s)')
ax.set_ylabel('Displacement (m)')
ax.set_title('Interactive Harmonic Oscillator Simulation (Drag sliders to change parameters)')
ax.grid(True)
ax.legend()

# Sliders
ax_m = plt.axes([0.15, 0.15, 0.65, 0.03])
ax_k = plt.axes([0.15, 0.10, 0.65, 0.03])
ax_b = plt.axes([0.15, 0.05, 0.65, 0.03])
ax_F = plt.axes([0.15, 0.00, 0.65, 0.03])

s_m = Slider(ax_m, 'Mass m', 0.1, 5.0, valinit=m0)
s_k = Slider(ax_k, 'Spring constant k', 1.0, 20.0, valinit=k0)
s_b = Slider(ax_b, 'Damping b', 0.0, 2.0, valinit=b0)
s_F = Slider(ax_F, 'Driving force F', 0.0, 5.0, valinit=F0)

def update(val):
    m = s_m.val
    k = s_k.val
    b = s_b.val
    F = s_F.val
    omega0 = np.sqrt(k / m)
    
    l1.set_ydata(0.5 * np.cos(omega0 * t))
    l2.set_ydata(0.5 * np.exp(-b*t/(2*m)) * np.cos(np.sqrt(omega0**2 - (b/(2*m))**2) * t))
    l3.set_ydata((F / m) / np.sqrt((omega0**2 - omega_d0**2)**2 + (b*omega_d0/m)**2) * np.cos(omega_d0 * t - np.pi/2))
    fig.canvas.draw_idle()

s_m.on_changed(update)
s_k.on_changed(update)
s_b.on_changed(update)
s_F.on_changed(update)

# ==================== 新增：相图（x-v 图）====================
fig2, ax2 = plt.subplots(figsize=(8, 6))
ax2.set_title('Phase Portrait (x - v)')
ax2.set_xlabel('Displacement x (m)')
ax2.set_ylabel('Velocity v (m/s)')
ax2.grid(True)

# 计算速度 v = dx/dt
v1 = -0.5 * np.sqrt(k0/m0) * np.sin(np.sqrt(k0/m0) * t)
v2 = np.gradient(x2 := 0.5 * np.exp(-b0*t/(2*m0)) * np.cos(np.sqrt((k0/m0) - (b0/(2*m0))**2) * t), t)  # 阻尼
v3 = np.gradient(x3 := (F0/m0) / np.sqrt(((k0/m0) - omega_d0**2)**2 + (b0*omega_d0/m0)**2) * np.cos(omega_d0 * t - np.pi/2), t)

ax2.plot(0.5 * np.cos(np.sqrt(k0/m0) * t), v1, label='Undamped', alpha=0.7)
ax2.plot(x2, v2, label='Damped', alpha=0.7)
ax2.plot(x3, v3, label='Forced', alpha=0.7)
ax2.legend()

plt.show()