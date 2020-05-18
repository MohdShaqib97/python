import re

s = input("Enter valid mail ID:")
m = re.fullmatch("\w[a-zA-Z0-9_.]*@gmail[.]com",s)
if m != None:
    print("it is valid mail ID")
else:
    print("it is invalid mail ID")