import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

# 参数初始值
m0 = 1.0
k0 = 4.0
b0 = 0.5
F0 = 0.5
omega_d0 = 2.0

# 时间
t = np.linspace(0, 20, 2000)

fig, ax = plt.subplots(figsize=(10, 6))
plt.subplots_adjust(bottom=0.35)

# 初始曲线
l1, = ax.plot(t, 0.5 * np.cos(np.sqrt(k0/m0) * t), label='无阻尼', alpha=0.7)
l2, = ax.plot(t, 0.5 * np.exp(-b0*t/(2*m0)) * np.cos(np.sqrt((k0/m0) - (b0/(2*m0))**2) * t), label='阻尼振子', alpha=0.7)
l3, = ax.plot(t, (F0/m0) / np.sqrt(((k0/m0) - omega_d0**2)**2 + (b0*omega_d0/m0)**2) * np.cos(omega_d0 * t - np.pi/2), label='受迫振动', alpha=0.7)

ax.set_xlabel('时间 (s)')
ax.set_ylabel('位移 (m)')
ax.set_title('力学振子交互仿真（拖动滑块实时调节）')
ax.grid(True)
ax.legend()

# 滑块位置
ax_m = plt.axes([0.15, 0.15, 0.65, 0.03])
ax_k = plt.axes([0.15, 0.10, 0.65, 0.03])
ax_b = plt.axes([0.15, 0.05, 0.65, 0.03])
ax_F = plt.axes([0.15, 0.00, 0.65, 0.03])

s_m = Slider(ax_m, '质量 m', 0.1, 5.0, valinit=m0)
s_k = Slider(ax_k, '劲度系数 k', 1.0, 20.0, valinit=k0)
s_b = Slider(ax_b, '阻尼系数 b', 0.0, 2.0, valinit=b0)
s_F = Slider(ax_F, '驱动力 F', 0.0, 5.0, valinit=F0)

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

plt.show()