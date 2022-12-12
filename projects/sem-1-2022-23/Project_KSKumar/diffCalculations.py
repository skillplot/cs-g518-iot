#Please update the api and access token with actual keys


#packages import--> open cv
#imutils is an image processing package
import cv2          #Used to convert regular image to grayscale
import imutils      
import numpy as np
import skimage
from skimage.metrics import structural_similarity as ssim       #Facilitates in finding the differences between two grayscale images.
import tweepy
#tweepy allows to post tweets
#twython can also be used

#from skimage import measure
#skimage.metrics.structural_similarity.
#from skimage.metrics import structural_similarity as ssim
#Load images with paths
roadImgOld = cv2.imread("images/unaffected.jpg")
roadImgOld = cv2.resize(roadImgOld,(600,360))
roadImgNew = cv2.imread("images/affected.jpg")
roadImgNew = cv2.resize(roadImgNew,(600,360))

#Converting images to grayscale
roadImgOldGS = cv2.cvtColor(roadImgOld, cv2.COLOR_BGR2GRAY)
roadImgNewGS = cv2.cvtColor(roadImgNew, cv2.COLOR_BGR2GRAY)

#Mean structural similarity is fetched, if full is true, full structural similarity image is returned.
# Highlighting the damaged areas using absdiff

(similar,differences) = ssim(roadImgOldGS, roadImgNewGS, full=True)
#diff is in range of 0 to 1. Converting it to 0 - 255.
differences = (differences*255).astype("uint8")
#cv2.imshow("differences(img1, img2)",differences)

#Apply threshold --> cv2.threshoId(image, thresh _ pixel _ values,max pixel_values,type_of_threshold)
#Applies a fixed level threshold to each array element / to a multiple-Channel array. The method is used to get a bi-level (binary) image out ot a grayscale image 

thresholdImg = cv2.threshold(differences, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
#cv2.imshow( "Thresholded image" ,thresholdImg)
#Thresholding is the simplest method of segmenting images. From a grayscale image, thresholding can be used to create binary images.

# Find contours -  simply as a curve joining all the continuous points (along the boundary), having same color or intensity. The contours are a useful tool for shape analysis, object detection and recognition
contours = cv2.findContours(thresholdImg.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
contoursArr = imutils.grab_contours(contours)

# Loop over each contour
for contour in contoursArr:
    if cv2.contourArea(contour) > 5:
        # Calculate bounding box
        x, y, w, h =  cv2.boundingRect(contour)
        #Draw rectangle • bounding box. Highlights the desired aspect in an image.
        cv2. rectangle(roadImgOld, (x, y), (x+w, y+h), (0,0,255), 2)
        cv2. rectangle(roadImgNew, (x, y), (x+w, y+h), (0,0,255), 2)
        #cv2.putText(img2, str(similarity percent, (10,30), cv2.FONT_HERSHEY_SIMPLEX, .7, (0,0,255), 2)
                    
#Show differences
x = np.zeros((360,10,3), np.uint8)
                
#hstack is used to concatenate images horizontally
result = np.hstack((roadImgOld, x, roadImgNew))
cv2.imshow("Final differences",  result)

cv2.imwrite("images/differences.jpeg", result)
'''


# your twitter consumer and access information goes here
# note: these are garbage strings and won't work
apiKey = '**'
apiSecret = '**************'
accessToken = '*-ifWT5Mr********JIWO37RnjQMuvjaFkw'
accessTokenSecret = '***'
 # Upload image





#Donot use the method: api.update_status(status=tweetStr) #This is v1.1, Currently v2 is being used.
#response = api.create_tweet(text='Test Tweet IoT-2022', media_ids=[media.media_id])
'''
#Update these with actual keys
apiKey = '**'
apiSecret = '***'
accessToken = '***'
accessTokenSecret = '***G'

'''
client = tweepy.Client(consumer_key=apiKey,
auth = tweepy.OAuthHandler(apiKey, apiSecret)
auth.set_access_token(accessToken, accessTokenSecret) 
api = tweepy.API(auth)  # Upload image  
media = api.media_upload("images/cameraTest.jpg")
tweet = "Test Tweet IoT-2022 with Image" 
post_result = api.create_tweet(status=tweet, media_ids=[media.media_id])   
'''

auth = tweepy.OAuthHandler(apiKey, apiSecret)
auth.set_access_token(accessToken, accessTokenSecret) 

api = tweepy.API(auth)  # Upload image  
media = api.media_upload("images/differences.jpeg")

tweet = "*Please Ignore* Test Tweet IoT-2022 with Image" 
post_result = api.update_status(status=tweet, media_ids=[media.media_id])     #Please note, elevated access is needed to tweet with images
cv2.waitKey(0)
cv2.destroyAllWindows()
                    
