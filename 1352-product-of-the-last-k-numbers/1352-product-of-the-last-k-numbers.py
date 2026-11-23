class ProductOfNumbers:

    def __init__(self):
        self.prefix = [1]   # start with 1 to simplify division

    def add(self, num: int) -> None:
        if num == 0:
            self.prefix = [1]  # reset because any future product before this is invalid
        else:
            self.prefix.append(self.prefix[-1] * num)

    def getProduct(self, k: int) -> int:
        if k >= len(self.prefix):  
            return 0  # means zero was in the last k numbers
        return self.prefix[-1] // self.prefix[-1 - k]
