class Solution:
    def isPalindrome(self, x: int) -> bool:
        new_num = str(x)[::-1]
        if str(x) == new_num:
            return True
        return False
