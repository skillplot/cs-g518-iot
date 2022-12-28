Road damage detection without comparision(i.e old image is not needed). </br>
Download the entire version2 onto your Raspberry pi. </br>
Connect to powerbank as the power source.
Only the <h3>potholeDetectPiCamSchedule</h3> needs to be executed on the raspberry pi. Other files are the alternate versions. </br>
potholeDetectionLocalImages uses local images instead of pi camera. So you can test damaged roads with local images(eg:downloaded from internet).</br>

The code is scheduled currently for every 30 seconds. This can be updated so every day after those many seconds specified in time, road will be examined.
 </br>Just run the file in terminal, and remove the HDMI cable.
 </br>Since the power is from powerbank, the raspberry pi would continue to work forever till the power is supplied to the powerbank.
