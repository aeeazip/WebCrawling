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

with open(r'C:\Users\cheaw\Desktop\data_clean.csv', 'r', encoding='utf-8') as f:
    csvreader = csv.DictReader(f, delimiter=';')
    for row in csvreader:
        for key, value in row.items():
            if key == "image_urls":
                image_urls = value
            elif key == "name":
                name = value
            elif key == "gender":
                gender = value
            elif key == "group":
                group = value
            elif key == "main_accords":
                main_accords = value
            elif key == "top":
                top = value
            elif key == "middle":
                middle = value
            elif key == "base":
                base = value

        
        # Perfume_Category에 group값 있는지 검사해서 없으면 삽입
        try:
            cur.execute('insert into Perfume_Category(name) values(%s)', group)
            conn.commit()
        except:
            pass
        
        # Perfume 테이블 삽입
        try:
            sql="insert into Perfume(perfume_name, perfume_img, perfume_gender, perfume_group) VALUES(%s, %s, %s, %s)"
            cur.execute(sql, (name, image_urls, gender, group))
            conn.commit()
        except:
            pass
            
        # Perfume_Top Middle Base 넣기
        # Top Middle Base 나눠지지 않은 경우(None_Note에 삽입)
        if middle=="" or base=="":
            list = top.split(',')
            for x in list:            
                try:                    
                    cur.execute('insert into Perfume_Scent(name) VALUES(%s)', x)
                    conn.commit()
                except:
                    pass

                #excuteQuery
                try:
                    sql = "select id from Perfume_Scent where name=%s"
                    cur.execute(sql, x)
                    scent_id = cur.fetchone()
                    conn.commit()
                    
                    sql = "select perfume_id from Perfume where perfume_name=%s"
                    cur.execute(sql, name)
                    perfume_id = cur.fetchone()
                    conn.commit()
                    
                    sql = "insert into Perfume_None_Note(Perfume_Scent_id, Perfume_perfume_id) values(%s, %s)"
                    cur.execute(sql, (scent_id[0], perfume_id[0]))
                    conn.commit()
                except:
                    pass
                
        # Top Middle Base 나눠진 경우
        else:
            list = top.split(',')
            for x in list:            
                try:                    
                    cur.execute('insert into Perfume_Scent(name) VALUES(%s)', x)
                    conn.commit()
                except:
                    pass

                #excuteQuery
                try:
                    sql = "select id from Perfume_Scent where name=%s"
                    cur.execute(sql, x)
                    scent_id = cur.fetchone()
                    conn.commit()

                    sql = "select perfume_id from Perfume where perfume_name=%s"
                    cur.execute(sql, name)
                    perfume_id = cur.fetchone()
                    conn.commit()

                    sql = "insert into Perfume_Top(Perfume_Scent_id, Perfume_perfume_id) values(%s, %s)"
                    cur.execute(sql, (scent_id[0], perfume_id[0]))
                    conn.commit()
                except:
                    pass

            list1 = middle.split(',')
            for x in list1:            
                try:                    
                    cur.execute('insert into Perfume_Scent(name) VALUES(%s)', x)
                    conn.commit()
                except:
                    pass

                #excuteQuery
                try:                   
                    sql = "select id from Perfume_Scent where name=%s"
                    cur.execute(sql, x)
                    scent_id = cur.fetchone()
                    conn.commit()

                    sql = "select perfume_id from Perfume where perfume_name=%s"
                    cur.execute(sql, name)
                    perfume_id = cur.fetchone()
                    conn.commit()

                    sql = "insert into Perfume_Middle(Perfume_Scent_id, Perfume_perfume_id) values(%s, %s)"
                    cur.execute(sql, (scent_id[0], perfume_id[0]))
                    conn.commit()
                except:
                    pass

            list2 = base.split(',')
            for x in list2:            
                try:                    
                    cur.execute('insert into Perfume_Scent(name) VALUES(%s)', x)
                    conn.commit()
                except:
                    pass

                #excuteQuery
                try:                   
                    sql = "select id from Perfume_Scent where name=%s"
                    cur.execute(sql, x)
                    scent_id = cur.fetchone()
                    conn.commit()

                    sql = "select perfume_id from Perfume where perfume_name=%s"
                    cur.execute(sql, name)
                    perfume_id = cur.fetchone()
                    conn.commit()

                    sql = "insert into Perfume_Base(Perfume_Scent_id, Perfume_perfume_id) values(%s, %s)"
                    cur.execute(sql, (scent_id[0], perfume_id[0]))
                    conn.commit()
                except:
                    pass

conn.close()


                
