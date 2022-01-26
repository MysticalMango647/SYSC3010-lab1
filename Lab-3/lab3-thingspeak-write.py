from sense_hat import SenseHat
import requests
sendKey = "T76KD0FQ67S1H970"
url = "https://api.thingspeak.com/update"
def main():
    sense = SenseHat()
    temperature = sense.get_temperature()
    humidity = sense.get_humidity()
    pressure = sense.get_pressure()
    print(temperature)
    print(humidity)
    print(pressure)
 # payload includes the headers to be sent with the GET request
# read the documentation for more information (https://docs.pythonrequests.org)
    payload = {'field1': temperature,'field2': humidity,'field3': pressure, 'api_key': sendKey}
    #payload = {'field2': humidity, 'api_key': sendKey}
    #payload = {'field3': pressure, 'api_key': sendKey}
    try:
        # Sends an HTTP GET request
        response = requests.get(url, params=payload)
        # The library can also decode JSON responses
        response = response.json()
        print(response)
    except:
        print("Connection Failed")
if __name__ == "__main__":
    main() 