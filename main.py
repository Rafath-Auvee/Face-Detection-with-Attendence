import mysql.connector

conn = mysql.connector.connect(user='i8692629_wp1', password='U.5n6Kuwd4rzfoL8sN655', host='127.0.0.1', database='i8692629_wp1')

cursorObject = conn.cursor()
query = "SELECT  `email`, `user_id`,`guid` FROM `wp_wlsm_student_records` JOIN `wp_posts` on wp_wlsm_student_records.photo_id = `wp_posts`.ID"

cursorObject.execute(query)

data = cursorObject.fetchall()

print("Connection established to: ")

for x in data:
    print(x)

conn.close()