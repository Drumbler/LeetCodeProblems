class Calculator:
    operationPriority = [
        {'(', 0},
        {'+', 1},
        {'-', 1},
        {'*', 2},
        {'/', 2},
        {'^', 3},
        {'~', 4}
    ]

    def generate_tokens(self, expr):
        dict_expr = expr.split(" ")
        return dict_expr

    def to_postfix(self, dict_expr):
        stack = []
        postfix_expr = ""
        for i, c in enumerate(dict_expr):
            print(c, i)
            if c.isnumeric():
                postfix_expr += c + " "
            elif (c == '('):
                stack.append(c)
            elif (c == ')'):
                while len(stack) > 0 & stack[0] != '(':
                    postfix_expr += stack.pop(0)
                    print(len(stack))
            elif c in s.operationPriority:
                
                

                

        print(postfix_expr)

                




s = Calculator()

print(s.to_postfix("1 + 2 + 3"))
