class MyRange:
    def __init__(self, x, y=None, step=1):
        if step == 0:
            raise ValueError('MyRange() arg 3 must not be zero')
        else:
            self.__step = step

        if y is None:
            self.__start, self.__stop = 0, x
        else:
            self.__start, self.__stop = x, y

    def __next__(self):
        ret = self.__start
        self.__start += self.__step

        if self.__step > 0 and ret < self.__stop\
                or self.__step < 0 and ret > self.__stop:
            return ret
        else:
            raise StopIteration

    def __iter__(self):
        return self


for i in MyRange(5):
    print(i, end=' ')
print()

for i in MyRange(1, 7):
    print(i, end=' ')
print()

for i in MyRange(2, 11, 2):
    print(i, end=' ')
print()

for i in MyRange(10, 1, -1):
    print(i, end=' ')
print()

# for i in MyRange(1, 5, 0):
#     print(i, end=' ')
# print()