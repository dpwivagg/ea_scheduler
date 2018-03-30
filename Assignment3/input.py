# input line should be like "em sample_EM_data_v2.csv 3"

def input_line():

    line = input()
    line_split = line.split(" ")
    file_name = str
    cluster_number = str or int

    for i in range(len(line_split)):
        if i == 1:
            file_name = line_split[1]
        if i == 2:
            cluster_number = line_split[2]

    return file_name, cluster_number
