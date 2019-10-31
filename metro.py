import os
import numpy as np
import matplotlib.pyplot as plt

plt.figure()
n_points = 10000
sigma = 1.0

x = main()

x_model = np.linspace(x.min(), x.max(), n_points)
y_model = exp(-x_model**2/(2.0*sigma**2))

_ = plt.hist(x, bins=30, density=True, label='Metropolis-Hastings')
plt.plot(x_model, y_model, label='Modelo')

plt.legend()
plt.xlabel("X")
plt.ylabel("Y")
plt.savefig("metro.png")