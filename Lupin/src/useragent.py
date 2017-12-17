from request import Request
from lxml import etree


def main():
    req = Request()
    req.agents = [
        ('Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like '
         'Gecko) Chrome/46.0.2486.0 Safari/537.36 Edge/13.10586'),
        ('Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like '
         'Gecko) Chrome/51.0.2704.103 Safari/537.36')]
    response = req.get('http://utaukitune.ldblog.jp/archives/65696057.html')
    print __parse(response.text)


def __parse(text):
    et = etree.fromstring(text, parser=etree.HTMLParser())
    with open('agents.txt', 'w') as f:
        for e in et.xpath("//div[@class='article-body-inner']/text()"):
            awk_e = e.strip()
            if 'Mozilla' in awk_e:
                try:
                    f.write(awk_e)
                    f.write('\n')
                except UnicodeEncodeError as err:
                    print '[Ignore] {0}'.format(awk_e.encode('utf-8'))
                    print '  Debug: {0}'.format(err)


if __name__ == '__main__':
    main()
