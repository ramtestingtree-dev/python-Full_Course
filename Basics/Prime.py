n = 17

is_prime = True

for i in range(2, n):
    if n%i == 0:
        is_prime = False
        break
if is_prime:
    print('Given Number is Prime Number')

else:
    print('Given Number is Not a Prime Number')