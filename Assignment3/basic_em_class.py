import numpy as np
import matplotlib.pyplot as plt

class basic_em_class:

    def __init__(self, filename):
        # Import the data to a numpy array
        self.array_data = np.genfromtxt(filename, delimiter=',')

        # Randomly generate some probabilities for iteration 1
        (self.rows, self.cols) = self.array_data.shape
        rand_matrix = np.ones((self.rows, 3)) / 3
        self.array_data = np.append(self.array_data, rand_matrix, axis=1)

        # Normalize the starting (random) data
        # self.normalize_array_data()

        ## Create necessary EM data
        # Mu represents average
        a = np.random.randint(0, self.rows)
        b = np.random.randint(0, self.rows)
        c = np.random.randint(0, self.rows)
        self.mu_1 = np.array([[self.array_data[a, 0]], [self.array_data[a, 1]]])
        self.mu_2 = np.array([[self.array_data[b, 0]], [self.array_data[b, 1]]])
        self.mu_3 = np.array([[self.array_data[c, 0]], [self.array_data[c, 1]]])

        # Sigma represents covariance
        self.sigma_1 = np.cov(np.transpose(self.array_data[:, [0, 1]])) / 8
        self.sigma_2 = self.sigma_1
        self.sigma_3 = self.sigma_1

        # Pi represents likelihood of each cluster
        self.pi_1 = 1/3
        self.pi_2 = 1/3
        self.pi_3 = 1/3


    def normalize_array_data(self):
        for i in range(0, self.rows):
            total = self.array_data[i, 2] + self.array_data[i, 3] + self.array_data[i, 4]
            self.array_data[i, 2] = self.array_data[i, 2] / total
            self.array_data[i, 3] = self.array_data[i, 3] / total
            self.array_data[i, 4] = self.array_data[i, 4] / total


    # Calculate the likelihood that ONE POINT belongs to the distribution given by mean, covar, and pi
    def calc_one_expectation(self, point, mean, covar, pi_c):
        # Solve for the probability using the gaussian distribution given by the mean and covariance
        # I am sorry for this part. Write it out by hand if it doesn't make sense.
        a = np.subtract(point, mean)
        b = np.transpose(a)
        c = np.linalg.inv(covar)
        d = np.dot(b, c)
        e = np.dot(d, a)
        exponent = (-1 / 2) * np.asscalar(e)
        fraction = (2 * np.pi) * np.sqrt(np.linalg.det(covar))
        answer = (pi_c / fraction) * np.exp(exponent)
        return answer


    # Calcluate the likelihood that EACH POINT belongs to EACH DISTRIBUTION and update the probabilities
    def calc_all_expectations(self):
        for i in range(0, self.rows):
            point = np.array([[self.array_data[i, 0]], [self.array_data[i, 1]]])
            self.array_data[i, 2] = self.calc_one_expectation(point, self.mu_1, self.sigma_1, self.pi_1)
            self.array_data[i, 3] = self.calc_one_expectation(point, self.mu_2, self.sigma_2, self.pi_2)
            self.array_data[i, 4] = self.calc_one_expectation(point, self.mu_3, self.sigma_3, self.pi_3)


    # Recalculate the parameters of each distribution given the set of points and current likelihood values
    def maximize_likelihoods(self):
        self.m_1 = np.sum(self.array_data[:, 2])
        self.m_2 = np.sum(self.array_data[:, 3])
        self.m_3 = np.sum(self.array_data[:, 4])
        m = self.m_1 + self.m_2 + self.m_3

        self.pi_1 = self.m_1 / m
        self.pi_2 = self.m_2 / m
        self.pi_3 = self.m_3 / m

        self.mu_1 = np.zeros((2, 1))
        self.mu_2 = np.zeros((2, 1))
        self.mu_3 = np.zeros((2, 1))

        self.sigma_1 = np.zeros((2, 2))
        self.sigma_2 = np.zeros((2, 2))
        self.sigma_3 = np.zeros((2, 2))

        for i in range(0, self.rows):
            point = np.array([[self.array_data[i, 0]], [self.array_data[i, 1]]])
            self.mu_1 = np.add(self.mu_1, (self.array_data[i, 2] / self.m_1) * point)
            self.mu_2 = np.add(self.mu_2, (self.array_data[i, 3] / self.m_2) * point)
            self.mu_3 = np.add(self.mu_3, (self.array_data[i, 4] / self.m_3) * point)


        for i in range(0, self.rows):
            point = np.array([[self.array_data[i, 0]], [self.array_data[i, 1]]])
            point1 = np.subtract(point, self.mu_1)
            point2 = np.subtract(point, self.mu_2)
            point3 = np.subtract(point, self.mu_3)

            self.sigma_1 = np.add(self.sigma_1, (self.array_data[i, 2] / self.m_1) * np.dot(point1, np.transpose(point1)))
            self.sigma_2 = np.add(self.sigma_2, (self.array_data[i, 3] / self.m_2) * np.dot(point2, np.transpose(point2)))
            self.sigma_3 = np.add(self.sigma_3, (self.array_data[i, 4] / self.m_3) * np.dot(point3, np.transpose(point3)))


    # Does ONE iteration of updating likelihoods and then maximizing
    def iterate_once(self):
        self.calc_all_expectations()
        ll = self.calc_log_likelihood()
        self.normalize_array_data()
        self.maximize_likelihoods()
        return ll


    def calc_log_likelihood(self):
        ll = np.sum(np.log(np.sum(self.array_data[:, [2,3,4]],1)))
        a = np.sum(np.log(self.array_data[:, 2]))
        b = np.sum(np.log(self.array_data[:, 3]))
        c = np.sum(np.log(self.array_data[:, 4]))
        log_likelihood = a + b + c
        # log1 = np.log(a)
        # log2 = np.log(b)
        # log3 = np.log(c)

        # log_likelihood = np.sum(np.log(a))
        return ll


    def run(self):
        # Does all iterations until log likelihood converges
        # last_log_likelihood = self.iterate_once()
        # log_likelihood = self.iterate_once()
        # while log_likelihood - last_log_likelihood > 0.001:
        #     last_log_likelihood = log_likelihood
        #     print(log_likelihood)
        #     log_likelihood = self.iterate_once()
        for i in range(0, 25):
            log_likelihood = self.iterate_once()
            print("Log likelihood: ", log_likelihood)

        self.plot_data()
        return (self.mu_1, self.mu_2, self.mu_3, self.sigma_1, self.sigma_2, self.sigma_3, log_likelihood)


    def plot_data(self):
        # Plot data for visualization purposes
        red_array = np.empty((1, 2))
        blue_array = np.empty((1, 2))
        green_array = np.empty((1, 2))

        for i in range(0, self.rows):
            if self.array_data[i, 2] > self.array_data[i, 3] and self.array_data[i, 2] > self.array_data[i, 4]:
                red_array = np.append(red_array, [[self.array_data[i, 0], self.array_data[i, 1]]], axis = 0)
            elif self.array_data[i, 3] > self.array_data[i, 2] and self.array_data[i, 3] > self.array_data[i, 4]:
                blue_array = np.append(blue_array, [[self.array_data[i, 0], self.array_data[i, 1]]], axis = 0)
            else:
                green_array = np.append(green_array, [[self.array_data[i, 0], self.array_data[i, 1]]], axis = 0)


        plt.scatter(red_array[:, 0], red_array[:, 1], c='red', s=7, edgecolors="none")
        plt.scatter(green_array[:, 0], green_array[:, 1], c='green', s=7, edgecolors="none")
        plt.scatter(blue_array[:, 0], blue_array[:, 1], c='blue', s=7, edgecolors="none")

        plt.show()

