class Solution:
    '''
    Runtime: O(n) - 2 pass
    Space: O(n) - stack
    '''
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        ans = []
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            elif s[i] == ')':
                if len(stack) and s[stack[-1]] == '(':
                    stack.pop()
                else:
                    stack.append(i)
        for i in range(len(s)):
            if len(stack):
                if i == stack[0]:
                    stack.pop(0)
                else:
                    ans.append(s[i])
            else:
                ans.append(s[i])
        return ''.join(ans)
                
                
