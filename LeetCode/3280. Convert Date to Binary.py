class Solution:
    def convertDateToBinary(self, date: str) -> str:
        date = date.split("-")
        ans = "-".join(self.convertToBinary(int(word)) for word in date)
        return ans

    def convertToBinary(self,num):
        ans = ""
        while num != 0:
            remainder = num % 2
            ans = str(remainder) + ans
            num = num // 2
        print(ans)
        return ans