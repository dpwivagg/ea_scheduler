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


def calc_expectation(point, mean, covar, pi_c):
    # Solve for the probability using the gaussian distribution given by the mean and covariance
    a = np.subtract(point, mean)
    b = np.transpose(a)
    c = np.linalg.pinv(covar)
    d = np.dot(b, c)
    e = np.dot(d, a)
    exponent = (-1/2)*np.asscalar(e)
    fraction = (2*np.pi)*np.sqrt(np.linalg.det(covar))
    answer = (pi_c/fraction)*np.exp(exponent)
    return answer


## Initialization steps
# Import the data to a numpy array
filename = 'sample_EM_data.csv'
array_data = np.genfromtxt(filename, delimiter=',')

# Randomly generate some probabilities for iteration 1
(rows, cols) = array_data.shape
rand_matrix = np.random.rand(rows, 3)
array_data = np.append(array_data, rand_matrix, axis=1)

# Normalize the data
normalize_array_data()

# Create necessary EM data
mu_1 = np.array([[np.mean(array_data[:, 0])], [np.mean(array_data[:, 1])]])
sigma_1 = np.cov(np.transpose(array_data[:, [0, 1]]))
pi_1 = np.random.random()
mu_2 = mu_1
sigma_2 = sigma_1
pi_2 = np.random.random()
mu_3 = mu_1
sigma_3 = sigma_1
pi_3 = np.random.random()

## Stuff that needs to be done a bunch

# Expectation step

for i in range(0, rows-1):
    point = np.array([[array_data[i, 0]],[array_data[i, 1]]])
    array_data[i, 2] = calc_expectation(point, mu_1, sigma_1, pi_1)
    array_data[i, 3] = calc_expectation(point, mu_2, sigma_2, pi_2)
    array_data[i, 4] = calc_expectation(point, mu_3, sigma_3, pi_3)

normalize_array_data()

# Maximization step

m_1 = np.sum(array_data[:,2])
m_2 = np.sum(array_data[:,3])
m_3 = np.sum(array_data[:,4])
m = m_1 + m_2 + m_3

pi_1 = m_1/m
pi_2 = m_2/m
pi_3 = m_3/m

mu_1 = np.zeros((2,1))
mu_2 = np.zeros((2,1))
mu_3 = np.zeros((2,1))
sigma_1 = np.zeros((2,2))
sigma_2 = np.zeros((2,2))
sigma_3 = np.zeros((2,2))

for i in range(0, rows-1):
    point1 = np.array([[array_data[i, 0]],[array_data[i, 1]]])
    point2 = np.array([[array_data[i, 0]],[array_data[i, 1]]])
    point3 = np.array([[array_data[i, 0]],[array_data[i, 1]]])
    mu_1 = np.add(mu_1, (array_data[i, 2]/m_1)*point1)
    mu_2 = np.add(mu_2, (array_data[i, 3]/m_2)*point2)
    mu_3 = np.add(mu_3, (array_data[i, 4]/m_3)*point3)

    sigma_1 = np.add(sigma_1, (array_data[i, 2] / m_1) * np.transpose(point1 - mu_1) * (point1 - mu_1))
    sigma_2 = np.add(sigma_2, (array_data[i, 3] / m_2) * np.transpose(point2 - mu_2) * (point2 - mu_2))
    sigma_3 = np.add(sigma_3, (array_data[i, 4] / m_3) * np.transpose(point3 - mu_3) * (point3 - mu_3))

# Plot starting data for visualization purposes
plt.scatter(array_data[:, 0], array_data[:, 1])
plt.scatter(mu_1[0], mu_1[1])
plt.show()


