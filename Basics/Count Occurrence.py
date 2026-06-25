str = 'This is Selenium python with API Selenium python'
str = str.split()

result = {}

for i in str:
    result[i] = result.get(i, 0) +1

for key, value in result.items():
    print(f'{key} = {value}')