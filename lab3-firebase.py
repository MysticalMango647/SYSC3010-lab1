from sense_hat import SenseHat
import pyrebase
import random
import time
import requests
# Create new Firebase config and database object
config = {
"apiKey": "AIzaSyBmJkp2JwZrf7W664EAwSxtNOJh1rwhLNY",
"authDomain": "sysc3010lab3.firebaseapp.com",
"databaseURL": "https://sysc3010lab3-default-rtdb.firebaseio.com/",
"storageBucket": "sysc3010lab3.appspot.com"
}
firebase = pyrebase.initialize_app(config)
db = firebase.database()
dataTemp = "temperatureDb"
dataHum = "humidityDb"
dataPres = "pressureDb"

# Write random numbers to database

def main():
    #writeData()
    readData()


def writeData():
    key = 0
    while True:
        # I'm using dummy sensor data here, you could use your senseHAT
        #sensorData = random.random()
        sense = SenseHat()
        sense.clear()
        temperature = sense.get_temperature()
        humidity = sense.get_humidity()
        pressure = sense.get_pressure()
        temperature = round(temperature, 1)
        humidity = round(humidity, 1)
        pressure = round(pressure, 1)
        print(temperature)
        print(humidity)
        print(pressure)
        # Will be written in this form:
        {
        "piHat" : {
         "temperature" : temperature,
         "humidity" : humidity,
         "pressure" : pressure
        }
        }
        # Each 'child' is a JSON key:value pair
        db.child(dataTemp).child(key).set(temperature)
        db.child(dataHum).child(key).set(humidity)
        db.child(dataPres).child(key).set(pressure)
        key = key + 1
        time.sleep(3)


config2 = {
  "apiKey": "AIzaSyD6gk7l2MrnlXJclWrs3dZCdSwTb2xvcuI",
  "authDomain": "sysc3010lab3-5d3d2.firebaseapp.com",
  "databaseURL": "https://sysc3010lab3-5d3d2-default-rtdb.firebaseio.com/",
  "storageBucket": "sysc3010lab3-5d3d2.appspot.com"
}

firebase2 = pyrebase.initialize_app(config2)
db2 = firebase2.database()

dataset1 = "Temperature" 
dataset2 = "Humidity"
dataset3 = "Pressure"



def readData(): 
    # Returns the entry as an ordered dictionary (parsed from json)
    tempData = db2.child(dataset1).get()
    humData = db2.child(dataset2).get()
    presData = db2.child(dataset3).get()
    
    # Returns the dictionary as a list
    tempData_list = tempData.each()
    humData_list = humData.each()
    presData_list = presData.each()

    print("Parent Key: {}".format(tempData.key()))
    print("Parent Value: {}\n".format(tempData.val()))

    print("Parent Key: {}".format(humData.key()))
    print("Parent Value: {}\n".format(humData.val()))

    print("Parent Key: {}".format(presData.key()))
    print("Parent Value: {}\n".format(presData.val()))



if __name__ == "__main__":
    main() 