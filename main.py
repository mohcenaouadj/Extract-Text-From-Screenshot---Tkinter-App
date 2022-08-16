import cv2 as cv
import numpy as np
import pytesseract


image = cv.imread('Capture d’écran du 2022-08-14 18-51-43.png')

# get grayscale image
def get_grayscale(image):
    return cv.cvtColor(image, cv.COLOR_BGR2GRAY)


# noise removal
def remove_noise(image):
    return cv.medianBlur(image,5)
 
#thresholding
def thresholding(image):
    return cv.threshold(image, 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)[1]

gray = get_grayscale(image)
#noiseless = remove_noise(gray)
thresh = thresholding(gray)

custom_config = r'--oem 3 --psm 6'
text = pytesseract.image_to_string(thresh, config=custom_config)
print(text)
