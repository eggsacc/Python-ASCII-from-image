import cv2
import numpy as np
import os

# update your folder directory
folderDir = r'C:\Users\{}]'

# adjust output width
max_width = 90

# adding more chars can improve reoslution!
ascii_char = ' .,-~:;=!*#$@' 

# filter by file extensions
def is_img(directory):
    extensions = ('.png', '.jpg', '.jpeg', '.bmp', '.gif', '.tiff')
    return directory.lower().endswith(extensions)

files = os.listdir(folderDir)
imges = [i for i in files if is_img(i)]

# create .txt file for each image
for item in imges:

    charOut = ""

    # convert image to grayscale
    img = cv2.imread(os.path.join(folderDir, item))
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # scale image to match screen width
    scaleFactor = max_width / imgGray.shape[1]
    nWidth = int(imgGray.shape[1] * scaleFactor)
    nHeight = int(imgGray.shape[0] * scaleFactor)
    imgScaled = cv2.resize(imgGray, (nWidth, nHeight))
    
    # assign ascii character based on brightness
    for row in range(nHeight):
        for clmn in range(nWidth):
            charOut += ascii_char[round(imgScaled[row][clmn] / 255 * (len(ascii_char) - 1))] + ' '
            
        # insert newline char after each row 
        charOut += '\n'

    # create .txt file with same name as image
    txt_filename = os.path.splitext(item)[0] + '.txt'
    txt_filepath = os.path.join(folderDir, txt_filename)
    
    with open(txt_filepath, 'w') as file:
        file.write(charOut)

print("Done")

    

    
