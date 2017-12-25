 #length of the longest substring without repeating characters.
 class Solution(object):
    def lengthOfLongestSubstring(self, s):
        hasfound = {}
        window = 0
        start = -1
        for i in range (len(s)):
            if s[i] in hasfound and start <= hasfound[s[i]]:
                start = hasfound[s[i]]
            else:
                 window = max(window,i-start)
            hasfound[s[i]] = i
        return window
