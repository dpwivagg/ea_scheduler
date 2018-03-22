import numpy as np
import matplotlib.pyplot as plt

# Normalizes the probability values in cols. 3-5 representing likelihoods of belonging to clusters 1-3
def normalize_array_data():
    (rows, cols) = array_data.shape
    for i in range(0, rows-1):
        total = array_data[i, 2] + array_data[i, 3] + array_data[i, 4]
        array_data[i, 2] = array_data[i, 2] / total
        array_data[i, 3] = array_data[i, 3] / total
        array_data[i, 4] = array_data[i, 4] / total



# Import the data to a numpy array
filename = 'sample_EM_data.csv'
array_data = np.genfromtxt(filename, delimiter=',')

# Randomly generate some probabilities for iteration 1
(rows, cols) = array_data.shape
rand_matrix = np.random.rand(rows, 3)
array_data = np.append(array_data, rand_matrix, axis=1)

# Normalize the data
normalize_array_data()

# Create necessary EM data (column 1 is means, column 2 is std. deviations)
em_vals = np.array([])

# Expectation step



# Maximization step



# Plot starting data for visualization purposes
plt.scatter(array_data[:, 0], array_data[:, 1])
plt.show()


