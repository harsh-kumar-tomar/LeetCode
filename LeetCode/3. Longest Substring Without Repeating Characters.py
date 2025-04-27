class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        hash_map = set()
        start = 0
        end = n - 1
        longest_substring = 0

        for end in range(n):
            el = s[end]

            if el in hash_map:
                while el in hash_map:
                    temp = s[start]
                    hash_map.remove(temp)
                    start += 1
            
            hash_map.add(el)
            longest_substring = max(longest_substring,len(hash_map))

        return longest_substring

a = Solution().lengthOfLongestSubstring("bbbbb")
print(a)

"""
old code 
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        se = set()

        left = 0
        right = 0
        value = -1

        while right < n:

            if s[right] in se:
                while s[right] in se:
                    se.remove(s[left])
                    left += 1

            se.add(s[right])
            value = max(value,len(se))


            right += 1
        
        return value if value != -1 else 0

"""