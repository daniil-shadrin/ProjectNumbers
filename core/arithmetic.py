from .alphabets import str_to_value_map

def addition_with_carry(num1: str, num2: str, base: int, alphabet):
    max_len = max(len(num1), len(num2))
    num1 = num1.rjust(max_len, alphabet[0])
    num2 = num2.rjust(max_len, alphabet[0])
    value_map = str_to_value_map(alphabet)

    carry = 0
    result = []
    steps = []
    for i in range(max_len - 1, -1, -1):
        d1 = value_map[num1[i]]
        d2 = value_map[num2[i]]
        s = d1 + d2 + carry
        carry, digit = divmod(s, base)
        result.append(alphabet[digit])
        steps.append(f'После последнего разряда перенос {carry} записываем в следующий разряд')
    if carry > 0:
        result.append(alphabet[carry])
    
    return ''.join(reversed(result)), steps
def subtraction_with_borrow(num1, num2, base, alphabet):
    max_len = max(len(num1), len(num2))
    num1 = num1.rjust(max_len, alphabet[0])
    num2 = num2.rjust(max_len, alphabet[0])
    value_map = str_to_value_map(alphabet)

    borrow = 0
    result = []
    steps = []
    for i in range(max_len - 1, -1, -1):
        d1 = value_map[num1[i]] - borrow
        d2 = value_map[num2[i]]

        if d1 < d2:
            d1 += base
            borrow = 1
            step_str = f'Разряд {max_len - i}: {value_map[num1[i]]} - перенос 1 + {base} < {d2}, заимствуем 1'
        else:
            borrow = 0
            step_str = f'Разряд {max_len - i}: {d1} - {d2}'
        diff = d1 - d2
        result.append(alphabet[diff])
        step_str += f' = {diff}, записываем {alphabet[diff]}, заимствование {borrow}'
        steps.append(step_str)
    res_str = ''.join(reversed(result)).lstrip(alphabet[0])
    if not res_str:
        res_str = alphabet[0]
    return res_str, steps