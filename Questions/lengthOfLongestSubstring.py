# 3. Longest Substring Without Repeating Characters
# Solved
# Medium
# Topics
# Companies
# Hint
# Given a string s, find the length of the longest 
# substring
#  without repeating characters.

# Example 1:

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
# Example 2:

# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:

# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if not len(s):
            return 0
        
        max_long_sub_string = len(s[0])
        start_index = 0

        for end_index in range(len(s)):
            sub_str = s[start_index : end_index+1]
            sub_str_len = len(sub_str)
            
            if sub_str_len == len(set(sub_str)):
                max_long_sub_string = max(max_long_sub_string, sub_str_len)
            else:
                start_index += 1

        return max_long_sub_string


