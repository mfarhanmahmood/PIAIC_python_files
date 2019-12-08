# Python predefined functions and useful code snippets


# input(object): Takes input from user and return it to calling function
string = input("Enter any string: ")

# Taking a number as input
integer_num = input("Enter any Integer number: ")
float_num = input("Enter any Real number: ")

# print(object): Displays the given parameter to the default output device
print('\n ') # printing a new line character
print('Printing a string')
print('Printing variable:', integer_num)

# printing formated/template strings
print(f'\nFormated string var: {string}')

# len(object): Check the length of any string or objects
string_length = len(string)
print(f"\nLength of inputted string is: {string_length}")

# type(object): Check the data type of given parameter
integer_num_type = type(integer_num)
float_num_type = type(float_num)

print(f"""
integer_num variable type is: {integer_num_type}
float_num variable type is: {float_num_type}
""")

# int(string) and float(string): Convert a valid string to integer or float number
integer_num = int(integer_num)
float_num = float(float_num)

# Rechecking type of variable to see if coversion worked
integer_num_type = type(integer_num)
float_num_type = type(float_num)

print(f"""After conversion of types: 

  integer_num variable type is: {integer_num_type}
  float_num variable type is: {float_num_type}
""")


# max(var...): Return the maximum value from numbers given in parameters
max_num = max(15, 25, 17, 102, 550, 154, 22, 1, 0, -5)

print(f"""Maximum number in the list
List: 15, 25, 17, 102, 550, 154, 22, 1, 0, -5
Maximum Number: {max_num}
""")

# round(number, decimal_places): Rounds a number to given decimal places
rounded_num = round(25.25867, 2)
print(f"Rounded 25.25867 to 2 decimal places: {rounded_num}")


