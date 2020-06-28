from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        # 所有放入nums1
        # for i in range(m, m + n):
        #     nums1[i] = nums2[i - m]
        #
        # nums1.sort()

        # 因为是有序数组, 所以从两个的最后一位开始谁大 放进去谁
        i, j = 0, 0

        while j < n:
            if i >= m + j:
                nums1[i:i + n - j] = nums2[j:n]
                break
            if nums1[i] < nums2[j]:
                i += 1
            else:
                nums1[i + 1:] = nums1[i:len(nums1) - 1]
                nums1[i] = nums2[j]
                # python 是 从后向前执行的代码
                # nums1[i], nums1[i+1:] = nums2[j], nums1[i:len(nums1)-1]
                j += 1
                i += 1


if __name__ == '__main__':
    nums1 = [2, 0]
    Solution().merge(nums1,
                     1,
                     [1],
                     1)

    print(nums1)
