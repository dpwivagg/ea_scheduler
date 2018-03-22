import numpy as np
import matplotlib.pyplot as plt

filename = 'sample_EM_data.csv'
array_data = np.genfromtxt(filename, delimiter=',')

plt.scatter(array_data[:,0], array_data[:,1])
plt.show()