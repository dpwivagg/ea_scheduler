# test input: em sample_EM_data_v2.csv 3
from Assignment3.em_with_n_cluster import basic_em_class
from Assignment3.input import input_line
import matplotlib.pyplot as plt
import numpy as np

input = input_line()
bic_list = []

if input[1] == "X":
    clusterNum_list = range(1, 20)
    pBIC = 0.00
    BIC = 0.00
    i = 1
    # for i in clusterNum_list:
    while pBIC ==0 or (pBIC-BIC) > 0:
        pBIC = BIC
        a = basic_em_class(input[0], i)
        output = a.run()
        print("BIC value is: " + str(output))
        bic_list = np.append(bic_list, output)
        BIC = output
        i = i + 1
        print("\n")
    number = int(bic_list.argmin()) + 1
    print("Best cluster number: " + str(number))
    a = basic_em_class(input[0], number)
    mBIC = a.run()
    print("BIC Value is "+ str(mBIC))
    print("")
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
