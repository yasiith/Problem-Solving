s = input()

# checks is a list of boolean values
# any() function returns True if any of the character in the string s satisfies the condition
checks = [any(char.isalnum() for char in s),
          any(char.isalpha() for char in s),
          any(char.isdigit() for char in s),
          any(char.islower() for char in s),
          any(char.isupper() for char in s)]

# (*) is used to unpack the list
# unpacking occurs when each element of the list is passed as a seperate
# argument to the print() function

print(*checks, sep='\n')

# any() function
# in python, this is a built-in function that returns true if at least one element of given iterable
# is true