class main:
    def Palindrome(self,x,n) -> bool:
        x = int(input("Введите число"))
        x = str(x)
        n = x[::-1]
        if x == n:
            print("true")
        else:
            print("false")