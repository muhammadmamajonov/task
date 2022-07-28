import os
import pickle
import sqlite3

sqliteConnection = sqlite3.connect('db.sqlite3')
cursor = sqliteConnection.cursor()

apparatlar_id_list = []
sql = """
    Select apparat_id from main_apparat
    """
cursor.execute(sql)
apparatlar_id = cursor.fetchall()
cursor.close()

for apparat in apparatlar_id:
    apparatlar_id_list.append(apparat[0])

id = 1

cursor = sqliteConnection.cursor()

for filename in os.listdir('spot_cache_copy'):
    print(filename)
    with open(os.path.join("spot_cache_copy", filename), 'rb') as f:
        datas = pickle.load(f)
        for data in datas:
           if data:
            
            if data[0] in apparatlar_id_list:
                    print(data)
                    sql = f"""
                        INSERT INTO main_data(id, apparat_id, time) VALUES(?, ?, ?)
                        """
                    cursor.execute(sql, (id, data[0], data[3]))
                    sqliteConnection.commit()
                    id += 1
                    print(id)

    
cursor.close()
        

           