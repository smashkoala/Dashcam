#!/usr/bin/env python

import RPi.GPIO as GPIO
import subprocess

#GPIO.setmode(GPIO.BCM)
#GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_UP)
#GPIO.wait_for_edge(4, GPIO.FALLING)

subprocess.call(['python','/home/pi/dashcam/preview.py'], shell=False)
