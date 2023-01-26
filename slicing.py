x = 'Jake is AWESOME'

slicedx = x[::-1]
print(slicedx.lower())

my_string_double_quotes = "this is a string"
my_string_single_quotes = 'this is a string'

if my_string_double_quotes == my_string_single_quotes:
    print(f'These two strings are equal and their types are the same too')
else:
    print(f'The two types are likely not the same {type(my_string_double_quotes)} and {type(my_string_single_quotes)}')

my_string = 'I love quotes'

# you can print any index

print(my_string[0])
print(my_string[-1])
