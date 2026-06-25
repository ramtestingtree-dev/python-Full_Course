# Demonstrating List, Set, Dictionary, and Tuple in Python with Exception Handling

# 1. List - Ordered, allows duplicates, mutable
my_list = [1, 2, 3, 2, 4]
print("List:", my_list)
my_list.append(5)  # add element
print("List after append:", my_list)

try:
    print("Access element at index 2:", my_list[2])
    print("Access element at index 10:", my_list[10])  #  IndexError
except IndexError:
    print("Error: Tried to access an index that doesn't exist in the list.")

# 2. Set - Unordered, no duplicates, mutable
my_set = {1, 2, 3, 2, 4}
print("\nSet:", my_set)  # duplicates removed automatically
my_set.add(5)  # add element
print("Set after add:", my_set)

# 3. Dictionary - Key-value pairs, keys must be unique
my_dict = {"name": "Alice", "age": 25, "city": "Chennai"}
print("\nDictionary:", my_dict)

try:
    print("Access value by key 'name':", my_dict["name"])
    print("Access value by key 'salary':", my_dict["salary"])  #  KeyError
except KeyError:
    print("Error: Tried to access a key that doesn't exist in the dictionary.")

my_dict["age"] = 26  # update value
print("Dictionary after update:", my_dict)

# 4. Tuple - Ordered, allows duplicates, immutable
my_tuple = (1, 2, 3, 2, 4)
print("\nTuple:", my_tuple)

try:
    print("Access element at index 1:", my_tuple[1])
    my_tuple[1] = 10  #  TypeError (tuples are immutable)
except TypeError:
    print("Error: Tuples are immutable, you cannot modify them.")
