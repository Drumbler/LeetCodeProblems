class numberComplement(object):
    def findComplement(self, num):
        comp = []
        while num:
            comp.append(num % 2)
            num = num // 2
        final = 0
        for i in range(len(comp) - 1, -1, -1):
            final = final * 2 + (1 - comp[i])
        return (final)


s = numberComplement()
print(s.findComplement(4))
