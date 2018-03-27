# test input: em sample_EM_data_v2.csv 3
from basic_em_class import basic_em_class
from input import input_line

a = basic_em_class(input_line()[0])
vars = a.run()

print("First distribution: \n")
print("Mean: ", vars[0], "\nVariance: ", vars[3])
print("\nSecond distribution: \n")
print("Mean: ", vars[1], "\nVariance: ", vars[4])
print("\nThird distribution: \n")
print("Mean: ", vars[2], "\nVariance: ", vars[5])
print("\nLog likelihood: ", vars[6])