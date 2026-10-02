class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        abs = []
        curr = []
        def dfs(open,close):
            if open == 0 and close == 0:
                abs.append(''.join(curr))
                return 
            if open>0:
                curr.append('(')
                dfs(open - 1, close)
                curr.pop()
            if close>open:
                curr.append(')')
                dfs(open,close -1)
                curr.pop()
        dfs(n, n)
        return abs