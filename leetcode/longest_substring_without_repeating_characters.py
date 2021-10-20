class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        chars = list(s)
        i = j = res = 0

        while j < len(chars):
            if not chars[j] in seen:

                seen.add(chars[j]);
                j += 1
                res = max(len(seen), res)

            else:

                seen.remove(chars[i])
                i += 1

        return res
