import mysql.connector


conn = mysql.connector.connect(
    host = 'localhost',
    user = 'maya',
    password = 'Dahab2024$',
    database = 'task_manger'
)


def insertTask(conn,created_by,assigned_to,header,description,status):
    mycursor = conn.cursor()
    sql = 'INSERT INTO cards (created_by,assigned_to,header,description,status) VALUES (%s,%s,%s,%s,%s);'
    val = (created_by,assigned_to,header,description,status)
    mycursor.execute(sql,val)
    conn.commit()
    print(mycursor.rowcount, 'taskinserted')


