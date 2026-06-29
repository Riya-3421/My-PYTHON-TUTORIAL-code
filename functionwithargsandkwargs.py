def print_args_kwargs(*args, **kwargs):
    # Print positional arguments as a tuple
    print('args:', args)
    # Print keyword arguments as a dictionary
    print('kwargs:', kwargs)

# Test 1: Mixed integers and strings
print_args_kwargs(1, 2, 3, a='Apple', b='Banana')
print("-" * 30)

# Test 2: Mixed strings and named numbers
print_args_kwargs('hello', 'world', x=10, y=2)
