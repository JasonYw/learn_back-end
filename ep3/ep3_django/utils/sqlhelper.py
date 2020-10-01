import mysql.connector
from getpass import getuser
def get_list(sql,args=[]):
    try:
        if getuser() == "rico":
            connect =mysql.connector.connect(user="root",password="rico0125",database="django")
        else:
            connect =mysql.connector.connect(user="root",password="0125",database="django")
        cursor =connect.cursor()
        cursor.execute(sql,args)
        result =cursor.fetchall()
        connect.commit()
        connect.close()
        return result
    except Exception as e:
        print(e)
        return None

def modify(sql,args=[]):
    try:
        if getuser() =="rico":
            connect =mysql.connector.connect(user="root",password="rico0125",database="django")
        else:
            connect =mysql.connector.connect(user="root",password="0125",database="django")
        cursor =connect.cursor()
        cursor.execute(sql,args)
        connect.commit()
        connect.close()
        return True
    except Exception as e:
        print(e)
        return False

class SqlHelper(object):

    def __init__(self):
        if getuser() == "rico":
            self.connect =mysql.connector.connect(user="root",password="rico0125",database="django")
        else:
            self.connect =mysql.connector.connect(user="root",password="0125",database="django")
        self.cursor =self.connect.cursor()

    def get_list(self,sql,args=[]):
        try:    
            self.cursor.execute(sql,args)
            result =self.cursor.fetchall()
            return result
        except Exception as e:
            print(e)
            return None

    def modify(self,sql,args=[]):
        try:
            self.cursor.execute(sql,args)
            self.connect.commit()
            return True
        except Exception as e:
            print(e)
            return False

    def multiple_modify(self,sql,args=[]):
        try:
            self.cursor.executemany(sql,args)
            self.connect.commit()
            return True
        except Exception as e:
            print(e)
            return False
    
    def close(self):
        self.connect.close()