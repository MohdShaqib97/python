num = [1,2,3,4,"hello","python",1.2,None]
print(num)

fruits1 = ["mango","grapes"]
fruits2 = ["mango","grapes"]
fruits = fruits1 + fruits2
print(fruits)
fruits.insert(1,"banana")
print(fruits)

fruits1.extend(fruits2)
print(fruits1)

fruits1.append(fruits2)
print(fruits1)

############pop method########
print("\n\n##########pop method########")
fruits = ["apple", "banana", "orange", "kiwi"]
fruits.pop()
print(fruits)

fruits.pop(1)
print(fruits)

######### del method#########
print("\n\n##########del method########")
fruits = ["apple", "banana", "orange", "kiwi"]

del fruits[2]
print(fruits)

###########remove method###########
print("\n\n##########remove method########")
fruits = ["apple", "banana", "orange", "kiwi"]
fruits.remove("banana")
print(fruits)

fruits = ["apple", "banana","apple", "orange", "kiwi"]
print(fruits.count("apple"))
fruits.remove("apple")
print(fruits)

fruits = ["apple", "banana","apple", "orange", "kiwi"]

while True:
    if 'apple' in fruits:
        fruits.remove('apple')
    else:
        break
print(fruits)

#count
#sort
#sorted function 
#reverse 
#clear
#copy
print('#####count_Sort_SortedFunction_Reverse_Clear_Copy#######')

fruits = ["apple", "banana","apple", "orange", "kiwi","mango"]
print(fruits.count("apple"))
fruits.sort()
print(fruits)
animal = fruits.copy()
print(animal)
fruits.reverse()
print(fruits)
fruits.clear()
print(fruits)

###########split() and join() method###########
print('\n\n\n\n###########split() and join() method##########')
name = 'mohd shaqib'
print(name.split())
print(name)

list = ['shaqib',' 22']
print(''.join(list))

