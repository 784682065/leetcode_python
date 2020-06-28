from typing import List


class Solution:

    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        # 暴力解法双for循环
        """
        length = len(nums)
        if length == 0:
            return 0

        ans = 1000000
        for index in range(0, length):
            sum = 0
            for index2 in range(index, length):
                sum += nums[index2]
                if (sum >= s):
                    ans = min(ans, index2 - index + 1)
                    break

        return 0 if ans == 1000000 else ans
        """

        # 双指针法
        if not nums:
            return 0

        n = len(nums)
        ans = n + 1
        start, end = 0, 0
        total = 0
        while end < n:
            total += nums[end]
            while total >= s:
                ans = min(ans, end - start + 1)
                total -= nums[start]
                start += 1
            end += 1

        return 0 if ans == n + 1 else ans


if __name__ == '__main__':
    l = Solution().minSubArrayLen(7, [2, 3, 1, 2, 4, 3])
    print(l)
