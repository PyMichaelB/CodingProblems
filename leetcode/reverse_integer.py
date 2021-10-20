class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        sign = 1
        if x < 0:
            sign = -1

        digits = list(str(sign * x))
        num_digits = len(digits)

        result_without_sign = []
        for i in range(num_digits):
            result_without_sign.append(int(digits[num_digits - 1 - i]))

        result = 0
        for i in range(num_digits):
            result += sign * result_without_sign[i] * (10 ** (num_digits - 1 - i))

        if result > 2 ** 31 - 1 or result < -1 * 2 ** 31:
            return 0
        else:
            return result