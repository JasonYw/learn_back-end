import mysql.connector

def get_list(sql,args=[]):
    try:
        connect =mysql.connector.connect(user="root",password="0125",database="django")
        cursor =connect.cursor()
        cursor.execute(sql,args)
        result =cursor.fetchall()
        connect.commit()
        connect.close()
        return result
    except:
        return None

def modify(sql,args=[]):
    try:
        connect =mysql.connector.connect(user="root",password="0125",database="django")
        cursor =connect.cursor()
        cursor.execute(sql,args)
        connect.commit()
        connect.close()
        return True
    except:
        return False



