class Solution:
    def max_product(self, n):

        product, self.max_prod = 1, 1
        digits = [int(digit) for digit in str(n)]
        digits.sort()
        print(digits)
        for i in range(len(digits)-1):
            product = digits[i] * digits[i+1]
            if self.max_prod < product:
                self.max_prod = product
        print(self.max_prod)


s = Solution()
s.max_product(267)