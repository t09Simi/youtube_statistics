import csv
import sqlite3


#open connection to database
conn =  sqlite3.connect('youtube_data.db')
cur = conn.cursor()

#drop the data from table
conn.execute('DROP TABLE IF EXISTS details')
print("Table dropped succcesfully")

#create table again
conn.execute('CREATE TABLE details(id INTEGER PRIMARY KEY AUTOINCREMENT, video_id TEXT , title TEXT, channel_title TEXT, views INTEGER)')
print("Table created succcesfully")

conn.execute('DROP TABLE IF EXISTS statistics')
print("Table dropped successfully")

conn.execute('CREATE TABLE statistics(id INTEGER PRIMARY KEY AUTOINCREMENT, details_id INTEGER, category_id INTEGER, comments_total INTEGER, likes INTEGER, dislikes INTEGER, date FLOAT, FOREIGN KEY(details_id) REFERENCES details(id))')
print("Table created successfully")
try:
    with open('data_of_gb_videos_category/GBvideos.csv', newline='',) as f:
        reader = csv.reader(f,delimiter=",")
        next(reader)
        for row in reader:
            print(row)

            video_id = row[0]
            title = row[1]
            channel_title = row[2]
            views = int(row[4])
        
            cur.execute('INSERT INTO details VALUES(NULL,?,?,?,?)',(video_id, title, channel_title, views ))
            conn.commit()
except FileNotFoundError as e:
    print("File not found error occurred") 
except:
    print("Some other error occured")
print("Data parsed for details table succcesfully")

try:
    with open('data_of_gb_videos_category/GBvideos.csv', newline='',) as f:
        reader = csv.reader(f,delimiter=",")
        next(reader)
        for row in reader:
            print(row)

            category_id = int(row[3])
            comments_total = int(row[7])
            likes = int(row[5])
            dislikes = int(row[6])
            date = float(row[8])
            details_id = cur.lastrowid

            cur.execute('INSERT INTO statistics VALUES(NULL,?,?,?,?,?,?)',(details_id, category_id, comments_total, likes, dislikes, date))
            conn.commit()
except FileNotFoundError as e:
    print("File not found error occurred") 
except:
    print("Some other error occurred")
finally:
    print("Data parsed for statistics table succesfully")
    conn.close()