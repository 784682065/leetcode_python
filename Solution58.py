class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # s = s.strip(' ')
        # l = s.split(' ')[-1]
        # return len(l)
        s = s.rstrip()
        n = len(s)
        # range（4，-1，-1）表示从4开始，注意递减，递减至 - 1 的前面那个元素的值，为0 。
        for i in range(n - 1, -1, -1):
            if s[i] == ' ':
                return n - 1 - i
        return n


ans = Solution().lengthOfLastWord(s="Hello World")
print(ans)
