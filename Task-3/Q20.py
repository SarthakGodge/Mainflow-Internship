def decimal_to_binary(m):
    binary = ""
    while m > 0:
        binary = str(m % 2) + binary
        m = m // 2
    return binary or "0"  

print(decimal_to_binary(11))