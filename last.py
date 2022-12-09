import csv
import time
import connectionSetting
import pymysql

setting = connectionSetting.info

# connection setting
conn = pymysql.connect(
    db=setting['db'],
    host=setting['host'],
    user=setting['user'],
    passwd=setting['passwd'],
    port=setting['port'],
    charset=setting['charset']
)

# cursor
cur = conn.cursor()

# 경로 변경 필요
with open(r'C:\Users\cheaw\Desktop\data_clean.csv', 'r', encoding='utf-8') as f:
    csvreader = csv.DictReader(f, delimiter=';')
    for row in csvreader:
        for key, value in row.items():
            if key == "name":
                name = value
            elif key == "like_rating":
                like = value
            elif key == "voters":
                voters = value
        
        # Perfume 테이블 삽입
        try:
            sql="UPDATE Perfume SET perfume_like=%s where perfume_name=%s"
            cur.execute(sql, (like, name))
            conn.commit()

            sql="UPDATE Perfume SET perfume_voters=%s where perfume_name=%s"
            cur.execute(sql, (voters, name))
            conn.commit()
        except:
            break              



                
