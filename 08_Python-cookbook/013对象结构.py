
class  ARI:
    def __init__(self, a1, b1):
        self.a1 = a1
        print(a1)
        self.b1 = b1
        print(b1)

    def sumx(self, a2, b2):
        self.a2 = a2
        self.b2 = b2
        total1 = a2 + b2
        return total1

    def subx(self, a3, b3):
        self.a3 = a3
        self.b3 = b3
        sub1 = a3 - b3
        return sub1

    def mulx(self):
        mul1 = self.a1 * self.b1
        return mul1

    def divx(self):
        div1 = self.a1 / self.b1
        return div1

aaa = ARI(50,10)
print(aaa.sumx(50, 5))
print(aaa.mulx())
print(aaa.divx())
print(aaa.subx(30,12))