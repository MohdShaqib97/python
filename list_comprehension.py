square = [i**2 for i in range(1,11)]
print(square)
########reverse in ls######
l = ['abc', 'xyz','pqr']
rev = [i[::-1] for i in l]
print(rev)
######## condition in ls#######
even_nums = [i for i in range(1,11) if i%2==0]
print(even_nums)

new_list = ['even' if i%2==0 else 'odd' for i in range(1,11)]
print(new_list)
#########num to string in ls#########
nums = [True, False, [1,2,3], 1, 2, 2.3]
num_to_string = [i for i in nums if type(i) == int or type(i) == float]
print(num_to_string)

#######nested list in ls########
nested_list = [[i for i in range(1,4)] for j in range (1,4)]
print(nested_list)
