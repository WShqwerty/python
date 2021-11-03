from urllib import request
import mysql.connector

def url_baidu():
    url = 'https://www.baidu.com'
    data = request.urlopen(url)
    print(data.read())

def add(a, b):
    return a+b


if __name__ == "__main__":
    print('hello world!')
    print(f'num = {add(3, 4)}')
    # url_baidu()
 