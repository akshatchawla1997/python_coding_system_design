class Solution:
    def max_product(self, n):
        q = n
        product = 1
        while(q > 0):
            r = q % 10
            q = q//10
            product *= r
        print(product)
        return product


s = Solution()
s.max_product(267)