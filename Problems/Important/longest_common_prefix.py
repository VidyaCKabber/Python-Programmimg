# Longest Common Prefix

# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".


# Example 1:

# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# Example 2:

# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.

# Attemp 1
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) > 0 and strs[0] != "" and strs[0] is not None:
            first_check = all(i.startswith(strs[0][0]) for i in strs)
            if first_check:
                min_word = strs[0]
                first_word_len = len(strs[0])
                for word in strs[1:]:
                    if len(word) < first_word_len:
                        first_word_len = len(word) 
                        min_word = word
                
                new_strs = strs.copy()
                new_strs.remove(min_word)
                is_not_found = False
                
                while len(min_word) > 0:
                    track_count = 0
                    for index, word in enumerate(new_strs):
                        if word.startswith(min_word):
                            track_count +=1
                        elif len(min_word) == 1 and min_word not in word:
                            is_not_found = True
                            break
                        else:
                            if len(strs)%2 != 0:
                                last_index = len(min_word) - index
                            else:
                                last_index = len(min_word) - index - 1
                            min_word = min_word[:last_index]
                
                    if track_count == len(new_strs):
                        break
                    elif is_not_found:
                        min_word = ""
                        break
                return min_word
            else:
                return ""


# Optmised
# Alogithem : the longest common prefix cannot be longer than the shortest string in the list
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        first_min_word = min(strs, key=len)
        min_words = [first_min_word]
        strs.remove(first_min_word)
        for word in strs:
            if len(word) == len(first_min_word):
                min_words.append(word) 
        
        for min_word in min_words:      
            for i, char in enumerate(min_word):
                for word in strs:   
                    if word[i] != char:
                        if i == 0:
                            return ""
                        return min_word[:i]
        return min_word
        else:
            return ""

