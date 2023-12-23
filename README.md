# PhotoDigitization
Digitize physical photo albums using OpenCV canny edge detection with a simple GUI. Tested on Python version 3.12.0.

# Steps
1. git clone repo
2. create virtualenv 
3. pip install -r requirements.txt
4. python3 gui.py

# Tuning
Can edit values in photo.py if edges are not detected properly in canny(). Might add this in future update into GUI.

# I/O
Currently only takes in .jpg and .png file types, will create a folder "Output" with labelled numbers according to selected photos. Try to use photos with edges as clear as possible, taking the photos as high quality without shadows.

# Easy use
Included a .exe for the lazy ones, should be able to work out of the box. 