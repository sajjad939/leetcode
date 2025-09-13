class Solution:
    def doesAliceWin(self, s: str) -> bool:
        vowels = set("aeiou")
        # Check if at least one character in s is a vowel
        for ch in s:
            if ch in vowels:
                return True
        return False
