from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # 矩阵转90° 等于先 转置矩阵,然后再 翻转一行
        # n = len((matrix[0]))  # 获取矩阵一行的长度
        #
        # # transpose matrix
        # for i in range(n):
        #     for j in range(i, n):
        #         matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        #
        # # reverse each row
        # for i in range(n):
        #     matrix[i].reverse()
        m = zip(*matrix)  # 切片 例如: 切下第一列  1,4,7  , *
        for i, _m in enumerate(m):
            matrix[i] = list(_m)[::-1]  # list函数变成list;  [::-1] 翻转一下 变成7,4,1


if __name__ == '__main__':
    matrix: List[List[int]] = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    Solution().rotate(matrix)
    print(matrix)
    # a = 'python'
    # b = a[::-1]
    # print(b)  # nohtyp  逆置
    # c = a[::-2]
    # print(c)  # nhy 隔一个逆置
    # # 从后往前数的话，最后一个位置为-1
    # d = a[:-1]  # 从位置0到位置-1之前的数 d = a[:-1] 等价于 d = a[0:-1]
    # print(d)  # pytho
    # e = a[:-2]  # 从位置0到位置-2之前的数
    # print(e)  #pyth
