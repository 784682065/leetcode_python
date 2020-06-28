from typing import List


class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        # num = 0
        # temp = heights.copy()
        # temp.sort()
        # for i in range(len(heights)):
        #     if temp[i] != heights[i]:
        #         num = num + 1
        #
        # return num
        # >> > a = [1, 2, 3]
        # >> > b = [4, 5, 6]
        # >> > zipped = zip(a, b)  # 打包为元组的列表
        # >> > c = [4, 5, 6, 7, 8]
        # >> > zip(a, c)  # 元素个数与最短的列表一致
        # [(1, 4), (2, 5), (3, 6)]
        return sum(h1 != h2 for h1, h2 in zip(heights, sorted(heights)))


if __name__ == '__main__':
    count = Solution().heightChecker([1, 1, 4, 2, 1, 3])
    print(count)
