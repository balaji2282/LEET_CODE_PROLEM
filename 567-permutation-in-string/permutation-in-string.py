class Solution:
    def checkInclusion(self, s1, s2):
        if len(s1) > len(s2):
            return False

        s1_count = [0] * 26
        window = [0] * 26

        # Build frequency arrays
        for i in range(len(s1)):
            s1_count[ord(s1[i]) - ord('a')] += 1
            window[ord(s2[i]) - ord('a')] += 1

        # Check first window
        if s1_count == window:
            return True

        # Slide the window
        for i in range(len(s1), len(s2)):
            window[ord(s2[i]) - ord('a')] += 1
            window[ord(s2[i - len(s1)]) - ord('a')] -= 1

            if window == s1_count:
                return True

        return False