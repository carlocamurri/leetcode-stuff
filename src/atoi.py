class Solution:

    def char_is_numeric(self, char):
        return char.isnumeric() or char == '-' or char == '+'

    def atoi(self, string):
        INT_MIN = -(2**31)
        INT_MAX = 2**31 - 1
        stripped = string.lstrip(' ')
        if stripped == '':
            return 0
        first_char = stripped[0]
        if not self.char_is_numeric(first_char):
            return 0
        number_string = ''
        for char in stripped:
            if self.char_is_numeric(char):
                number_string += char
            else:
                break
        number = int(number_string)
        if number < INT_MIN:
            return INT_MIN
        elif number > INT_MAX:
            return INT_MAX
        return number
