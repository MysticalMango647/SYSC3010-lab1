# Write your code here :-)
from sense_hat import SenseHat
from time import sleep


def get_sensehat():
    sense = SenseHat()
    return(sense)



def alarm(sense, flash_time):
    decrement = 1
    totalTime = flash_time
    red = (255, 0, 0)
    blank = (0,0,0)
    while (totalTime >=0):
        sense.clear(red)
        totalTime -= decrement
        sleep(1)
        sense.clear(blank)
        totalTime -= decrement
        sleep(1)
