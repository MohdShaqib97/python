user = {'name' : 'shaqib', 'age' : 22}
print(user)

user1 = dict(name = 'shaqib', age = 22)
print(user1)
print(user1['name'])

user2 = {}
user2['name'] = 'shaqib'
user2['age'] = 22
print(user2)

####check if key and values present in dictionary####
#{'name': 'shaqib', 'age': 22}
if 'name' in user2:
    print("present")
else:
    print('not present')

if 'shaqib' in user2.values():
    print('present')
else:
    print('not present')

#######update method#######
print("\n\n\n#######update method########")
user = {'name' : 'shaqib', 'age' : 22}
update_info = {'hobbies' : 'gym',}
user.update(update_info)
print(user)

#fromkeys
print('\n\n####from keys method####')
d = dict.fromkeys(['name','age','height'],'unknown')
print(d)

d = dict.fromkeys("abc",'unknown')
print(d)

d = dict.fromkeys(range(1,11),'unknown')
print(d)

d = dict.fromkeys(['name','age'],['unknown','unknown'])
print(d)

#get method
print('\n\n#######get method#######')
d = {'name': 'shaqib', 'age': '22', 'height': '73cm'}
print(d.get('name'))
print(d.get('names'))

if d.get('name'):
    print('present')
else:
    print('not present')

print(d.get('names','not found !'))