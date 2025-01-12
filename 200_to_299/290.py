class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        dic = {}
        arr_words = s.split(" ")
        arr_pattern = [*pattern]
        if len(set(arr_words)) != len(set(arr_pattern)) or len(arr_words) != len(arr_pattern):
            return False
        for i in range(len(arr_words)):
            if dic.get(arr_pattern[i]) is None:
                dic[arr_pattern[i]] = arr_words[i]
            else:
                if dic[arr_pattern[i]] != arr_words[i]:
                    return False

        return True
