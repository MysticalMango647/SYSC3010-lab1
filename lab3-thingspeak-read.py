import requests
from sense_hat import SenseHat
from time import sleep

sense = SenseHat()

#used my own api, but it works at display results and printing on sense hat
readKey = "Q59OBKU9M27XT49P"
channelNumber = "1640372"
url = "https://api.thingspeak.com/channels/" + channelNumber +"/feeds.json"
results = 5
red = (255, 0, 0)
blue = (0, 0, 255)
speed = .25
#GET https://api.thingspeak.com/channels/1640372/feeds.json?api_key=Q59OBKU9M27XT49P&results=2
def main():
    # payload includes the headers to be sent with the GET request
    # read the documentation for more information (https://docs.pythonrequests.org)
    payload = {'api_key': readKey, 'results': results}
    # Sends an HTTP GET request
    response = requests.get(url, params=payload)
    response = response.json()
    print("Channel Name: {}".format(response['channel']['name']))

    entries = response['feeds']
    # Print out the temperature at each entry's time
    for e in entries:
        print("At {}, the temperature was {}".format(e['created_at'],e['field1']))
        sense.show_message("temperature {}".format(e['field1']), text_colour =red, back_colour = blue, scroll_speed = speed)
        print("At {}, the humidity was {}".format(e['created_at'],e['field2']))
        sense.show_message("humidity {}".format(e['field2']), text_colour =red, back_colour = blue, scroll_speed = speed)
        print("At {}, the pressure was {}".format(e['created_at'],e['field3']))
        sense.show_message("pressure {}".format(e['field3']), text_colour =red, back_colour = blue, scroll_speed = speed)
        

if __name__ == "__main__":
    main() 
    
