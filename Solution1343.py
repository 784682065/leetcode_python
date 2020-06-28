from typing import List

"""
给你一个整数数组 arr 和两个整数 k 和 threshold 。
请你返回长度为 k 且平均值大于等于 threshold 的子数组数目。
"""


class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        ans = 0
        # 第一步取出前面 k个数
        arr_sum = sum(arr[0:k])
        if arr_sum >= threshold * k:
            ans += 1

        for index in range(k, len(arr)):
            arr_sum = arr_sum - arr[index - k] + arr[index]
            if arr_sum / k >= threshold:
                ans += 1
        return ans
    # def numOfSubarrays(self, arr, k, threshold):
    #     total_num = len(arr) - k + 1
    #     res = 0
    #     for i in range(total_num):
    #         if i == 0:
    #             arr_sum = sum(arr[0:k])
    #         else:
    #             arr_sum = arr_sum + arr[i + k - 1]
    #
    #         if arr_sum >= threshold * k:
    #             res += 1
    #         arr_sum -= arr[i]
    #     return res


if __name__ == '__main__':
    arr = [2, 2, 2, 2, 5, 5, 5, 8]
    count = Solution().numOfSubarrays(arr, 3, 4)
    print(count)
