from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        # num_str = " "
        # for i in digits:
        #     num_str += str(i)
        #
        # # 遍历字符串,每个字符串变成数组的一部分
        # return list(map(int, str(int(num_str) + 1)))
        # 从-1位到1位
        for i in range(len(digits) - 1, -1, -1):
            # 倒序判断,该位为9则替换为0
            if digits[i] == 9:
                digits[i] = 0
            else:
                # 将前一位加一
                num = digits[i]
                digits[i] = num + 1
                break
        # 首位为0,进一位
        if digits[0] == 0:
            digits.insert(0, 1)
        return digits


an = Solution().plusOne([0,1,9,9])
print(an)
# for i in range(len(an)):
#     print(an[i])
