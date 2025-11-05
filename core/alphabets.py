def generate_alphabet(base: int):
    if not 2 <= base <= 50:
        raise ValueError
    alphabet = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    return list(alphabet)[:base]

def str_to_value_map(alphabet):
    return {char: idx for idx, char in enumerate(alphabet)}