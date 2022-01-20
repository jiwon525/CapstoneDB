from datetime import datetime, timedelta
from json.tool import main
import mysql.connector
from mysql.connector import Error

import pandas as pd
empdata = pd.read_csv('"C:\GO-Work\src\CapstoneDB\CollatedCalendarData.csv', index_col=False, delimiter = ',')
empdata.head()




def main():
    conn = mysql.connector.connect(host='localhost',
                                        database='GoogleCal_db',
                                        user='root',
                                        password='root')
    if conn.is_connected():
        cursor = conn.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("You're connected to database: ", record)
    else:
        print("not connected")
    file = ['CollatedCalendarData']
    df = pandas.read_excel(file)
    for row in range(len(df.index)):
        CalID = df.iloc[row]['CALENDAR_ID']
        CalName = df.iloc[row]['CALENDAR_NAME']
        EventT = df.iloc[row]['Event Title']
        startDate = df.iloc[row]['START DATE']
        startDate = datetime.strptime(startDate, "%d/%m/%Y")
        endDate = df.iloc[row]['END DATE']
        endDate = datetime.strptime(endDate, "%d/%m/%Y")
        startTime = df.iloc[row]['START TIME']
        startTime = datetime.strptime(startTime, "%-I/%-M/%-S")
        endTime = df.iloc[row]['END TIME']
        endTime = datetime.strptime(endTime, "%-I/%-M/%-S")
        duration = df.iloc[row]['Duration']
        duration = datetime.strptime(duration, "%-I/%-M/%-S")
        continuous = df.iloc[row]['Duration']
        trainer = df.iloc[row]['TRAINER']
        mTrainer = df.iloc[row]['MULTIPLE TRAINER']
        location = df.iloc[row]['LOCATION']
        eventDesc = df.iloc[row]['ADDITIONAL INFO TO DISPLAY AS NOTES']

        sql = ("INSERT INTO GoogleCal_db.Program VALUES (%s,%s,%s,%x,%x,%X,%X,%X,%s,%s,%s,%s)", CalID, CalName, EventT, startDate, endDate, startTime, endTime, duration, continuous, trainer, mTrainer,location, eventDesc)
        cursor.execute(sql, tuple(row))


'''def CreateEvents_DB():
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
            for i, row in empdata.iterrows():
                #here %S means string values 
                #starttime = dt.now()
                sql = "INSERT INTO GoogleCal_db.Program VALUES (%s,%s,%x,%x,%d,%s,%s,%s,%s,%s,%d,%d,%X,%X,%X,%s,%s)"
                cursor.execute(sql, tuple(row))
                print(sql)
                print("Record inserted")
                # the connection is not auto committed by default, so we must commit to save our changes
                conn.commit()
            
    except Error as e:
        print("Error while creating table or inserting records", Error)

CreateEvents_DB()'''