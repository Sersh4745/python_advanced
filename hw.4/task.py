class Range:
    def __init__(self,stop,count = 0):
        self.stop = stop
        self.count = count

    def __iter__(self):
        return self

    def __next__(self):
        self.count += 1

        if self.count < self.stop:
            return self.count
        else:
            raise StopIteration


range = Range(10,-2)
# print(next(range))
# print(next(range))
# print(next(range))

for r in range:
    """ можем найти все не четные числа"""
    if r % 2 == 1:
        print(r,end=',')