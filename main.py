# Function for turning integers into roman numerals.
# Creating lists with integers and the corresponding roman numerals.
integers = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
romans = ["I", "IV", "V", "IX", "X", "XL", "L", "XC", "C", "CD", "D", "CM", "M"]
def int_to_roman(val):
    i = 12
    roman_from_number = ""
    # while-loop that runs as long as value is greater than 0.
    while val > 0:
        # for-loop to see if the value can be divided with the current integer value of i.
        for _ in range(val // integers[i]):
            # adds the character corresponding to the current integer to the string then subtracts
            # it from the overall value (the input)
            roman_from_number += romans[i]
            val -= integers[i]
        i -= 1
    return roman_from_number

# Roman numerals to integers
# Dictionary
trans = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
def roman_to_int(numeral):
    num_from_roman = 0
    # while-loop that runs as long as the length of numeral is more than 0.
    while len(numeral) > 0:
        # After that, it checks if length of the input is greater than 1, and if the next character is equal to
        # 5x or 10x the value of the current one
        if len(numeral) > 1 and trans[numeral[1]] in (trans[numeral[0]] * 5, trans[numeral[0]] * 10):
            # if the next character is greater, you want to subtract the one in front of it.
            add = trans[numeral[1]] - trans[numeral[0]]
            numeral = numeral[2:]
        else:
            # else it adds the value corresponding to the character.
            add = trans[numeral[0]]
            numeral = numeral[1:]
        num_from_roman += add
    return num_from_roman

# Printing out to see that it works.
print(int_to_roman(1994))
print(roman_to_int("MCMXCIV"))

# Prints out 1-3999 in both roman numerals and the corresponding integers
def up_to_3999():
    for i in range(1, 4000):
        # converts value of i to roman numerals
        roman = int_to_roman(i)
        # converts the roman numerals back to an integer
        integer = roman_to_int(roman)
        # prints the values
        print(roman, integer)

up_to_3999()