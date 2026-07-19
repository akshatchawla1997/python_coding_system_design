class Solution:
    def smallestSubsequence(self, s: str) -> str:
        hash_map = {}
        for i in s:
            hash_map[i] = hash_map.get(i,0) + 1
        result =  "".join(hash_map)
        print(f"option 1 result {result}")
        return sorted(result) 
    
    def alternative(self, s:str) -> str:
        str = ""
        for i in s:
            if  i in str:
                str = str.replace(i,"")
                print(f"{i} after removing {str}")
            if i not in str:
                str = str + i
                print(f"{i} after addition {str}")

        print(f"option 2 {str}")
        return str
        
s = Solution()
# s.smallestSubsequence("cbacdcbc")
s.alternative("cbacdcbc")