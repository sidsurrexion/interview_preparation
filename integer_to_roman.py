predefined_integer_to_roman = {
    1: 'I',
    4: 'IV',
    5: 'V',
    9: 'IX',
    10: 'X',
    40: 'XL',
    50: 'L',
    90: 'XC',
    100: 'C',
    400: 'CD',
    500: 'D',
    900: 'CM',
    1000: 'M'
}


def compute_conversion(roman_text, base, number):
    q = int(number / base)
    r = number % base
    roman_text += predefined_integer_to_roman[base] * q
    return roman_text, r


def convert_integer_to_roman(number):
    roman_text = ''
    while number != 0:
        if number >= 1000:
            roman_text, number = compute_conversion(roman_text, 1000, number)
        elif number >= 500:
            if number >= 900:
                roman_text, number = compute_conversion(roman_text, 900,
                                                        number)
            else:
                roman_text, number = compute_conversion(roman_text, 500,
                                                        number)
        elif number >= 100:
            if number >= 400:
                roman_text, number = compute_conversion(roman_text, 400,
                                                        number)
            else:
                roman_text, number = compute_conversion(roman_text, 100,
                                                        number)
        elif number >= 50:
            if number >= 90:
                roman_text, number = compute_conversion(roman_text, 90, number)
            else:
                roman_text, number = compute_conversion(roman_text, 50, number)
        elif number >= 10:
            if number >= 40:
                roman_text, number = compute_conversion(roman_text, 40, number)
            else:
                roman_text, number = compute_conversion(roman_text, 10, number)
        else:
            if number == 9:
                roman_text, number = compute_conversion(roman_text, 9, number)
            elif number >= 5:
                roman_text, number = compute_conversion(roman_text, 5, number)
            elif number == 4:
                roman_text, number = compute_conversion(roman_text, 4, number)
            else:
                roman_text, number = compute_conversion(roman_text, 1, number)
    return roman_text

for i in range(1, 100):
    print(i, convert_integer_to_roman(i))
