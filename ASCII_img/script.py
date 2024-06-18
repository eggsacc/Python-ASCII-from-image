import cv2
import os

# Update your folder directory
folderDir = r'{directory}'

# Adjust output width
max_width = 90

# Characters list; adding more chars can improve reoslution!
ascii_char = ' .,-~:;=!*#$@' 

# Filter out image files
def is_img(directory):
    extensions = ('.png', '.jpg', '.jpeg', '.bmp', '.gif', '.tiff')
    return directory.lower().endswith(extensions)

files = os.listdir(folderDir)
imges = [i for i in files if is_img(i)]

# Scale image to match output width
def scaleIMG(img):
    scaleFactor = max_width / img.shape[1]
    nWidth = int(img.shape[1] * scaleFactor)
    nHeight = int(img.shape[0] * scaleFactor)
    imgScaled = cv2.resize(img, (nWidth, nHeight))
    return imgScaled

# Assign ASCII character based on pixel brightness
def charAssign(img):
    charOut = ''
    for row in range(img.shape[0]):
        for clmn in range(img.shape[1]):
            charOut += ascii_char[round(img[row][clmn] / 255 * (len(ascii_char) - 1))] + ' '  
        charOut += '\n'
    return charOut

# Create .txt file for each image
for item in imges:

    # Convert image to grayscale
    img = cv2.imread(os.path.join(folderDir, item))
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    scaledImg = scaleIMG(imgGray)
    ascii_output = charAssign(scaledImg)

    # .txt file created inherits img file name
    txt_filename = os.path.splitext(item)[0] + '.txt'
    txt_filepath = os.path.join(folderDir, txt_filename)
    
    with open(txt_filepath, 'w') as file:
        file.write(ascii_output)

print("Done!")

    

    
