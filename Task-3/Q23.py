def second_largest(numbers):
    unique_numbers = list(set(numbers)) 
    unique_numbers.sort()
    return unique_numbers[-2] if len(unique_numbers) >= 2 else None

print(second_largest([10, 20, 4, 45, 99, 99]))  