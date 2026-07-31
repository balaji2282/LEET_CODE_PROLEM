class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        from collections import Counter

        ans = []
        n = len(words)
        w = len(words[0])
        need = Counter(words)

        for i in range(len(s) - n * w + 1):
            temp = []

            for j in range(n):
                temp.append(s[i + j*w : i + (j+1)*w])

            if Counter(temp) == need:
                ans.append(i)

        return ans
        