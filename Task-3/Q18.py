def swap_numbers(a, b):
    print(f"Before swap: a = {a}, b = {b}")
    a = a + b
    b = a - b
    a = a - b  
    print(f"After swap: a = {a}, b = {b}")

swap_numbers(10, 20)