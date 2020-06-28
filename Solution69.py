class Solution:

    #求平方根在牛顿迭代公式中，f(x)=x^2-a，则f'(x）=2x。以上的牛顿迭代公式变为：x(n+1）=x(n）-(x(n)^2-a)/2x，即(x(n)+a/x(n))/2。我们随便猜一个数r，假设r是f(x)=0的根，经过几次牛顿迭代公式后（以上的公式）所得到的x值即是f(x)=0的根或者其非常精确的近似值。
    def mySqrt(self, x: int) -> int:
        """
         :type x: int
         :rtype: int
        """
        if x <= 1:
            return x
        r = x
        while r > x / r:
            r = (r + x/r) // 2
        return int(r)


i = Solution().mySqrt(8)
print(i)
