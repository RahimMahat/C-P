'''
Given a string s, find the length of the longest substring without repeating characters
'''

def lengthOfLongestSubstring(s) -> int:
        m = {}
        left, right = 0, 0
        ans = 0
        n = len(s)
        
        while left < n and right < n:
            el = s[right]
            if el in m:
                left = max(left, m[el]+1)
            m[el] = right
            ans = max(ans, right - left + 1)
            right += 1
        
        return ans

s = "abcabcbb"
res = lengthOfLongestSubstring(s)
print(res)