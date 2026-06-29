t1 = 'seleniummm'

duplicate = []
clean = []

for char in t1:
    if t1.count(char) >= 1 and char not in clean:
        clean.append(char)
    else:
        duplicate.append(char)
        # duplicate[char] = duplicate.get(char, 0) + 1

print(clean, duplicate)

#
# print(f'clean = {clean}, \n {duplicate}')
# for key, value in duplicate.items():
#     print(key, value)

