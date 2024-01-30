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
        postfix_expr: str
        for i, c in enumerate(dict_expr):
            print(c, i)
            if i == 0:
                postfix_expr = c + " "
            if c.isnumeric():
                postfix_expr += dict_expr + " "

                




s = Calculator()
print(s.to_postfix("1 + 2 + 3"))
