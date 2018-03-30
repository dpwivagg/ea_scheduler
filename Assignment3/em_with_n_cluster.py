import numpy as np
import matplotlib.pyplot as plt

class basic_em_class:

    def __init__(self, filename, num):
        self.num = num
        self.log_likelihood = 0.00
        # Import the data to a numpy array
        self.array_data2 = np.genfromtxt(filename, delimiter=',')
        # Randomly generate some probabilities for iteration 1
        (self.rows, self.cols) = self.array_data2.shape
        rand_matrix = np.ones((self.rows, self.num)) / self.num
        self.array_data2 = np.append(self.array_data2, rand_matrix, axis=1)
        self.normalize_array_data()
        for i in range(self.num):
            a = np.random.randint(1, self.rows)
            mu = np.array([[self.array_data2[a, 0]], [self.array_data2[a, 1]]])
            if i == 0:
                self.muArray = mu
            else:
                self.muArray = np.append(self.muArray, mu, axis=1)
        for i in range(self.num):
            sigma = np.cov(np.transpose(self.array_data2[:, [0, 1]])) / 8
            sigma = np.reshape(sigma,(1,4))

            if i == 0:
                self.sigmaArray = sigma
            else:
                self.sigmaArray = np.append(self.sigmaArray, sigma, axis=1)
        self.sigmaArray = np.reshape(self.sigmaArray,(self.num,2,2))
        self.piArray = np.array([1/self.num]*self.num)

    def normalize_array_data(self):
        # print("Once")
        for i in range(0, self.rows):
            total = 0
            for j in range(self.num):
                total = total + self.array_data2[i, 2 + j]
            for j in range(self.num):
                self.array_data2[i, 2 + j] = self.array_data2[i, 2 + j] / total

    def calc_one_expectation(self, point, mean, covar, pi_c):
        m = np.reshape(mean, (2,1))
        a = np.subtract(point, m)
        b = np.transpose(a)
        c = np.linalg.inv(covar)
        d = np.dot(b, c)
        e = np.dot(d, a)
        exponent = (-1 / 2) * np.asscalar(e)
        fraction = (2 * np.pi) * np.sqrt(np.linalg.det(covar))
        answer = (pi_c / fraction) * np.exp(exponent)
        return answer

    def calc_all_expectations(self):
        for i in range(0, self.rows):
            point1 = np.array([[self.array_data2[i, 0]], [self.array_data2[i, 1]]])
            for j in range(self.num):
                self.array_data2[i, 2 + j] = self.calc_one_expectation(point1, self.muArray[:, j], self.sigmaArray[j],
                                                                       self.piArray[j])

    def maximize_likelihoods(self):
        mz = 0
        m_Array = np.array([np.sum(self.array_data2[:, 2])])

        for i in range(1,self.num):
            m_Array = np.append(m_Array, np.sum(self.array_data2[:, 2 + i]))
        for i in range(self.num):
            mz = mz + m_Array[i]

        for i in range(self.num):
            self.piArray[i] = m_Array[i] / mz

        for i in range(self.num):
            self.muArray[:, i] = np.zeros(2)
            self.sigmaArray[i] = np.zeros((2, 2))

        for i in range(self.rows):
            pointz = np.array([[self.array_data2[i, 0]], [self.array_data2[i, 1]]])
            for j in range(self.num):
                b = (self.array_data2[i, 2 + j] / m_Array[j])
                c = b * pointz
                a = np.add(np.reshape(self.muArray[:, j], (2, 1)), c)
                self.muArray[:, j] = np.reshape(a, (2,))

        for i in range(self.rows):
            point = np.array([[self.array_data2[i, 0]], [self.array_data2[i, 1]]])
            for j in range(self.num):
                pointz = np.subtract(point, np.reshape(self.muArray[:, j], (2, 1)))
                self.sigmaArray[j] = np.add(self.sigmaArray[j],
                                            (self.array_data2[i, 2 + j] / m_Array[j]) * np.dot(pointz,
                                                                                               np.transpose(pointz)))

    def iterate_once(self):
        self.calc_all_expectations()
        ll = self.calc_log_likelihood()
        self.normalize_array_data()
        self.maximize_likelihoods()
        return ll

    def calc_log_likelihood(self):
        ll = np.sum(np.log(np.sum(self.array_data2[:, 2:],1)))
        # log_likelihood = 0
        # for i in range(self.num):
        #     log_likelihood = log_likelihood + np.sum(np.log(self.array_data2[:, 2+i]))
        return ll

    def run(self):
        # Does all iterations until log likelihood converges
        while abs(self.iterate_once()-float(self.log_likelihood)) > 0.05:
            self.log_likelihood=self.iterate_once()

        for i in range(self.num):
            print("Mean of cluster "+str(i+1)+": ",self.muArray[:,i])
            print("Variance of cluster "+str(i+1)+": \n",self.sigmaArray[i])
        print("Log likelihood: ", self.log_likelihood)

        bic_value = self.compute_bic()
        # print("BIC value: " + str(bic_value))
        # self.plot_data()
        return bic_value

    def plot_data(self):
        # Plot data for visualization purposes
        cluster={}
        colorlist = ["red", "green",'blue',"yellow", "black"]
        for i in range(0, self.num):
            cluster[i]=np.empty((1,2))

        for i in range(0, self.rows-1):
            x = list()
            for n in range(0, self.num):
                x=np.append(x, self.array_data2[i,n+2])
                # print(x)
            j=int(x.argmax())
            # print(j)
            cluster[j]=np.append(cluster[j],[[self.array_data2[i, 0], self.array_data2[i, 1]]], axis = 0)

        for i in range(0,self.num):
            plt.scatter(cluster[i][:,0],cluster[i][:,1],c=colorlist[i],s=7,edgecolors="none")

        plt.show()

    def compute_bic(self):
        D = 2
        bic_value = (-2) * self.log_likelihood + ((self.num-1) + self.num * (D + 1/2 * D * (D + 1))) * (np.log(self.rows))
        return bic_value

