class Solution:
    def countAndSay(self, n: int) -> str:

        arr = [0]*(n+1)
        arr[1] = "1"
        for i in range(2,n+1):
            a = arr[i-1]
            arr[i] = self.traverse(str(a))
        
        return arr[n]

    def traverse(self,n:str):
        char = n[0]
        count = 1
        curr_pointer = 1
        r = []

        while curr_pointer <= len(n):

            if curr_pointer == len(n):
                r.append(str(count))
                r.append(char)
                break

            if n[curr_pointer] == char:
                count += 1
            else:
                r.append(str(count))
                r.append(char)
                char = n[curr_pointer]
                count = 1
            
            curr_pointer += 1
        
        return "".join(r)

a = Solution().countAndSay(4)
print(a)

"""
apporach 1
class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        
        a = self.countAndSay(n-1)
        b = self.traverse(str(a))
        
        return b

    
    def traverse(self,n:str):
        char = n[0]
        count = 1
        curr_pointer = 1
        r = []


        while curr_pointer <= len(n):

            if curr_pointer == len(n):
                r.append(str(count))
                r.append(char)
                break

            if n[curr_pointer] == char:
                count += 1
            else:
                r.append(str(count))
                r.append(char)
                char = n[curr_pointer]
                count = 1
            
            curr_pointer += 1
        
        return "".join(r)
"""