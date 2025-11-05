from .alphabets import generate_alphabet, str_to_value_map

def convert_to_decimal(number, base, alphabet):
    value_map = str_to_value_map(alphabet)
    number = number.strip()
    result = 0
    for char in number:
        if char not in value_map or value_map[char] >= base:
            raise ValueError(f'Недопустимый символ "{char}" для системы счисления с основанием {base}')
        result = result * base + value_map[char]
    return result

def convert_from_decimal(number, base, alphabet):
    if number == 0:
        return alphabet[0]
    digits = []
    while number > 0:
        number, remainder = divmod(number, base)
        digits.append(alphabet[remainder])
    return ''.join(reversed(digits))

def convert_number(number_str, base_from, base_to):
    alphabet_from = generate_alphabet(base_from)
    alphabet_to = generate_alphabet(base_to)
    dec_value = convert_to_decimal(number_str, base_from, alphabet_from)
    return convert_from_decimal(dec_value, base_to, alphabet_to)