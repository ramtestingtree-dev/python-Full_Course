given = 'automation'
count = 0
vowels = []

for char in given:
    if char.lower() in 'aeiou':
        count += 1                  # Count the Vowels
        vowels.append(char)         # Get the Vowels

print(count)
print(vowels)