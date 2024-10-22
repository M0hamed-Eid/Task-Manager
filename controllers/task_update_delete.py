from flask import Blueprint, request, jsonify
from helpers.db_connection import get_db_connection
import aiomysql


tasks_controller = Blueprint('tasks_controller', __name__)

@tasks_controller.route('/updateTask', methods=['PUT'])
async def updateTask():
    """
    This api for updating tasks
    it get: card_id, header, status, description, assigned_to
    then searchs for task using card_id
    and change header, status, description, assigned_to
    Return: "Task not found", "Task updated successfully" or error
    """
    data = request.get_json()

    # Extract validated data
    header = data.get('header')
    description = data.get('description')
    status = data.get('status')
    assigned_to = data.get('assigned_to')
    card_id = data.get('card_id')

    db = await get_db_connection()

    # Check if task exists
    try:
        async with db.cursor(aiomysql.DictCursor) as cursor:


            check_task_sql = "SELECT * FROM cards WHERE card_id = %s"
            await cursor.execute(check_task_sql, (card_id,))
            existing_task = await cursor.fetchone()

            if not existing_task:
                return jsonify({"error": "Task not found"}), 404

            # Update task
            update_sql = """
                UPDATE cards 
                SET header = %s, description = %s, status = %s, assigned_to = %s
                WHERE card_id = %s
            """
            await cursor.execute(update_sql, (header, description, status, assigned_to, card_id))
            await db.commit()  

            return jsonify({"message": "Task updated successfully"}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500
    

@tasks_controller.route('/deleteTask', methods=['PUT'])
async def deleteTask():
    """
    This api deletes a task using card_id 
    
    Keyword arguments:
    argument -- cari_id
    Return: "Task not found", "Task deleted successfully!" or error
    """
    
    data = request.get_json()

    card_id = data.get('card_id')

    db = await get_db_connection()
    
    try:
        async with db.cursor(aiomysql.DictCursor) as cursor: 
            check_task_sql = "SELECT * FROM cards WHERE card_id = %s"
            await cursor.execute(check_task_sql, (card_id,))
            existing_task = await cursor.fetchone()

            if not existing_task:
                return jsonify({"error": "Task not found"}), 404

            delet_task_sql = "DELETE FROM cards WHERE card_id = %s"
            await cursor.execute(delet_task_sql, (card_id,))
            await db.commit()


        return jsonify({"message": "Task deleted successfully!"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500