def roman_to_int(s):
    roman_to_int_map = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    total = 0
    prev_value = 0

    for x in reversed(s): # right to left
        current_value = roman_to_int_map[x]
        if current_value < prev_value:
            total -= current_value
        else:
            total += current_value

        prev_value = current_value

    return total


print(roman_to_int(input('enter roman numeral: ')))
