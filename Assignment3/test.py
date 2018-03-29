# test input: em sample_EM_data_v2.csv 3
from Assignment3.em_with_n_cluster import basic_em_class
from Assignment3.input import input_line

a = basic_em_class('sample_EM_data_v2.csv')
vars = a.run()

# print("First distribution: \n")
# print("Mean: ", vars[0], "\nVariance: ", vars[3])
# print("\nSecond distribution: \n")
# print("Mean: ", vars[1], "\nVariance: ", vars[4])
# print("\nThird distribution: \n")
# print("Mean: ", vars[2], "\nVariance: ", vars[5])
# print("\nLog likelihood: ", vars[6])