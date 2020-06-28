from typing import List


# 寻找峰值
def binarySearch(nums: List[int], left: int, right: int) -> int:
    if left == right:
        return left

    mid = int((left + right) / 2)
    if nums[mid] < nums[mid + 1]:
        return binarySearch(nums, mid + 1, right)
    else:
        return binarySearch(nums, left, mid)


class Solution:
    # 二分查找法
    def findPeakElement(self, nums: List[int]) -> int:
        # return binarySearch(nums, 0, len(nums) - 1)
        l, r = 0, len(nums) - 1
        while l < r:
            mid = int((l + r) / 2)
            if nums[mid] > nums[mid + 1]:
                r = mid
            else:
                l = mid + 1
        return l


if __name__ == '__main__':
    nums = [1, 2, 3, 1]
    res = Solution().findPeakElement(nums)
    print(res)
