from picamera import PiCamera
from time import sleep
from datetime import datetime

camera = PiCamera()
while True:
    camera.start_preview()
    sleep(5)
    now = datetime.now()
    date_time = now.strftime("%Y%m%d-%H%M%S")
    pic = "/home/pi/Projects/NightCrawler/pictures/" + date_time + ".jpg"
    camera.capture(pic)
    camera.stop_preview()
    sleep(300)
