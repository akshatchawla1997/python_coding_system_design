class Solution:
    def minimumCost(self, nums: list[int], k: int) -> int:
        print(nums)
        count = 0
        total_cost = 0
        resources = k # 4, 3, 2, 6, 10, 3,  7, 11, 15, 
        for i in nums:
            while ( i> resources):                
                resources = resources + k
                count += 1
                total_cost += count
                print(f"more than {resources}")
            if i < resources:
                resources -= i
                print(f"less than {resources}")
        return total_cost
    
s  = Solution()
# res = s.minimumCost(nums = [1,2,3,4], k = 4)
# print(res)
res = s.minimumCost(nums = [1,1,7,14], k = 4)
print(res)
