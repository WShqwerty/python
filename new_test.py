from selenium import webdriver
from time import sleep

def main():
    print("hello")
    url = "https://www.google.com"
    try:
        driver = webdriver.Chrome()
        driver.get(url)
        sleep(2)

    finally:
        driver.close()
        driver.quit()


if __name__ == "__main__":
    main()

