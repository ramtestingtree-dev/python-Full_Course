from collections import Counter

paragraph = "This is the python, C++, java is the most comfortable language in order on python, it is the best and C++ is the most used and java is the most.....it is very good for python and it not good on C++ by its way is very good in the python and java and it is C++"

words = paragraph.replace(",", "").replace(".", "").split()

counts = Counter(words)
print(counts)

for lang in ("python", "C++", "java"):
    print(f"{lang} = {counts[lang]}")

print(f"{' '.join(word[::-1] for word in words)}")