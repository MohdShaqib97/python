import re
#pattern = re.compile("ab")
#matcher = pattern.finditer("abaaabab")
matcher = re.finditer("ab","abaaabab")
for match in matcher:
    print(match.start())


matcher = re.finditer("[abc]","a7b@k4z")
for match in matcher:
    print(match.start(),"...",match.group())

matcher = re.finditer("[^abc]","a7b@k4z")
for match in matcher:
    print(match.start(),"...",match.group())

matcher = re.finditer("[0-9]","a7b@k4z")
for match in matcher:
    print(match.start(),"...",match.group())

matcher = re.finditer("[a-zA-Z0-9]","a7b@k4z")
for match in matcher:
    print(match.start(),"...",match.group())

matcher = re.finditer("[^a-zA-Z0-9]","a7b@k4z")
for match in matcher:
    print(match.start(),"...",match.group())

matcher = re.finditer("[\s]","a7b @k4z")
for match in matcher:
    print(match.start(),"...",match.group())

matcher = re.finditer("[\S]","a7b @k4z")
for match in matcher:
    print(match.start(),"...",match.group())


matcher = re.finditer("[\d]","a7b @k4z")
for match in matcher:
    print(match.start(),"...",match.group())

matcher = re.finditer("[\D]","a7b @k4z")
for match in matcher:
    print(match.start(),"...",match.group())

matcher = re.finditer("[\w]","a7b @k4z")
for match in matcher:
    print(match.start(),"...",match.group())

matcher = re.finditer("[\W]","a7b @k4z")
for match in matcher:
    print(match.start(),"...",match.group())

matcher = re.finditer(".","a7b @k4z")
for match in matcher:
    print(match.start(),"...",match.group())


####### Quantifier ########
print("\n\n####### Quantifier ########")

matcher = re.finditer("a","abaaabab")
for match in matcher:
    print(match.start(),"...",match.group())

matcher = re.finditer("a+","abaaabab")
for match in matcher:
    print(match.start(),"...",match.group())


matcher = re.finditer("a*","abaaabab")
for match in matcher:
    print(match.start(),"...",match.group())

matcher = re.finditer("a?","abaaabab")
for match in matcher:
    print(match.start(),"...",match.group())

# a{n}----> exactly n number of a

matcher = re.finditer("a{3}","abaaabab")
for match in matcher:
    print(match.start(),"...",match.group())

# a{m,n}---> minimum m number if "a" and maximum n numebers of "a"

matcher = re.finditer("a{1,3}","abaaabaab")
for match in matcher:
    print(match.start(),"...",match.group())

matcher = re.finditer("a{5}a*","abaaabab")
for match in matcher:
    print(match.start(),"...",match.group())

matcher = re.finditer("[^a]","abaaabbab")
for match in matcher:
    print(match.start(),"...",match.group())

# a^ to check whether the given string starts with a
# a$ to check whether the given string ends with a

# function of re module:
#--------------------------
# 1. match()
# 2. fullmatch()
# 3. search()
# 4. findall()
# 5. sub()
# 6. subn()
# 7. finditer()
# 8. split()
# 9. compile()

####### sub():
#------------------------
# substitution and replacement
#re.sub(regex,replacement,targetString)

s = re.sub("\d","#","d2k3l6n2")
print(s)

# subn():-
#---------
# t = re.subn(regex,replacement,targetString)
#tuple
#(resultString,number of replacement)

t = re.subn("\d","###","d2k3l6n2")
print("result string",t[0])
print("number of replacement",t[1])

# split():-
#----------
l = re.split("-","10-20-30-40")
print(l)

#^(starts with) and $(Ends with) symbol:-
#----------------------------------------
s = "learning python is easy"
res = re.search("Easy$",s,re.IGNORECASE)
if res != None:
    print("target string ends with Easy")
else:
    print("target string not ends with Easy")


#############################################################
s = input("Enter indentifier to validate: ")
m = re.fullmatch("[a-k][0396][a-zA-Z0-9#]*",s)
if m != None:
    print(s,"is valid Yava indentifier")
else:
    print(s,"is not valid yava indentifier") 


########## 10 digit mobile number #########
s = input("enter mobile number to validate")
m = re.fullmatch("[6-9]\d{9}",s)
if m != None:
    print("it is valid mobile number")
else:
    print("it is invalid mobile number")