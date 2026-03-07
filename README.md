import numpy as np
import matplotlib.pyplot as plt

m = 1.0
k = 4.0
omega = np.sqrt(k / m)

t = np.linspace(0, 10, 1000)
x = 0.5 * np.cos(omega * t)

plt.plot(t, x)
plt.title('简谐振子位移-时间图像')
plt.xlabel('时间 (s)')
plt.ylabel('位移 (m)')
plt.grid(True)
plt.show()