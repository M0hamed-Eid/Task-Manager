
import aiomysql

async def get_db_connection():
    return await aiomysql.connect(
        host='localhost',
        port=3306,
        user='root',
        password='',
        db='task_manager',
        autocommit=True
    )

    


    