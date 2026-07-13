class Solution:
    def findAnagrams(self, s, p):
        if len(p) > len(s):
            return []

        p_count = [0] * 26
        window = [0] * 26
        result = []

        # Frequency of p and first window
        for i in range(len(p)):
            p_count[ord(p[i]) - ord('a')] += 1
            window[ord(s[i]) - ord('a')] += 1

        if p_count == window:
            result.append(0)

        # Sliding window
        for i in range(len(p), len(s)):
            window[ord(s[i]) - ord('a')] += 1
            window[ord(s[i - len(p)]) - ord('a')] -= 1

            if window == p_count:
                result.append(i - len(p) + 1)

        return result
        