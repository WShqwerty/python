from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import mysql.connector

List_youtube = []

def web_work():
    try:
        driver = webdriver.Chrome()

        driver.get('https://www.youtube.com')

        titles_get = driver.find_elements(By.ID, "video-title-link")
        sleep(1)
        
        for title_get in titles_get:
            youtube = {
                "title": title_get.get_attribute("title"), 
                "href" : title_get.get_attribute("href")
            }
            # print(youtube)
            List_youtube.append(youtube)
    finally:
        driver.quit()


def sql_work():
    try:
        mydb = mysql.connector.connect(
            host = "localhost",
            user = "root",
            passwd = "Wsh.123456",
            database = "work_test1",
            auth_plugin = "mysql_native_password"
        )

        mycursor = mydb.cursor()

        for i in List_youtube:
            print(i['title'])
            sql = "insert into youtube (title, href) values (%s, %s)"
            val = (i["title"], i["href"])
            # print("done")
            mycursor.execute(sql, val)
            mydb.commit()
        print("done")
    finally:
        mycursor.close()
        mydb.close()

if __name__ == "__main__":
    web_work()
    sql_work()