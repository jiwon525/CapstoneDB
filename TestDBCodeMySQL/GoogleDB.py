
import mysql.connector
from mysql.connector import Error

import pandas as pd
empdata = pd.read_csv('C:\\Users\\huiyi\\Downloads\\Year 3-Poly\\Sem 3.2 Capstone\\CollatedCalendarData.csv', index_col=False, delimiter = ',')
empdata.head()

'''def connection_To_DB():
    try:
        connection = mysql.connector.connect(host='localhost',
                                            database='GoogleCal_db',
                                            user='root',
                                            password='root')
        if connection.is_connected():b  
            db_Info = connection.get_server_info()
            print("Connected to MySQL Server version ", db_Info)
            cursor = connection.cursor()
            cursor.execute("select database();")
            record = cursor.fetchone()
            print("You're connected to database: ", record)

    except Error as e:
        print("Error while connecting to MySQL", e)
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")'''

def CreateEvents_DB():
    try:
        conn = mysql.connector.connect(host='localhost',
                                        database='GoogleCal_db',
                                        user='root',
                                        password='root')
        if conn.is_connected():
            cursor = conn.cursor()
            cursor.execute("select database();")
            record = cursor.fetchone()
            print("You're connected to database: ", record)

            #Code to test out
            cursor.execute('DROP TABLE IF EXISTS AllInOne;')
            print("Creating table...")
            # in the below line please pass the create table statement which you want #to create
            cursor.execute("CREATE TABLE AllInOne(CalendarID varchar(5), EventID varchar(20), StartDate date, EndDate date, Continuous bool, Start2End varchar(20), AddInfo VARCHAR(100), Trainer varchar(20), MTrainer varchar(30), Location varchar(30), MinClass int, Flag bool, StartTime time, EndTime time, Duration time, ProgramID varchar(10), ProgramName varchar(50))")
            conn.commit()
            print("Table is created....")
            for row in empdata.iterrows():
                #here %S means string values 
                sql = "INSERT INTO GoogleCal_db.Program VALUES (%s,%s,%x,%x,%d,%s,%s,%s,%s,%s,%d,%d,%X,%X,%X,%s,%s)"
                cursor.execute(sql, tuple(row))
                print("Record inserted")
                # the connection is not auto committed by default, so we must commit to save our changes
                conn.commit()
            
    except Error as e:
        print("Error while connecting to MySQL", Error)

CreateEvents_DB()

