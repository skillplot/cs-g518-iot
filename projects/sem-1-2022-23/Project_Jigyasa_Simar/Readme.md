Project: BLIND ASSISTANCE SYSTEM

Follow steps:
1. First install opencv with python 3 using following link : https://pyimagesearch.com/2017/09/04/raspbian-stretch-install-opencv-3-python-on-your-raspberry-pi/
2. Download the files from "Project_Jigyasa_Simar" in a folder and add following folders and files to it:
    
    2.1. Create a folder named "trainer" which will store the trained model.
    
    2.2. Create a folder named "dataset" to store all the images of people.
    
    2.3. Create a file "names.txt" which will store the names of people captured before training.
3. Now you are good to go.
4. Open terminal and go to your environment using following 2 commands:
        
        source ~/.profile
        workon cv
5. Go to your project directory using "cd <project_directory_name>"
6. First start with capturing some new faces in your dataset using command:
        
        python face_dataset.py
   It will automatically train the model after capturing the images. 
7. Now run following command to finally start detecting faces:
        
        python 03_face_recognition.py
   
