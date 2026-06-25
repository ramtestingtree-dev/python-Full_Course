lt = [23, 33, 44, 66, 77, 41, 98]
large = lt[0]

for num in lt:          #Loop Method
    if num > large:
        large = num

lt.sort()
print(lt)        #Using Sort function
print(f'Second Largest: {lt[-2]}')
print(f'Largest number:{large}')
lt.sort(reverse=True)
print(lt)


