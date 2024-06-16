# ASCII from image
## How it works

Computers represent images as an array of numbers. A grayscale image is simply a 2D matrix of numbers that represent the brightness (0-255) of each pixel. An image in the RGB colorspace is slightly more complex and is a stack of red, green and blue pixel values in a 3D matrix.
<br></br>  
<img src="https://github.com/eggsacc/Python-ASCII-from-image/assets/128606148/b5b45001-6a95-4ec2-a608-3736d9c59ced" alt="RGB representation" width="500">
<br></br>

To convert an image to ASCII, we just need to convert it to grayscale and map the brightness of each pixel to a corresponding ASCII character.

The `OpenCV` python package is a powerful compter vision & image processing library, widely used for real-time processes and includes a ton of features. It is used here to obtain the image matrices, convert it to grayscale and scale the image.
<br></br>
> FYI, OpenCV converts RGB to grayscale by taking the weighted average of the 3 color chanels of each pixel. The formula is<br>**`Gray = 0.299·Blue + 0.587·Green + 0.114·Red`**</br>This is also referred to as the luminosity method, which accounts for humans perception as we are more sensitive to the color green as compared to red or blue.

<br></br>
The ASCII characters list here is `** .,-~:;=!*#$@ ]`, from lightest to darkest. The full ASCII grayscale sequence is `$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/|()1{}[]?-_+~<>i!lI;:,"^.`. You can add more intermediate characters in the original list to make the output more refined.
<br></br>

## How to use

1. Download the folder
2. Open `script.py` and update the folder path to `ascii_img` (copy from file explorer)
3. Drag images into the `ascii_img folder`
4. Run the python script, `.txt` files will be created in the same folder
<br></br>

## Doggo

![pexels-photo-1851164](https://github.com/eggsacc/Python-ASCII-from-image/assets/128606148/821fcb9b-b955-422b-83a4-baa6098e8dc8)
<br></br>
![image](https://github.com/eggsacc/Python-ASCII-from-image/assets/128606148/a8b793e4-64f8-46ae-ba2c-98d8ac3e4724)

