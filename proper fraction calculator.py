from fractions import Fraction
try:
    fraction1 = input('enter fraction 1: ')
    operation = input('enter operation: ')
    fraction2 = input('enter fraction 2: ')


    frac1 = Fraction(fraction1)
    frac2 = Fraction(fraction2)


    if operation=='+':
        result=frac1+frac2
        if result.denominator==1:
            # then only print the numerator
            print(f'the answer to {frac1} {operation} {frac2} is {result.numerator}')
        elif result.denominator<result.numerator:
            whole_number = result.numerator//result.denominator
            numerator = result.numerator%result.denominator
            denominator = result.denominator
            print(f'the answer to {frac1} {operation} {frac2} is {whole_number} {numerator}/{denominator}')
        elif result.numerator==result.denominator:
            print(f'the answer to {frac1} {operation} {frac2} is 1')
        else:
            print(f'the answer to {frac1} {operation} {frac2} is {result}')

    elif operation=='-':
        result = frac1 - frac2
        if result.denominator==1:
            print(f'the answer to {frac1} {operation} {frac2} is {result.numerator}')
        elif result.denominator<result.numerator:
            whole_number = result.numerator // result.denominator
            numerator = result.numerator%result.denominator
            denominator = result.denominator
            print(f'the answer to {frac1} {operation} {frac2} is {whole_number} {numerator}/{denominator}')
        elif result.numerator==result.denominator:
            print(f'the answer to {frac1} {operation} {frac2} is 1')
        else:
            print(f'the answer to {frac1} {operation} {frac2} is {result}')
    elif operation=='X':
        result = frac1*frac2
        if result.denominator==1:
            print(f'the answer to {frac1} {operation} {frac2} is {result.numerator}')
        elif result.denominator<result.numerator:
            whole_number = result.numerator // result.denominator
            numerator = result.numerator % result.denominator
            denominator = result.denominator
            print(f'the answer to {frac1} {operation} {frac2} is {whole_number} {numerator}/{denominator}')
        elif result.numerator==result.denominator:
            print(f'the answer to {frac1} {operation} {frac2} is 1')
        else:
            print(f'the answer to {frac1} {operation} {frac2} is {result}')
    elif operation=='/':
        result = frac1/frac2
        if result.denominator==1:
            print(f'the answer to {frac1} {operation} {frac2} is {result.numerator}')
        elif result.denominator<result.numerator:
            whole_number = result.numerator // result.denominator
            numerator = result.numerator % result.denominator
            denominator = result.denominator
            print(f'the answer to {frac1} {operation} {frac2} is {whole_number} {numerator}/{denominator}')
        elif result.numerator==result.denominator:
            print(f'the answer to {frac1} {operation} {frac2} is 1')
        else:
            print(f'the answer to {frac1} {operation} {frac2} is {result}')
    else:
        print('please enter a valid operation')



except ValueError: # not entering valid fractions
    print('please enter valid fractions')
except KeyboardInterrupt: # stopping the code in between form the python
    exit()

