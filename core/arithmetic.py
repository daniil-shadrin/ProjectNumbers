def addition_with_carry(num1: str, num2: str, base: int, alphabet):
    max_len = max(len(num1), len(num2))
    num1 = num1.rjust(max_len, alphabet[0])
    num2