# input like "gibbs price schools=good location=ugly -u 10000 -d 0"

def input_line():

    line = input()
    line_split = line.split(' ')
    evidence_node = {}
    #print (line_split)

    for number in range(len(line_split)):

        if line_split[number] == 'gibbs':
            query_node = line_split[(number + 1)]
            #print(query_node)

        if line_split[number] == '-u':
            update_number = line_split[(number + 1)]
            #print(update_number)

        if line_split[number] == '-d':
            drop_number = line_split[(number + 1)]
            #print(drop_number)

    for i, s in enumerate(line_split):
        if '=' in s:
            s_split = s.split('=')
            evidence_node[s_split[0]]=s_split[1]

    #print(evidence_node)

    return query_node, evidence_node, update_number, drop_number

input_line()