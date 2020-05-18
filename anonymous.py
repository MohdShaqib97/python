print('\n\n############# *operator #############')
def all_total(num1,*args):
    print(num1)
    print(args)
    sum = 0
    for i in args:
        sum += i
    return sum

print(all_total(11,22,33,44))
print('\n\n#######list#######')
l = [2,3,4]
print(all_total(*l)) # *unpack

print('\n\n##############################################\n####################################')
def to_power(num, *args):
    if args:
        return [i**num for i in args]
    else:
        return 'list is empty'
    
nums = [1,2,3,4]
print(to_power(3,*nums))

print('\n\n######### **kwargs (keyword arguments) ###########')
def func(**kwargs):
    for k,v in kwargs.items():
        print(f'{k} : {v}')
    return kwargs
print(func(name = 'shaqib' , age = 22))

d = {'abc' : 1, 'bcd' : 'shaqib'}
print(func(**d))

print('\n\n#############lambda func#############')
add = lambda a,b : a+b
print(add(2,3))

print('\n\n#############lambda function with condition statements#############')
func = lambda s: True if len(s) < 5 else False
print(func('abc'))

print('\n\n#############Enumerate Function#############')
names = ['mohd','shaqib','saifi']
for pos, name in enumerate(names):
    print(f'{pos}-->{name}')

print('\n\n#############map function#############')
num = [1,2,3,4]
def square(a):
    return a**2

squares = list(map(square, num))
print(squares)

cubes = list(map(lambda a:a**3, num))
print(cubes)

print('\n\n#############filter function#############')
def is_even(a):
    return a%2==0
numbers = [i for i in range (1,11)]
evens = tuple(filter(is_even, numbers))
print(evens)

evens = tuple(filter(lambda a:a%2==0,[i for i in range(1,10)]))
print(evens)

print('\n\n#############zip function#############') #### zip
user_id = ['user1','user2','user3']
names = ['Mohd', 'Shaqib', 'Saifi']

example = list(zip(user_id,names))
print(example)
print(dict(example))

print('\n\n############# *operator with zip function#############')  #### unzip
l = [(1,2),(3,4),(5,6),(7,8)]
print(list(zip(*l)))   
l1, l2 = list(zip(*l))
print(f'{l1}\n{l2}')
