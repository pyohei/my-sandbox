from request import Request
from lxml import etree

REQ = 'https://www.google.co.jp/search?hl=ja&tbm=shop&tbs=vw:l&q=4972883116306'


def main():
    req = Request()
    req.agents = [
        ('Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like '
         'Gecko) Chrome/46.0.2486.0 Safari/537.36 Edge/13.10586'),
        ('Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like '
         'Gecko) Chrome/51.0.2704.103 Safari/537.36')]
    response = req.get(REQ)
    print __parse(response.text)


def __parse(text):
    et = etree.fromstring(text, parser=etree.HTMLParser())
    for e in et.xpath("//a[@class='pstl']"):
        suffix = e.attrib['href']
        url = REQ + suffix
        req = Request()
        req.agents = [
            ('Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like '
             'Gecko) Chrome/46.0.2486.0 Safari/537.36 Edge/13.10586'),
            ('Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like '
             'Gecko) Chrome/51.0.2704.103 Safari/537.36')]
        response = req.get(url)
        et2 = etree.fromstring(response.text, parser=etree.HTMLParser())


if __name__ == '__main__':
    main()
