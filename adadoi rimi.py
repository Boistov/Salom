def roman(rim):
    try:
        num = int(rim)
    except ValueError:
        return "Invalid input. Please provide a valid integer."
    symbols = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    roman_num = ''
    i = 0
    while num > 0:
        for _ in range(num // values[i]):
            roman_num += symbols[i]
            num -= values[i]
        i += 1
    
    return roman_num

number_str = input("Enter an integer: ")
print(roman(number_str))
