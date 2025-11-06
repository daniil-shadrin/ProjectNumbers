roman_numerals = [
    ('M', 1000),
    ('CM', 900),
    ('D', 500),
    ('CD', 400),
    ('C', 100),
    ('XC', 90),
    ('L', 50),
    ('XL', 40),
    ('X', 10),
    ('IX', 9),
    ('V', 5),
    ('IV', 4),
    ('I', 1),
]

def int_to_roman(num):
    if not (1 <= num <= 3999):
        raise ValueError
    result = []
    for roman, value in roman_numerals:
        while num >= value:
            num -= value
            result.append(roman)
    return ''.join(result)

def roman_to_int(s):
    s = s.upper()
    i = 0
    num = 0
    for roman, value in roman_numerals:
        while s[i:i + len(roman)] == roman:
            i += len(roman)
            if i >= len(s):
                break
    if i != len(s):
        raise ValueError('Некорректное римское число')
    if not (1 <= num <= 3999):
        raise ValueError('Результат выходит за пределы 1 - 3999')
    return num