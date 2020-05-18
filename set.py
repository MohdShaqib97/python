#set data type
#unordered collection of unique items

s = {1,2,3}
print(list(s)[0])

l = [1,2,3,3,3,3,3,4,4,4,4,5,5,5,6,7,8,9]
s2 = set(l)
print(s2)

############add and remove or discard method function###############
s = {1,2,3}
s.add(4)
s.add(5)
print(s)

s.remove(3)
print(s)

s.discard(3)
print(s)

#######copy and clear method######
s1 = s.copy()
s.clear()
print(s)
print(s1)

#we cannot store list and dictionary in our set

########union and intersection in set#########
s1 = {1,2,3,4,5}
s2 = {4,5,6,7,8}

union_set = s1|s2
print(union_set)

interection_set = s1 & s2
print(interection_set)