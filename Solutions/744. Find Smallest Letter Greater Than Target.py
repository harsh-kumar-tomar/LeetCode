class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        
        start = 0
        end = len(letters) -1
        n = len(letters)
        target = ord(target)

        while start <= end:
            mid = start + (end-start)//2

            if ord(letters[mid]) == target:
                start = mid + 1
                # return letters[mid+1] if mid < n-1 else letters[0]
            elif ord(letters[mid]) > target:
                end = mid - 1
            else:
                start = mid + 1
        
        return letters[start] if start < n else letters[0]


            