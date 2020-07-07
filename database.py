import mysql.connector

def DataUpdate(ids,days):
    mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        passwd = "root",
        database = "Leave_Application",
        auth_plugin = 'mysql_native_password'

    )

    mycursor = mydb.cursor()

    #sql = "CREATE TABLE Leave_Data(ID VARCHAR(10),No_of_Leaves VARCHAR(2));"


    sql = 'INSERT INTO Leave_Data(ID,No_of_Leaves) VALUES ("{0}","{1}");'.format(ids,days);
    mycursor.execute(sql)
    mydb.commit()
    print(mycursor.rowcount,"record inserted")

if __name__=="__main__":
    DataUpdate("106","10")
