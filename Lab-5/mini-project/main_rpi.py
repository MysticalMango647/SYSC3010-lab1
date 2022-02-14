#!/usr/bin/env python
from helper_functions import camera
from helper_functions import sensehat
from helper_functions import computer_vision
import time


def main():
    camera_i = camera.get_camera()
    sense = sensehat.get_sensehat()
    print("Enter 1 if image is already saved, Enter 2 to take image")

    take_background_image = input()

    if take_background_image == "2":
        preview = False
    countdown = 0
    for i in range(10, 1, -1):
        print(i)

    camera.capture_image(camera_i, "images/background.jpg",
                         countdown_time=countdown, preview=preview)

    arm_system = input("Would you like to arm the system? y/n \n")
    if arm_system == "y":
        # TO-DO: Should be a user input
        interval = int(input("Enter interval:"))
        t1 = int(input("Enter threshold(keep it somewhere between 30 and 45 for best results:"))  # TO-DO: Should be a user input
        print("Monitoring will begin in:")
        for i in range(10, 1, -1):
            print(i)
        count = 0;
        while True:  # DO NOT MODIFY, function call must work as is
            # DO NOT MODIFY, function call must work as is
            camera.capture_image(
                camera_i, "images/images%s.jpg" % count, countdown_time=interval)
            person_detected = computer_vision.person_detected(
                "images/background.jpg", "images/images%s.jpg" % count, t1)  # DO NOT MODIFY, function call must work as is
            if person_detected:  # DO NOT MODIFY, function call must work as is
                # DO NOT MODIFY, function call must work as is
                print("Person Detected")
                # DO NOT MODIFY, function call must work as is
                sensehat.alarm(sense, interval)
            else:
                # DO NOT MODIFY, function call must work as is
                print("No Person Detected")
            count += 1


if __name__ == "__main__":
    main()