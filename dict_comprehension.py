square = {num:num**2 for num in range(1,11)}
print(square)

string = 'Mohd shaqib'
word_count = {char:string.count(char) for char in string}
print(word_count)

odd_even = {i:'even' if i%2==0 else 'odd' for i in range(1,11)}
print(odd_even)

#####set comprehension########
s = {i**2 for i in range(1,11)}
print(s)