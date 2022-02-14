from picamera import PiCamera
import time


def get_camera():
    camera = PiCamera()
    return (camera)


def camera_preview(camera, preview_time):
    camera.start_preview()
    sleep(preview_time)
    camera.stop_preview()


def rotate_camera(camera, degrees):
    camera.rotation = degrees


def capture_image(camera, image_out_location, countdown_time, preview=False):
    if (preview == True):
        camera.start_preview()
    else:
        camera.stop_preview()
    time.sleep(countdown_time)
    camera.capture(image_out_location)