name = ['abc','csd','fdd','shaqib']
for i in range (0,len(name)):
    print(i+1,'-->',name[i])

######### Enumerate function ######
print("#### Enumerate function ####")
for n, name in enumerate(name):
    print(f"{n}--->{name}")

name = ['abc','csd','fdd','shaqib']

def find_Pos(l,target):
    for n, name in enumerate(l):
        if name == target:
            return n
    return 'not found'

print(find_Pos(name,'shaqib'))


######## Map Function() #######
print("######## Map Function() #######")

numbers = [1,2,3,4]

def square(a):
    return a**2

print(list(map(square,numbers)))

print(list(map(lambda a:a**2,numbers)))

###### filter function ######
print("###### filter function ######")

number = [i for i in range(1,11)]
print(number)

def even(a):
    return a%2==0

print(list(filter(even,number)))
print(list(filter(lambda a:a%2==0,number)))

######## Zip function() ########
print("######## Zip function() ########")

user = ["user1","user2","user3"]
name = ["Mohd","shaqib","saifi"]
print(dict(zip(user,name)))

avg_finder = lambda *args:[sum(pair)/len(pair) for pair in zip(*args)]
print(avg_finder([1,2,3],[4,5,6]))

##### any, all function() #####
print("##### any, all function() #####")
print(all([num for num in range(1,11) if num%2==0]))

l = [1,2,3,4,5]
print(any([i%2==0 for i in l]))

def my_sum(*args):
    if all([(type(arg) == int or type(arg) == float) for arg in args]):
        total = 0
        for num in args:
            total += num
        return total
    else:
        return "invalid input"

print(my_sum(1.2,3,4))
print(my_sum(1,2,3,"abc"))


########## Advance min() max() function#########
print("########## Advance min() max() function#########")

names = ["shaqib","jerry","Mohd"]
print(max(names,key = lambda item:len(item)))

students = [ 
    {"name":"Shaqib","score":20,"age":23},
    {"name":"JERRY","score":23,"age":20},
    {"name":"MOhd","score":25,"age":24}
]

print(max(students, key = lambda item:item.get("score")))

student2 = {
    "shaqib" : {"score":90, "age":24},
    "jerry" : {"score":98, "age":21},
    "Mohd" : {"score":89, "age":19}
}

print(max(student2, key = lambda item: student2[item]["score"]))

######## Advance Sorted fun() ###########
print("######## Advance Sorted fun() ###########")

fruits = ("grapes","mango","apple")
print(sorted(fruits))
fruit = list(fruits)
print(sorted(fruit))

guitars = [
    {"modal": "yamaha f310", "price":8400},
    {"modal": "faith naptune", "price":50000},
    {"modal": "faith apollo venus", "price":35000},
    {"modal": "taylor 814ce", "price":450000},
]
print(sorted(guitars, key = lambda item: item["price"]))
print(sorted(guitars, key = lambda item: item["price"], reverse = True))