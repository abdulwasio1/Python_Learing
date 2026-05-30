'''
An anonymous function is a function without a name. In Python, these are created using the lambda keyword.
SYNTAX
lambda arguments : expression
'''

# def power (base , exponent):
#     return base ** exponent

# result = power(2, 5)
# print(result)

# USING ANONYMOUS FUNCTION

result = lambda base , power : base ** power

'''
When Python executes lambda a, b: a + b, it creates a nameless function object first. At that moment, it has no name.
Then separately, that object gets assigned to the variable result so result variable is just a label pointing to it..
'''

print(result(2,5))

