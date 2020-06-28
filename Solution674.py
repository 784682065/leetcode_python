from typing import List


class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        cur = 1
        # 最少是一个最长数列
        madlen = 1
        l = len(nums)
        if l == 0:
            return 0

        for i in range(1, l):
            if nums[i] > nums[i - 1]:
                cur += 1
            else:
                madlen = max(madlen, cur)
                cur = 1

        return max(madlen, cur)


if __name__ == '__main__':
    l = Solution().findLengthOfLCIS([1, 3, 5, 4, 7])
    print(l)
