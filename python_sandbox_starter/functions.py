# A function is a block of code which only runs when it is called. In Python, we do not use parentheses and curly brackets, we use indentation with tabs or spaces

#Passing a default value to a function that can be overwritten when the function is called
def say_hello(name = 'Alex'):
    print(f'1. Hello {name}.')

say_hello()


# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression. Very similar to JS arrow functions
get_sum = lambda num1, num2 : num1 + num2

print('Lambda function:', get_sum(3, 4))
