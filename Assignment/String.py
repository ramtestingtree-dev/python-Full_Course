n1 = "This is the new chapter"
print(n1)

print(n1.split(" "))

for i in n1.split():
    print(f"{i} = {n1.count(i)}")

# seen = set()
#
# for char in n1:
#
#     if n1.count(char) >= 1 and char not in seen:
#         print(f'{char} = {n1.count(char)}')
#         seen.add(char)
#
# print(sorted(seen))
# print(n1)
# print(len(n1))
#
