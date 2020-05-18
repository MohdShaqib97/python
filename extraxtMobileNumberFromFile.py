import re
#### read mobile number form file ##########
f1 = open("input.txt","r")
f2 = open("output.txt","w")

for l in f1:
    list = re.findall("[6-9]\d{9}",l)
    for numbers in list:
        f2.write(numbers+"\n")
f1.close()
f2.close()