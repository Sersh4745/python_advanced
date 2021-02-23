from time import time, sleep


class DecorTimeCrit:
    def __init__(self, critical_time):
        self.critical_time = critical_time

    @staticmethod
    def benchmark(new_attr, attr, critical_time):
        def wrapper(*args, **kwargs):
            start = time()

            result = new_attr(*args, **kwargs)

            if time() - start > critical_time:
                print(f'Warninig! {attr} slow. Time {round((time() - start), 4)} sec')
            else:
                print(f'Time process {round((time() - start), 4)} sec')

            return result

        return wrapper

    def __call__(self, cls):
        for attr in dir(cls):
            if attr.startswith('__'):
                continue
            new_attr = getattr(cls, attr)
            if callable(new_attr):
                decor_metod = DecorTimeCrit.benchmark(new_attr, attr, self.critical_time)
                setattr(cls, attr, decor_metod)
        return cls


@DecorTimeCrit(critical_time=0.45)
class Test:
    def method_1(self):
        print('slow method start')
        sleep(1)
        print('slow method finish')

    def method_2(self):
        print('fast method start')
        sleep(0.1)
        print('fast method finish')


t = Test()
t.method_1()
t.method_2()