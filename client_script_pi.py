import socket
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(4,GPIO.IN)

while True:
        if GPIO.input(4)== 1:

                s = socket.socket()
                host = "server_address"
                port = 12345

                s.connect((host, port))
                print s.recv(1024)
                while True:
                        i=1
                        f = open('med_names'+ str(i)+".txt",'wb')
                        i=i+1
                        while (True):
                        # receive and write file
                                l = s.recv(1024)
                                while (l):
                                        f.write(l)
                                        l = s.recv(1024)
                                        print "file received"
                                        s.send('file received')
                                s.close()
                                f.close()