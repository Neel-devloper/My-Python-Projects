# this code will convert a mixed number to an improper fraction and then calculate the result
try:
    from fractions import Fraction
    mixed_number1 = input('enter mixed number1: ')
    operation = input('enter operation: ')
    mixed_number2 = input('enter mixed number2: ')
    parts1 = mixed_number1.split(' ') # parts1 = ['3','3/4']
    parts2 = mixed_number2.split(' ') # parts2 = ['1','1/4']
    whole_number1 = parts1[0] # 3
    whole_number2 = parts2[0] # 1
    fraction_part1 = parts1[1] # 3/4
    fraction_part2 = parts2[1] # 1/4
    numerator1 = fraction_part1[0]
    denominator1 = fraction_part1[2]
    numerator2 = fraction_part2[0]
    denominator2 = fraction_part2[2]
    improper_fraction_numerator1 = int(whole_number1)*int(denominator1)+int(numerator1) # whole number = 3 * denominator + numerator
    improper_fraction_denominator1 = denominator1
    improper_fraction_numerator2 = int(whole_number2)*int(denominator2)+int(numerator2)
    improper_fraction_denominator2 = denominator2
    improper_fraction1 = f'{improper_fraction_numerator1} / {improper_fraction_denominator1}'
    improper_fraction2 = f'{improper_fraction_numerator2} / {improper_fraction_denominator2}'
    improper_fraction1 = Fraction(improper_fraction1)
    improper_fraction2 = Fraction(improper_fraction2)
#done converting the mixed number to an improper fraction
    frac1 = improper_fraction1
    frac2 = improper_fraction2
# calculating the answer to the question


    if operation == '+':
        result = frac1 + frac2
        if result.denominator == 1:
            print(f'the answer to {frac1} {operation} {frac2} is {result.numerator}')
        elif result.denominator < result.numerator:
            whole_number = result.numerator // result.denominator
            numerator = result.numerator % result.denominator
            denominator = result.denominator
            print(f'the answer to {frac1} {operation} {frac2} is {whole_number} {numerator}/{denominator}')
        elif result.numerator == result.denominator:
            print(f'the answer to {frac1} {operation} {frac2} is 1')
        else:
            print(f'the answer to {frac1} {operation} {frac2} is {result}')

    elif operation == '-':
        result = frac1 - frac2
        if result.denominator == 1:
            print(f'the answer to {frac1} {operation} {frac2} is {result.numerator}')
        elif result.denominator < result.numerator:
            whole_number = result.numerator // result.denominator
            numerator = result.numerator % result.denominator
            denominator = result.denominator
            print(f'the answer to {frac1} {operation} {frac2} is {whole_number} {numerator}/{denominator}')
        elif result.numerator == result.denominator:
            result = 1
            print(f'the answer to {frac1} {operation} {frac2} is {result}')
        else:
            print(f'the answer to {frac1} {operation} {frac2} is {result}')
    elif operation == 'X':
        result = frac1 * frac2
        if result.denominator == 1:
            print(f'the answer to {frac1} {operation} {frac2} is {result.numerator}')
        elif result.denominator < result.numerator:
            whole_number = result.numerator // result.denominator
            numerator = result.numerator % result.denominator
            denominator = result.denominator
            print(f'the answer to {frac1} {operation} {frac2} is {whole_number} {numerator}/{denominator}')
        elif result.numerator == result.denominator:
            print(f'the answer to {frac1} {operation} {frac2} is 1')
        else:
            print(f'the answer to {frac1} {operation} {frac2} is {result}')
    elif operation == '/':
        result = frac1 / frac2
        if result.denominator == 1:
            print(f'the answer to {frac1} {operation} {frac2} is {result.numerator}')
        elif result.denominator < result.numerator:
            whole_number = result.numerator // result.denominator
            numerator = result.numerator % result.denominator
            denominator = result.denominator
            print(f'the answer to {frac1} {operation} {frac2} is {whole_number} {numerator}/{denominator}')
        elif result.numerator == result.denominator:
            print(f'the answer to {frac1} {operation} {frac2} is 1')
        else:
            print(f'the answer to {frac1} {operation} {frac2} is {result}')
    else:
        print('please enter a valid operation like +,-,X or /')
except KeyboardInterrupt:
    exit()
except IndexError:
    print('please enter a MIXED NUMBER')