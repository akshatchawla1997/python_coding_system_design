from itertools import count
from typing import List
class Solution:
    def maximumWidth(self, planks: List[int]) -> int:
        hash_map = {}
        max_count = 0
        result = {} 
        arr = []

        for i in planks:
            hash_map[i] = hash_map.get(i, 0) + 1
        print(f"hash_map: {hash_map}")
        max_key = max(hash_map.keys())
        print(f"max_key: {max_key}")
        target = max_key
        
        for i in range(0, len(planks) - 1):
            sum = planks[i] + planks[i + 1]
            print(f"sum: {sum}")
            if sum == target:
                max_count += 1
                arr.append(i)
                arr.append(i + 1)
        print(f"arr: {arr}")
        result[max_key] = hash_map[max_key] + hash_map[max_key]
        print(f"result: {result} and hash_map[max_key]: {hash_map[max_key]} and max_count: {max_count}")
        return count

s = Solution()
planks = [1,3,2,5,7,5,4,2,1]
s.maximumWidth(planks)