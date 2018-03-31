This is the README file for CS534 Assignment

How to run this program:
    To run this program you should run the file test
    Then it will ask for your input.
    Your input should follow the format of  em data_file_name number_of_clusters

Files in this project:
    basic_em_class.py: The first working file for expectation maximization which runs for fixed of three clusters analysis
    em_with_n_cluster.py: The real running em for n number of clusters
    input.py: Analysis the input string and return the required arguments
    test.py: The simulation
    README.txt: Contains information before people run this project


Here is an example of input:
    em sample_EM_data_v2.csv 3
    This will use the data in the sample_EM_data_v2.csv as the data file and separates the data into three clusters.

    When you input 'X' as the cluster number, our program will try different cluster numbers for this data set.
    It stops when BIC value stops decreasing.

The random data set for question 5 in the write up is called new_data.csv
