class Solution:
    def isPalindrome(self, s: str) -> bool:
        newS = s.lower().replace(" ","")
        newS = "".join(ch for ch in newS if ch.isalnum())
        print(newS)
        if newS == newS[::-1]:
            return True
        else:
            return False