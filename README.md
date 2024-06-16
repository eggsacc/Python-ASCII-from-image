# ASCII from image

## Dependencies

Enter `pip install opencv` in terminal to update / install OpenCV.
<br></br>
## How to use
> 2 sample images are included by default
> 
1. Download the folder
2. Open `script.py` and update the folder path to `ascii_img` (copy from file explorer)
3. Drag images into the `ascii_img folder`
4. Run the python script, `.txt` files will be created in the same folder
5. Open .txt files using Notepad (preferably)
6. Ctrl + scroll to adjust size of image
<br></br>

## Example

Doug            |  ASCII Doug
:-------------------------:|:-------------------------:
<img src="https://github.com/eggsacc/Python-ASCII-from-image/assets/128606148/44c61bb3-3e8c-4de0-ad62-d9d83c059fb5" width="500" height="500" /> |  <img src="https://github.com/eggsacc/Python-ASCII-from-image/assets/128606148/ebcfe814-d365-49ad-ad0d-a850b42fd313" width="500" height="500" />

<br></br>
## How it works

Computers represent images as an array of numbers. A grayscale image is simply a 2D matrix of numbers that represent the brightness (0-255) of each pixel. An image in the RGB colorspace is slightly more complex and is a stack of red, green and blue pixel values in a 3D matrix.
<br></br>  
RGB matrix (3D)            |  Grayscale matrix (2D)
:-------------------------:|:-------------------------:
<img src="https://github.com/eggsacc/Python-ASCII-from-image/assets/128606148/e1729a9a-771a-4044-a1a5-0b1fe81c6262" width="250" height="300" /> |  <img src="https://github.com/eggsacc/Python-ASCII-from-image/assets/128606148/bf39248c-36bd-4ecf-9d8f-f2735468a3d2" width="250" height="300" />

<br></br>
To convert an image to ASCII, we just need to convert it to grayscale and map the brightness of each pixel to a corresponding ASCII character. Different ASCII represents brightness by the amount of space it occupies. The character `@` and `#` are dense and representes darker pixels, while `,` and `'` are perceived as lighter pixels.

The `OpenCV` python package is a powerful compter vision & image processing library, widely used for real-time processes and includes a ton of features. It is used here to obtain the image matrices, convert it to grayscale and scale the image.

The ASCII characters list here is ` .,-~:;=!*#$@`, from lightest to darkest. The full ASCII grayscale sequence is `$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/|()1{}[]?-_+~<>i!lI;:,"^.`. You can add more intermediate characters in the original list to make the output more refined.
<br></br>
> FYI, OpenCV converts RGB to grayscale by taking the weighted average of the 3 color chanels of each pixel. The formula is<br>**`Gray = 0.299·Blue + 0.587·Green + 0.114·Red`**</br>This is also referred to as the luminosity method, which accounts for humans perception as we are more sensitive to the color green as compared to red or blue.





