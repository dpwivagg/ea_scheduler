def set_evidence_node():

    evidence_number = int(input("How many evidence node do you want?\n"))
    nodes = []
    evidence_list = {}
    count=0

    while count < evidence_number:
        print("For the " + str(count+1) + " evidence node, please choose one evidence node from 0 to 7:")
        node = "0. amenities \n" \
               "1. neighborhood \n" \
               "2. location \n" \
               "3. children \n" \
               "4. size \n" \
               "5. school \n" \
               "6. age \n" \
               "7. price \n"

        while True:
            try:
                evidence = int(input(node + "\nSet evidence node: \n"))
                if evidence not in range(8):
                    print('Invalid value entered. Please enter again. \n')
                    continue
                if evidence == h[0]:
                    print('This is your Query Node! please enter again. \n')
                    continue
                if evidence in nodes:
                    print('You have selected this node. Please enter again. \n')
                    continue
                count +=1
                break
            except ValueError:
                print('Invalid value entered. Please enter again.')

        dict = {"amenities":["lots", "little"],
                "neighborhood":["good", "bad"],
                "location":["good", "bad", "ugly"],
                "children":["good", "bad"],
                "size":["small", "medium", "large"],
                "school":["good", "bad"],
                "age":["old", "new"],
                "price":["cheap", "ok", "expensive"]}

        print("\nPlease select evidence status:")

        if evidence == 0:
            node_1 = "0. lots \n" \
                     "1. little \n"
            while True:
                try:
                    amenities_n = int(input(node_1 + "\nSelect status: \n"))
                    if amenities_n not in range(2):
                        print('Invalid value entered. Please enter again. \n')
                        continue
                    break
                except ValueError:
                    print('Invalid value entered. Please enter again.')
            nodes.append(0)
            evidence_list["amenities"] = dict["amenities"][amenities_n]

        if evidence == 1:
            node_2 = "0. good \n" \
                     "1. bad \n"
            while True:
                try:
                    neighborhood_n = int(input(node_2 + "\nSelect status: \n"))
                    if neighborhood_n not in range(2):
                        print('Invalid value entered. Please enter again. \n')
                        continue
                    break
                except ValueError:
                    print('Invalid value entered. Please enter again.')
            nodes.append(1)
            evidence_list["neighborhood"] = dict["neighborhood"][neighborhood_n]

        if evidence == 2:
            node_3 = "0. good \n" \
                     "1. bad \n" \
                     "2. ugly \n"
            while True:
                try:
                    location_n = int(input(node_3 + "\nSelect status: \n"))
                    if location_n not in range(3):
                        print('Invalid value entered. Please enter again. \n')
                        continue
                    break
                except ValueError:
                    print('Invalid value entered. Please enter again.')
            nodes.append(2)
            evidence_list["location"] = dict["location"][location_n]

        if evidence == 3:
            node_4 = "0. good \n" \
                     "1. bad \n"
            while True:
                try:
                    children_n = int(input(node_4 + "\nSelect status: \n"))
                    if children_n not in range(2):
                        print('Invalid value entered. Please enter again. \n')
                        continue
                    break
                except ValueError:
                    print('Invalid value entered. Please enter again.')
            nodes.append(3)
            evidence_list["children"] = dict["children"][children_n]

        if evidence == 4:
            node_5 = "0. small \n" \
                     "1. medium \n" \
                     "2. large \n"
            while True:
                try:
                    size_n = int(input(node_5 + "\nSelect status: \n"))
                    if size_n not in range(3):
                        print('Invalid value entered. Please enter again. \n')
                        continue
                    break
                except ValueError:
                    print('Invalid value entered. Please enter again.')
            nodes.append(4)
            evidence_list["size"] = dict["size"][size_n]

        if evidence == 5:
            node_6 = "0. good \n" \
                     "1. bad \n"
            while True:
                try:
                    school_n = int(input(node_6 + "\nSelect status: \n"))
                    if school_n not in range(2):
                        print('Invalid value entered. Please enter again. \n')
                        continue
                    break
                except ValueError:
                    print('Invalid value entered. Please enter again.')
            nodes.append(5)
            evidence_list["school"] = dict["school"][school_n]

        if evidence == 6:
            node_7 = "0. old \n" \
                     "1. new \n"
            while True:
                try:
                    age_n = int(input(node_7 + "\nSelect status: \n"))
                    if age_n not in range(2):
                        print('Invalid value entered. Please enter again. \n')
                        continue
                    break
                except ValueError:
                    print('Invalid value entered. Please enter again.')
            nodes.append(6)
            evidence_list["age"] = dict["age"][age_n]

        if evidence == 7:
            node_8 = "0. cheap \n" \
                     "1. ok \n" \
                     "2. expensive \n"
            while True:
                try:
                    price_n = int(input(node_8 + "\nSelect status: \n"))
                    if price_n not in range(3):
                        print('Invalid value entered. Please enter again. \n')
                        continue
                    break
                except ValueError:
                    print('Invalid value entered. Please enter again.')
            nodes.append(7)
            evidence_list["price"] = dict["price"][price_n]

    print("\nEvidence nodes have been selected:\n" + str(evidence_list) + "\n")
    return nodes, evidence_list



def get_query_node():
    node = "0. amenities \n" \
           "1. neighborhood \n" \
           "2. location \n" \
           "3. children \n" \
           "4. size \n" \
           "5. school \n" \
           "6. age \n" \
           "7. price \n"
    all_nodes = ["amenities", "neighborhood", "location", "children", "size", "school", "age", "price"]
    while True:
        try:
            query_n = int(input(node + "\nSelect query node: \n"))
            if query_n not in range(8):
                print('Invalid input! Please select again. \n')
                continue
            break
        except ValueError:
            print('Invalid value entered. Please enter again.')
    query_node = all_nodes[query_n]
    print("The query node is:" + query_node + '\n')
    return query_n, query_node

h = get_query_node()

set_evidence_node()