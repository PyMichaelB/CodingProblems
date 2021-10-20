class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False

        if x == 0:
            return True

        # x is now a positive number

        x_str = str(x)
        if x_str[::-1] == x_str:
            return True
        else:
            return False