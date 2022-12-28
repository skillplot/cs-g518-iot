Pothole detection: An old image of the road is used to compare with a fresh image to find if potholes exists.
<br />
Components used:  <br />
Raspberry Pi <br />
Pi camera 5mp <br />
<br />
To download on your local machine and to test on the raspberry pi, Please follow below guidelines: <br />
<br />
Install libraries:  <br />
Numpy: pip install numpy  <br />
cv2:  pip install opencv-python  <br />
skimage: pip install scikit-image <br />
imutils: pip install imutils <br />
<br />
<b>diffCalculations.py</b> can be used to post damaged road images on twitter. Two images will be compared and the potholes will be highlighted with rectangular boxes. <br />
Update the access tokens and api keys before using it on raspberry pi.<br />
 <br />

<br />
<b>diffCalculationsWithEmail.py</b> This is same as above but local images are used to test the damage. i.e both the images are local and raspberry pi doesn't freshly capture any images in this library. Hence can be used just to test the libraries.

<h3>diffCal-Email-Picam.py</h3> the above file should be used to mail the damaged road images. Two images will be compared and the potholes will be highlighted with rectangular boxes. <br />
Please update the email id, password and reciever's email id.
You need to have an old image of the road or the current image of the road to detect future/existing potholes. Update the old image path in roadOld and new picture taken by Pi camera should go to roadNew variables.
Thonny has issues with installing skimage, so visual code studio can be used to run the above library.
