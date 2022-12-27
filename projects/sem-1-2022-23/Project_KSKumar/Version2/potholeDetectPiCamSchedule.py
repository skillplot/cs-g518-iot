#importing necessary libraries
import cv2
import os
from picamera import PiCamera
import time
import os.path
import smtplib
import numpy as np
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

class Emailer:
    def sendmail(self, recipient, subject, content, image):

        #Create Headers
        emailData = MIMEMultipart()
        emailData['Subject'] = subject
        emailData['To'] = recipient
        emailData['From'] = GMAIL_USERNAME

        #Attach our text data
        emailData.attach(MIMEText(content))

        #Create our Image Data from the defined image
        imageData = MIMEImage(open(image, 'rb').read(), 'jpeg')
        imageData.add_header('Content-Disposition', 'attachment; filename="image.jpg"')
        emailData.attach(imageData)

        #Connect to Gmail Server
        session = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        session.ehlo()
        session.starttls()
        session.ehlo()

        #Login to Gmail
        session.login(GMAIL_USERNAME, GMAIL_PASSWORD)

        #Send Email & Exit
        session.sendmail(GMAIL_USERNAME, recipient, emailData.as_string())
        session.quit

def is_similar(img1, img2):
    #return list(img1.getdata()) == list(img2.getdata()):
    return (img1 == img2).all()

#time.sleep(15)
camera = PiCamera()

while(True):
    camera.capture('/home/pi/Images/pothole-main.jpg')
    roadImg = cv2.imread("/home/pi/Images/pothole-main.jpg") #image name
    roadImg = cv2.resize(roadImg,(600,360))
    roadCopyImg = roadImg.copy()

    #importing model weights and config file
    net = cv2.dnn.readNet('/home/pi/pothole-detectionTest/project_files/yolov4_tiny.weights', '/home/pi/pothole-detectionTest/project_files/yolov4_tiny.cfg')
    model = cv2.dnn_DetectionModel(net)
    model.setInputParams(scale=1 / 255, size=(416, 416), swapRB=True)
    classIds, scores, boxes = model.detect(roadImg, confThreshold=0.6, nmsThreshold=0.4)

    #detection 
    for (classId, score, box) in zip(classIds, scores, boxes):
        cv2.rectangle(roadImg, (box[0], box[1]), (box[0] + box[2], box[1] + box[3]),
                      color=(0, 255, 0), thickness=2)
     
    #cv2.imshow("pothole",roadImg)
    cv2.imwrite("/home/pi/Images/finalDetection"+".jpg",roadImg) #result name

    #Email Variables
    SMTP_SERVER = 'smtp.gmail.com' #Email Server (don't change!)
    SMTP_PORT = 587 #Server Port (don't change!)
    GMAIL_USERNAME = 'iotproject@gmail.com' #change this to match your gmail account
    GMAIL_PASSWORD = 'add pwd here'  #change this to match your gmail password





    if not is_similar(roadCopyImg, roadImg):
        sender = Emailer()
        image = '/home/pi/Images/finalDetection.jpg'
        sendTo = ''
        emailSubject = "Damaged Road - Pilani(Picam)"
        emailContent = "Please find the attachment for the damaged road pictures."   #+ time.ctime()
        sender.sendmail(sendTo, emailSubject, emailContent, image)
    else:
        print("No potholes detected")
    time.sleep(10)
cv2.waitKey(0)
cv2.destroyAllWindows()

