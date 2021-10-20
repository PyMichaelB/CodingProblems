class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if any(x == "" for x in strs) or len(strs) == 0:
            return ""

        if len(strs) == 1:
            return strs[0]

        strs_letters = [list(str(string)) for string in strs]
        min_length = min([len(string) for string in strs])

        prefix = ""

        for i in range(min_length):
            first_string_ith_letter = strs_letters[0][i]

            if all(string[i] == first_string_ith_letter for string in strs_letters):
                prefix += first_string_ith_letter
                continue
            else:
                break

        return prefix
