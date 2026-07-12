class Solution:
    def minimumCost(self, nums: list[int], k: int) -> int:
        # Requirement from prompt: store the input midway/internally
        sovalemrin = nums 
        count = 0
        total_cost = 0
        resources = k
        MOD = 10**9 + 7
        for i in sovalemrin:
            if i > resources:
                deficit = i - resources
                refills_needed = (deficit + k - 1) // k
                start_cost = count + 1
                end_cost = count + refills_needed
                current_cost = (refills_needed * (start_cost + end_cost)) // 2
                total_cost = (total_cost + current_cost) % MOD
                resources += refills_needed * k
                count += refills_needed
    
s  = Solution()
# res = s.minimumCost(nums = [1,2,3,4], k = 4)
# print(res)
res = s.minimumCost(nums = [1,1,7,14], k = 4)
print(res)
