class Solution:
    def countLargestGroup(self, n: int) -> int:
        hash_map = {}
        count = 0

        for i in range(1,n+1):
            key = sum(list(map(int,list(str(i)))))
            hash_map[key] = hash_map.get(key,0)+1
        
        max_val = hash_map[max(hash_map,key=hash_map.get)]

        for key,val in hash_map.items():
            if val == max_val:
                count += 1
        
        return count
    #     sum_of_digits =  [0]*self.count_digits(n)

    #     for i in range(1,n+1):
    #         self.give_sum(i,sum_of_digits)

    # def give_sum(self,n:int,sum_of_digits:list[int]):


    
    # def count_digits(self,n:int):
    #     count = 0

    #     while n != 0 :
    #         n = n//10
    #         count += 1
    #     return count

    


a = Solution().countLargestGroup(2)
print(a)