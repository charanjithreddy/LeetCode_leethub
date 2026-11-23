class ProductOfNumbers:

    def __init__(self):
        self.pre = [1]

    def add(self, num) :
        if num == 0:
            self.pre = [1]
        else:
            self.pre.append(self.pre[-1] * num)

    def getProduct(self, k):
        n = len(self.pre) - 1
        if k > n:
            return 0
        return self.pre[n] // self.pre[n - k]