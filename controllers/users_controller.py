from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash ,check_password_hash
from helpers.db_connection import get_db_connection
import aiomysql



users_controller = Blueprint('users_controller', __name__)


# API: Sign Up
@users_controller.route('/signUp', methods=['POST'])
async def signUp():
    data = request.get_json()

    # Extract validated data
    first_name = data.get('first_name')
    last_name = data.get('last_name')
    password = data.get('password')
    email = data.get('email')
    team_role = data.get('team_role')

    # Connect to the database
    db =await get_db_connection()
    try:
        async with db.cursor(aiomysql.DictCursor) as cursor:
            #Check if Email already exists
            check_email_sql = "SELECT * FROM users WHERE email = %s"
            await cursor.execute(check_email_sql, (email,))
            existing_user = await cursor.fetchone()

            if existing_user:
                return jsonify({"error": "Email is already in use"}), 400
            
            # Hash the password
            hashed_password = generate_password_hash(password)

            # Insert new user into the database
            insert_user_sql = """
                INSERT INTO users (first_name, last_name, email, password, team_role) 
                VALUES (%s, %s, %s, %s, %s)
            """
            await cursor.execute(insert_user_sql, (first_name, last_name, email, hashed_password, team_role))
            await db.commit()

        return jsonify({"message": "User registered successfully!"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# API: Sign In
@users_controller.route('/signIn', methods=['POST'])
async def signIn():
    data = request.get_json()
    
    # Extract validated data
    email = data.get('email')
    password = data.get('password')

    # Connect to the database
    db = await get_db_connection()
    try:
        async with db.cursor(aiomysql.DictCursor) as cursor:


            #Check if Email Not exists
            check_email_sql = "SELECT * FROM users WHERE email = %s"
            await cursor.execute(check_email_sql, (email,))
            existing_user = await cursor.fetchone()

            if not existing_user:
                return jsonify({"error": "Email does not exist"}), 400

            # Verify the password
            if not check_password_hash(existing_user['password'], password):
                return jsonify({"error": "Incorrect password"}), 400
            
            # Update user status to 'online'
            update_status_sql = "UPDATE users SET status = 'online' WHERE user_id = %s"
            await cursor.execute(update_status_sql, (existing_user['user_id'],))
            await db.commit()

            return jsonify({"message": 'Done' }), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500    
    


# API: Sign Out
@users_controller.route('/signOut/<int:id>', methods=['POST'])
async def sign_out(id):
    db = await get_db_connection()
    try:
        async with db.cursor(aiomysql.DictCursor) as cursor:

            #Check if Email Not exists
            check_email_sql = "SELECT * FROM users WHERE user_id = %s"
            await cursor.execute(check_email_sql, (id,))
            existing_user = await cursor.fetchone()

            if not existing_user:
                return jsonify({"error": "ID does not exist"}), 400

            
            # Update user status to 'offline'

            update_status_sql = "UPDATE users SET status = 'offline' WHERE user_id = %s"
            await cursor.execute(update_status_sql, (existing_user['user_id'],))
            await db.commit()

            return jsonify({"message": "User successfully signed out."}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500    




# API: Update User (cannot update email or ID)
@users_controller.route('/updateUser', methods=['PUT'])
async def updateUser():

    data = request.get_json()

    
    # Extract validated data
    first_name = data.get('first_name')
    last_name = data.get('last_name')
    team_role = data.get('team_role')
    user_id = data.get('user_id')

    db = await get_db_connection()

    # Check if user exists
    try:
        async with db.cursor(aiomysql.DictCursor) as cursor:


            check_user_sql = "SELECT * FROM users WHERE user_id = %s"
            await cursor.execute(check_user_sql, (user_id,))
            existing_user = await cursor.fetchone()

            if not existing_user:
                return jsonify({"error": "User not found"}), 404

            # Update user information
            update_sql = """
                UPDATE users 
                SET first_name = %s, last_name = %s, team_role = %s
                WHERE user_id = %s
            """
            await cursor.execute(update_sql, (first_name, last_name, team_role, user_id))
            await db.commit()  

            return jsonify({"message": "User updated successfully"}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500
    

