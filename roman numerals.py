def int_to_roman(num):
    """
    Converts an integer to its Roman numeral representation.
    Handles integers from 1 to 3999.
    """
    if not 1 <= num <= 3999:
        return "Input must be an integer between 1 and 3999."

    val = [
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4,
        1
    ]
    syb = [
        "M", "CM", "D", "CD",
        "C", "XC", "L", "XL",
        "X", "IX", "V", "IV",
        "I"
    ]

    roman_num = ""
    i = 0
    while num > 0:
        for _ in range(num // val[i]):
            roman_num += syb[i]
            num -= val[i]
        i += 1
    return roman_num
