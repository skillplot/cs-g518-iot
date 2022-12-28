import cv2
import numpy as np
import os

os.chdir("/home/pi/opencv-3.3.0/data/haarcascades")
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('/home/pi/IOTProject/FaceRecognition/trainer/trainer.yml')
cascadePath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath);

font = cv2.FONT_HERSHEY_SIMPLEX

#iniciate id counter
id = 0

# names related to ids: example ==> KUNAL: id=1,  etc
names = ['None', 'Pratik', 'Piyush', 'Nandini', 'Raj', 'Jigyasa', 'Siddhart', 'Rishab', 'Saksham', 'Arun', 'Shardul', 'Revanth']






import RPi.GPIO as GPIO
import time
#from picamera import PiCamera
from time import sleep
GPIO.setmode(GPIO.BCM)
TRIG = 20
ECHO = 21
#camera = PiCamera()
while True:
    print("Distance Check")
    GPIO.setup(TRIG, GPIO.OUT)
    GPIO.setup(ECHO, GPIO.IN)
    GPIO.output(TRIG, False)
    print("Calming Down")
    time.sleep(0.2)
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)
    while GPIO.input(ECHO) == 0:
        pulse_start = time.time()
    while GPIO.input(ECHO) == 1:
        pulse_end = time.time()
    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration * 17150
    distance = round(distance, 2)
    print("distance:", distance, "cm")
    time.sleep(2)

    if 0 < distance < 20:
        # Initialize and start realtime video capture
        cam = cv2.VideoCapture(0)
        cam.set(3, 640) # set video widht
        cam.set(4, 480) # set video height

        # Define min window size to be recognized as a face
        minW = 0.1*cam.get(3)
        minH = 0.1*cam.get(4)

        while True:
            ret, img =cam.read()
            #img = cv2.flip(img, -1) # Flip vertically
            gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

            faces = faceCascade.detectMultiScale(
                gray,
                scaleFactor = 1.2,
                minNeighbors = 5,
                minSize = (int(minW), int(minH)),
            )

            for(x,y,w,h) in faces:
                cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)
                id, confidence = recognizer.predict(gray[y:y+h,x:x+w])

                # Check if confidence is less them 100 ==> "0" is perfect match
                if (confidence < 100):
                    id = names[id]
                    confidence = "  {0}%".format(round(100 - confidence))
                else:
                    id = "unknown"
                    confidence = "  {0}%".format(round(100 - confidence))

                cv2.putText(img, str(id), (x+5,y-5), font, 1, (255,255,255), 2)
                cv2.putText(img, str(confidence), (x+5,y+h-5), font, 1, (255,255,0), 1)

            cv2.imshow('camera',img)

            k = cv2.waitKey(10) & 0xff # Press 'ESC' for exiting video
            if k == 27:
                break

        # Do a bit of cleanup
        print("\n [INFO] Exiting Program and cleanup stuff")
        cam.release()
        cv2.destroyAllWindows()
        time.sleep(2)
        break
    time.sleep(2)






