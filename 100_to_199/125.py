class Solution:
    def isPalindrome(self, s: str) -> bool:
        word = []
        s = s.lower()

        for w in s:
            if w.isalnum():
                word.append(w)

        i = 0
        j = len(word)-1
        while i < j:
            if word[i] != word[j]:
                return False
            i += 1
            j -= 1

        return True
