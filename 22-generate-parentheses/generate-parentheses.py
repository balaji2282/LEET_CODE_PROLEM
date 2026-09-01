class Solution:
    def generateParenthesis(self, n):
        result = []

        def make(s, left, right):
            if len(s) == 2 * n:
                result.append(s)
                return

            if left < n:
                make(s + "(", left + 1, right)

            if right < left:
                make(s + ")", left, right + 1)

        make("", 0, 0)
        return result