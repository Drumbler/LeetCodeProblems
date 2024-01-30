class validParentheses(object):
    def isValid(self, s) -> bool:
        stack = []
        pairs = {')': '(', ']': '[', '}': '{'}
        for c in s:
            if c in pairs:
                if not stack:
                    return False
                if stack.pop() != pairs[c]:
                    return False
            else:
                stack.append(c)

        return not stack


s = validParentheses()
print(s.isValid(''))
