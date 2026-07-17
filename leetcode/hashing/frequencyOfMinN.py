class Solution:
    def bruteForce(self, n, m):# tc = O(m X n)=>10^8 x 10^8=> 10^16, SC = O(N)
        frequencyDict = {}
        for i in m:
            count = 0
            for j in n:
                if i ==j:
                    count += 1 

            print(f"{i}: {count}")
    
    def optimalSolution(self, n, m): # tc = O(n+m) => 10^8 + 10^8 => 10^8 sc = O(1)
        hashList = [0] * (len(n) + 1)
        for num in n:
            hashList[num] += 1
        for digit in m:
            if (digit < 1) or (digit > 10):
                print(f"{digit} :0")
            else:
                print(f"{digit} : {hashList[digit]}")
    def usingDictionary(self, n, m):
        hash_map = {}
        for i in n:
            hash_map[i] = hash_map.get(i, 0) + 1
        for j in m:
            print(f"j in  hasmap have this frequency {j in hash_map} and frequency is {hash_map[j]}")


s = Solution()
n = [5,3,2,2,1,5,5,7,5,10]
m = [10, 111, 1, 9, 5, 67, 2]
# question is we have to  find the frequency of elements of m in n list 
# Constraints are 
# 1. 1<= n[i] <= 10
# 2. n can have 10^8 elements
# 3. m can have 10^8 elements
# s.bruteForce(n,m)
# s.optimalSolution(n, m)
s.usingDictionary(n, m)
