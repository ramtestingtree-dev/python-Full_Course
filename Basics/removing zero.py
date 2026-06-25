t = 120300200100
t1 = list(str(t))
remove_zero = []
clean =[]

for char in t1:
    if char == '0':
        remove_zero.append(char)
    else:
        clean.append(char)

result = ''.join(remove_zero)
result2= ''.join(clean)

final = result2 + result

print(final)










