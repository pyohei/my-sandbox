import copy
import random
import unittest
import time
from datetime import datetime
from sleeptimer import SleepTimer

class TestSleepTimer(unittest.TestCase):

    def setUp(self):
        random.seed()
        self.count = random.randrange(1, 10)
        self.sleep_timer = SleepTimer(self.count)
        self.wakeup_seconds = copy.deepcopy(self.sleep_timer.wakeup_seconds)

    def test_setup(self):
        self.assertIn(self.count, 
                      range(1, 10),
                      'Your count is {0}'.format(self.count))
        self.assertEqual(self.count, len(self.wakeup_seconds))
        print('Wakeup seconds are [{0}]. and sleep count is {1}'.format(
            ', '.join([str(n) for n in self.wakeup_seconds]),
            self.count))

    def test_sleep(self):
        for n in range(self.count):
            end_second = self.wakeup_seconds[n]
            self.sleep_timer.sleep()
            current_second = datetime.now().second
            self.assertTrue(
                current_second >= end_second, 
                'Current time is before end time' \
                'current={0} , estimation={1}'.format(current_second,
                                                      end_second))
        
    def test_simple_sleep(self):
        random.seed()
        sleep_seconds = random.sample(xrange(1, 20), 2)
        sleep_seconds.sort()
        min_sleep = sleep_seconds[0]
        max_sleep = sleep_seconds[1]
        t = time.time()
        self.sleep_timer.simple_sleep(min_sleep, max_sleep)
        diff = time.time() - t
        # print min_sleep, diff, max_sleep
        self.assertTrue(min_sleep <= diff <= max_sleep,
                        'Exceed your sleep time between {0} and {1}.'\
                        '({2})'.format(min_sleep, max_sleep, diff))
        

if __name__ == '__main__':
    unittest.main()
