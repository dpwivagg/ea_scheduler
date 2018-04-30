dic = { "presenter": [], "lead":[2,8,9],"no_role":[1,2,3] }
print(dic)
a = []
# a.append(dic.values())
for key in dic.keys():
    a.append(dic[key])
print(a)
h = 0
for key in dic.keys():
    if key != 'no_role':
        if len(dic[key]) < 1:
            h -= 5
            break
print (h)