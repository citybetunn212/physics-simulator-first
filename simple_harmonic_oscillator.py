import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

# 参数（可调节）
m = 1.0
k = 4.0
b = 0.5      # 阻尼系数（新增）
F = 0.5      # 驱动力幅度（新增）
omega_d = 2.0  # 驱动力频率

omega0 = np.sqrt(k / m)
t = np.linspace(0, 20, 2000)

# 无阻尼
x1 = 0.5 * np.cos(omega0 * t)
# 阻尼
x2 = 0.5 * np.exp(-b*t/(2*m)) * np.cos(np.sqrt(omega0**2 - (b/(2*m))**2) * t)
# 受迫（稳态）
x3 = (F / m) / np.sqrt((omega0**2 - omega_d**2)**2 + (b*omega_d/m)**2) * np.cos(omega_d * t - np.pi/2)

plt.figure(figsize=(10, 6))
plt.plot(t, x1, label='无阻尼', alpha=0.7)
plt.plot(t, x2, label='阻尼振子', alpha=0.7)
plt.plot(t, x3, label='受迫振动（稳态）', alpha=0.7)
plt.title('简谐振子三种情况对比')
plt.xlabel('时间 (s)')
plt.ylabel('位移 (m)')
plt.grid(True)
plt.legend()
plt.show()