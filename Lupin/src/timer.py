import functools
import random
import time


def run(timer):
    def _run(func):
        if timer and timer.pre_time:
            timer.sleep()

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            response = func(*args, **kwargs)
            timer.record()
            return response
        return wrapper
    return _run


class Timer(object):

    def __init__(self, min_time=1, max_time=5):
        self.min_time = min_time
        self.max_time = max_time
        self.pre_time = None

    def record(self):
        """Record current time."""
        self.pre_time = time.time()

    def sleep(self):
        sleep_time = 0
        if self.pre_time:
            _sleep_time = self.__fetch_sleep_time()
            sleep_time = _sleep_time - (time.time() - self.pre_time)
            if sleep_time < 0:
                sleep_time = 0
        print 'sleep time: {} sec.'.format(str(sleep_time))
        time.sleep(sleep_time)

    def __fetch_sleep_time(self):
        random.seed()
        return random.randint(self.min_time, self.max_time)
