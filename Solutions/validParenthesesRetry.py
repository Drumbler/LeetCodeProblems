def isValid(s: str) -> bool:
    stack = []
    pairs = {')': '(', ']': '[', '}': '{'}
    for bracket in s:
        if bracket in pairs:
            if not stack:
                return False
            if stack.pop() != pairs[bracket]:
                return False
        else:
            stack.append(bracket)
    return not stack


print(isValid('(){}[]'))
