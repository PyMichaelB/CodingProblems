class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        array_of_numerals = list(s)
        numerals_value = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

        converted_num = 0
        previous_numeral = None

        for numeral in array_of_numerals:

            if numeral == "D" or numeral == "M":
                if previous_numeral == "C":
                    converted_num -= 2 * numerals_value[previous_numeral]
            elif numeral == "L" or numeral == "C":
                if previous_numeral == "X":
                    converted_num -= 2 * numerals_value[previous_numeral]
            elif numeral == "V" or numeral == "X":
                if previous_numeral == "I":
                    converted_num -= 2 * numerals_value[previous_numeral]

            converted_num += numerals_value[numeral]
            previous_numeral = numeral

        return converted_num
