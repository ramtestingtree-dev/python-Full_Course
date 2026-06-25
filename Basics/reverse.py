str1 = 'ramkumar'

new = ''.join(reversed(str1))     # using reverse function
new2 = str1[::-1]                 # String Slicing
new3 = ''                         # Using for loop

for char in str1:
    new3 = char + new3

print(new)
print(new2)
print(new3)