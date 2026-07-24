class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        i = len(s) - 1
        j = 0
        while j < i:
            s[i], s[j] = s[j], s[i]
            i -= 1
            j += 1
        
        