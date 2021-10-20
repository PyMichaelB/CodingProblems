class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        parentheses_opened = []
        opened = {'(': 'round', '[': 'square', '{': 'curly'}
        closed = {')': 'round', ']': 'square', '}': 'curly'}

        for char in list(s):

            if char in opened:
                parentheses_opened.append(char)

            elif char in closed:
                if len(parentheses_opened) == 0:
                    # i.e. cannot have opened the bracket
                    return False

                if opened[parentheses_opened[-1]] != closed[char]:
                    return False  # i.e. not same bracket type

                else:
                    parentheses_opened.pop()  # Successfully closed the last opened bracket

        return True if len(parentheses_opened) == 0 else False
