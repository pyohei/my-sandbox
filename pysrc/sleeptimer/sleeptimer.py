"""Sleep scheduler."""

from time import sleep
from datetime import datetime
import random

class SleepTimer(object):

    def __init__(self, wakeup_count=1):
        self.wakeup_count = wakeup_count
        self.start_second = 1
        self.end_second = 58
        self.interval = 2
        self.wakeup_seconds = self.__schedule()

    def sleep(self):
        wakeup_second = self.wakeup_seconds.pop(0)
        second = datetime.now().second
        # print wakeup_second, second
        if wakeup_second > second:
            sleep(wakeup_second-second)

    def simple_sleep(self, min_sleep, max_sleep):
        return
        sleep(random.choice(range(min_sleep, max_sleep)))

    def __schedule(self):
        random.seed()
        sleep_seconds = random.sample(
            xrange(self.start_second, self.end_second, self.interval), 
            self.wakeup_count)
        sleep_seconds.sort()
        return sleep_seconds
