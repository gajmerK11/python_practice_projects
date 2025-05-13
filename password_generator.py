import random
import string

print("Welcome To Your Password Generator")

chars = string.ascii_letters + string.digits + string.punctuation

number = input("Number of passwords to generate: ")
number = int(number)

length = input("Enter the length of your password: ")
length = int(length)

print("\nHere are your passwords:")

for pwd in range(number):
    # here "_" is used as loop variable - it is Python convention of writing for loop when loop variable is not needed and you just want loop to run particular number of times
    password = ''.join(random.choice(chars) for _ in range(length))
    print(password)