# test input: em sample_EM_data_v2.csv 3
from Assignment3.em_with_n_cluster import basic_em_class
from Assignment3.input import input_line
import matplotlib.pyplot as plt
import numpy as np
import types

input = input_line()
bic_list = []

if input[1] == "X":
    clusterNum_list = range(1, 20)
    for i in clusterNum_list:
        a = basic_em_class(input[0], i)
        vars = a.run()
        bic_list = np.append(bic_list, vars)

    number = int(bic_list.argmax()) + 2
    print("Best cluster number: " + str(number))

    plt.plot(clusterNum_list, bic_list)
    plt.xticks(np.arange(min(clusterNum_list), max(clusterNum_list) + 1, 1.0))
    plt.ylabel("BIC Value")
    plt.show()
else:
    a = basic_em_class(input[0], int(input[1]))
    a.run()

# print("First distribution: \n")
# print("Mean: ", vars[0], "\nVariance: ", vars[3])
# print("\nSecond distribution: \n")
# print("Mean: ", vars[1], "\nVariance: ", vars[4])
# print("\nThird distribution: \n")
# print("Mean: ", vars[2], "\nVariance: ", vars[5])
# print("\nLog likelihood: ", vars[6])