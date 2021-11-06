from urllib import request
from bs4 import BeautifulSoup

def url_baidu():
    url = 'https://www.baidu.com'
    data = request.urlopen(url)
    # print(data.read())
    soup = BeautifulSoup(data.read(), 'lxml')
    print(soup)

def add(a, b):
    return a+b


if __name__ == "__main__":
    print('hello world!')
    print(f'num = {add(3, 4)}')
    url_baidu()
 