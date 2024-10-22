from new_task3 import *

def validateParams(created_by,assigned_to,header,description,status):
    if created_by is None or created_by is not numeric:
        return False
    if assigned_to is None or assigned_to is not numeric:
        return False
    if header is None or header == '':
        return False
    if description is None or description == '':
        return False 
    if status is None or status == '':
        return False
    return True                    


