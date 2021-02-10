"""
Создать класс декоратор (DecorTimeCrit) класса.
Декоратор, который измеряет время выполнения каждого метода, и печатает предупреждение, 
только если время выполнения было больше критического (параметр critical_time)
"""



# from time import time, sleep

# @DecorTimeCrit(critical_time=0.45)
# class Test:
#     def method_1(self):
#         print('slow method start')
#         sleep(1)
#         print('slow method finish')

#     def method_2(self):
#         print('fast method start')
#         sleep(0.1)
#         print('fast method finish')


# t = Test()

# t.method_1()
# t.method_2()

import time
# while True:
#     try:
#         critical_time = float(input('Введите критическое значение измерения (например 0.45): '))
#     except ValueError:
#         critic = float(input('Введите критическое значение измерения (например 0.45): '))
check_critic = input('Введите критическое значение измерения (например 0.45): ')
if check_critic == check_critic.isnumeric():
    critical_time = check_critic

def DecorTimeCrit(cls,critical_time=0.45):
    class NewCls:
        def __init__(self, *args, **kwargs):
            self._obj = cls(*args, **kwargs)

        def __getattribute__(self, s):
            try:
                x = super().__getattribute__(s)
            except AttributeError:
                pass
            else:
                return x
            attr = self._obj.__getattribute__(s)

            if isinstance(attr, type(self.__init__)):
                return time_(attr,critical_time)
            else:
                return attr
    return NewCls


def time_(method,critical):
    def timed(*args, **kwargs):
        ts = time.time()
        print_res = method(*args, **kwargs)
        te = time.time()
        delta = (te - ts) * 1000
        if delta > critical:
            print(f'Осторожно!!!!!{method.__name__} выполнялся {delta:2.2f} ms')
        else:
            print(f'{method.__name__} выполнялся {delta:2.2f} ms')
        return print_res
    return timed


@DecorTimeCrit
class Test:
    def method_1(self):
        print("медленный метод начался")
        time.sleep(1.0)
        print("медленный метод кончился")
    def method_2(self):
        print("быстрый метод начался")
        time.sleep(0.1)
        print("быстрый метод кончился")


t = Test()
t.method_1()
t.method_2()

