import random
import requests
import timer


class Request(object):

    req_tiemr = None

    def __init__(self):
        self.session = requests.Session()
        self.agents = []
        self.timer = timer.Timer()

    def set_sleep_range(self, min_time=1, max_time=5):
        self.timer.min_time = min_time
        self.timer.max_time = max_time

    def get(self, url):
        @timer.run(self.timer)
        def _get(url):
            """Get request.

            :param str url: access url

            :return: requests object (http response data)
            """
            self.__rewrite_session()
            return self.session.get(url)
        return _get(url)

    def __rewrite_session(self):
        if self.agents:
            header = self.session.headers
            header['User-Agent'] = self.__load_agent()
            self.session.headers = header

    def __load_agent(self):
        random.seed()
        return random.choice(self.agents)

if __name__ == '__main__':
    req = Request()
    req.agents = [
        ('Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like '
         'Gecko) Chrome/46.0.2486.0 Safari/537.36 Edge/13.10586'),
        ('Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like '
         'Gecko) Chrome/51.0.2704.103 Safari/537.36')]
    print req.get('http://133.242.129.45/')
    print req.get('http://133.242.129.45/')
