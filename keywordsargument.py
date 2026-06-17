# Keyword arguments example
def print_details(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# Function with positional and keyword arguments
def show_arguments(*args, **kwargs):
    for val in args:
        print(f"Positional argument: {val}")

    for key, value in kwargs.items():
        print(f"{key}: {value}")

# Calling print_details
print_details(name="Riya", age="22", country="India")

print()  # blank line

# Calling show_arguments
show_arguments(1, 2, 3, 4, "Riya",
               name="Riya",
               age="22",
               country="India")