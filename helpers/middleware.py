# import jwt
# from flask import request
# from helpers.db_connection import get_db_connection
# import aiomysql

# # Secret key for JWT
# SECRET_KEY = 'VGX'


# async def verify_token():
#     token = request.headers.get('token')  
#     db = await get_db_connection()
#     if not token:
#         return None, "Token is missing", 401

#     try:
#         data = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
#         user_id = data['user_id']

#         async with db.cursor(aiomysql.DictCursor) as cursor:
#             check_user_sql = "SELECT * FROM users WHERE user_id = %s AND status = 'online'"
#             await cursor.execute(check_user_sql, (user_id,))
#             user = await cursor.fetchone()


#             if not user:
#                 return None, "User not found or not online", 401

#         return user, None, None 
#     except jwt.ExpiredSignatureError:
#         return None, "Token has expired", 401
#     except jwt.InvalidTokenError:
#         return None, "Invalid token", 401
#     except Exception as e:
#         return None, str(e), 500
