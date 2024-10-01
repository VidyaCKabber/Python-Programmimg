
4. Longest Substring Without Repeating Characters
Problem: Given a string s, find the length of the longest substring without repeating characters.
Example:
Input: s = "abcabcbb"
Output: 3 (substring is "abc")

s = "abbcabcbbcdfg"

def LongestSubString():
    longest_sub_str = s[0]
    start_index = 0
    res_str_len = len(longest_sub_str)

    if not s:
        return None
    for end_index in range(1, len(s)):
        sub_string = s[start_index : end_index+1]
        sub_string_len = len(sub_string)

        if len(set(sub_string)) == sub_string_len:
            res_str_len = max(res_str_len, sub_string_len)

            if res_str_len == sub_string_len:
                longest_sub_str = sub_string
        else:
            start_index += 1

    return res_str_len, longest_sub_str

print(LongestSubString())
