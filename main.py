from cgitb import text
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import connectionSetting
import pymysql

setting = connectionSetting.info
#connection setting
conn = pymysql.connect(
    db=setting['db'],
    host=setting['host'],
    user=setting['user'],
    passwd=setting['passwd'],
    port=setting['port'],
    charset=setting['charset']
)
#cursor
cur = conn.cursor()

driver = webdriver.Chrome()
driver.get("https://www.fragrantica.com/notes/")

#open the file for write operation
f = open('notes.txt' , 'w')

time.sleep(5)
notes = driver.find_elements(By.CLASS_NAME, 'notebox')
for note in notes:
    try:
        text = note.text
        f.write(text)
        f.write("\n")
        #excuteQuery
        cur.execute('INSERT INTO Perfume_Scent(name) VALUES(%s)', text)
        conn.commit()
    except:
        pass


conn.close()
f.close()
driver.close()


