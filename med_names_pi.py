import RPi.GPIO as GPIO
import subprocess, signal
import os

GPIO.setmode(GPIO.BCM)
GPIO.setup(4,GPIO.IN)

subprocess.call('python client_script.py', shell=True)
subprocess.Popen('processing-java --sketch=mednames --run', shell=True)

while True:
        try:
                if GPIO.input(4)== 1:
					p = subprocess.Popen(['ps', '-A'], stdout=subprocess.PIPE)
					out, err = p.communicate()
					for line in out.splitlines():
						if 'omxplayer' in line:
						pid = int(line.split(None, 1)[0])
						os.kill(pid, signal.SIGKILL)
                        subprocess.call('python client_script.py', shell=True)
                        subprocess.call('omxplayer waves.mp3', shell=True)
        except ValueError:
                print "Nothing to worry"