import cv2 as cv
import numpy as np
import os
os.chdir(r'C:\Users\Vinxe\Documents\Python\Python\Proyectos\images')

def resize(image):
    src = cv.imread(rf'C:\Users\Vinxe\Documents\Python\Proyectos\{image}', cv.IMREAD_GRAYSCALE)

    #percent by which the image is resized
    scale_percent = 50

    #calculate the 50 percent of original dimensions
    width = int(src.shape[1] * scale_percent / 100)
    height = int(src.shape[0] * scale_percent / 100)

    # dsize
    dsize = (width, height)

    # resize image
    output = cv.resize(src, dsize)

    cv.imwrite(rf'C:\Users\Vinxe\Documents\Python\Proyectos\{image}',output)  



img1 = cv.imread('Screenshot_8.png',cv.IMREAD_ANYCOLOR)
img2 = cv.imread('Screenshot_7.png', cv.IMREAD_ANYCOLOR)

result = cv.matchTemplate(img1, img2, cv.TM_CCOEFF_NORMED)


min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)

print ('best match top left position: %s' % str(max_loc))
print('Best match confidence: %s' % max_val)

threshold = 0.3
if max_val >= threshold:
    print('Food buff found')

    buff_w = img2.shape[1]
    buff_h = img2.shape[0]
    top_left = max_loc
    bottom_right = (top_left[0] + buff_w, top_left[1] + buff_h)

    cv.rectangle(img1, top_left, bottom_right,
                    color=(0,0,255), thickness=2, lineType=cv.LINE_4)
    
    cv.imshow('Result', img1)
    cv.waitKey()
else:
    print('Buff not found')