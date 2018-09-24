from picamera import PiCamera
from time import sleep
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(18,GPIO.OUT)


while True: 
	while GPIO.input(4) == GPIO.HIGH:
		time.sleep(.1)
	#GPIO.wait_for_edge(4, GPIO.FALLING)
	camera = PiCamera()
	camera.resolution = (640, 480)
	print("PiCamera loaded.. . warming camera")
	time.sleep(2)
	camera.start_preview()
	camera.start_recording('/home/pi/dashcam/video/record.h264')
	print("PiCamera started recording")

	cnt = 0
	while GPIO.input(4) == GPIO.HIGH:
		time.sleep(.1)
		if cnt < 10:
			print("LED on")
			GPIO.output(18, GPIO.HIGH)
		elif cnt < 20:
			print("LED off")
			GPIO.output(18, GPIO.LOW)
		cnt += 1
		if cnt >= 20:
			cnt = 0

	camera.stop_recording()
	GPIO.output(18, GPIO.LOW)
	print("PiCamera stopped recording")

	camera.stop_preview()
	camera.close()
	time.sleep(1)
