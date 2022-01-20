#3010 W22
#yunas magsi - 101115159


from time import sleep

sense = SenseHat()

red = (255, 0, 0)
blue = (0, 0, 255)
speed = 0.5

while True:
    sense.show_message("Yunas Magsi", text_colour =red, back_colour = blue, scroll_speed = speed)
    sleep(1)
