n = input('Enter the word ').lower()

def palindrome(n):
    if n == n[::-1]:
        print("Given Word is a Palindrome")

    else:
        print("Given Word is Not Palindrome")


palindrome(n)