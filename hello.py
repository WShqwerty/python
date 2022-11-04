import os
from urllib import request


print("hello")
print("do test git!")
print("do test commit!")

# vscode使用git，需要commit 然后push就可以上传到github
 
def math_add(n,m):
  return n+m+n*m*m


def url_work():
  print("start work!")
  url = "https://www.top250.com"

  data = request.urlopen(url)
  print(data.read())

 
if __name__ == "__main__":
  print(math_add(1,2))
  print("hello")

  print("hello!")
  url_work()
