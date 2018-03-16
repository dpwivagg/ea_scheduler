# input like "gibbs price schools=good location=ugly -u 10000 -d 0"

def input_line():

    line = input()
    line_split = line.split(' ')
    evidence_node = {}

    for number in range(len(line_split)):

        if line_split[number] == 'gibbs':
            query_node = line_split[(number + 1)]

        if line_split[number] == '-u':
            update_number = line_split[(number + 1)]

        if line_split[number] == '-d':
            drop_number = line_split[(number + 1)]

    for i, s in enumerate(line_split):
        if '=' in s:
            s_split = s.split('=')
            input_state = str(s_split[1])
            if input_state in ['good', 'lots', 'small', 'old', 'cheap']:
                state = 0
            elif input_state in ['bad', 'little', 'medium', 'new', 'ok']:
                state = 1
            elif input_state in ['large', 'ugly', 'expensive']:
                state = 2
            evidence_node[s_split[0]] = state

    print('Query node:' + '\t' + str(query_node))
    print('Evidence nodes:' + '\t' + str(evidence_node))
    print('Update number:' + '\t' + str(update_number))
    print('Drop number:' + '\t' + str(drop_number))

    return query_node, evidence_node, int(update_number), int(drop_number)


