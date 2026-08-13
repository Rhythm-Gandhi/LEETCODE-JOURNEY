class Solution:
    def isPalindrome(self, s: str):
        str = ""
        for i in s:
            if i.isalnum():
                str+= i.lower()
        rev = str[::-1]
        if str==rev:
            return True
        return False