#Yunas Magsi
#exercise 3 section 2.2.3

###SQL Commands

#new version
#sqlite3 sensorDB.db
#BEGIN;
#CREATE TABLE temps (id INTEGER PRIMARY KEY, tdate DATE, ttime TIME, temperature REAL, humidity REAL, pressure REAL);
#COMMIT;

import time
from sense_hat import SenseHat
import sqlite3
import datetime
from time import sleep

dbconnect = sqlite3.connect("sensorDB.db");
dbconnect.row_factory = sqlite3.Row;
cursor = dbconnect.cursor();
sense = SenseHat()
sense.clear()
id =0
#variable delcaration



while True:
    d = datetime.datetime.now()
    t = sense.get_temperature()
    p = sense.get_pressure()
    h = sense.get_humidity()
    t = round(t, 1)
    p = round(p, 1)
    h = round(h, 1)
    id = id+1
    print(id,d,t,p,h)
    cursor.execute('''INSERT OR IGNORE INTO temps values (?,date('now'),time('now'),?,?,?)''',(id,t, h,p));
    dbconnect.commit();
    sleep(1)

