import numpy as np
import cv2 as cv
import binascii
import time

#011011110011101000100 (don't remember what is it)

cap = cv.VideoCapture('test_cut.mp4')  # video from task

frame_count = 0
green_on = False
red_on = False
red_count = 0
cyclecount = 0
data = ''
while True:

    frame_count += 1
    #print(frame_count % 60)
    if frame_count > 172723:
        break
    #if frame_count > 50000:
    #    time.sleep(0.5)

    _, frame = cap.read()

    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    sensitivity_1 = 80


    lower_white_1 = np.array([0, 0, 255 - sensitivity_1])
    upper_white_1 = np.array([255, sensitivity_1, 255])
    mask_red = cv.inRange(hsv, lower_white_1, upper_white_1)

    res_red = cv.bitwise_and(frame, frame, mask=mask_red)

    sensitivity_2 = 80
    lower_white_2 = np.array([0, 0, 255 - sensitivity_2])
    upper_white_2 = np.array([255, sensitivity_2, 255])
    mask_green = cv.inRange(hsv, lower_white_2, upper_white_2)

    res_green = cv.bitwise_and(frame, frame, mask=mask_red)

    red_prev = red_on
    print(hsv[12][16])
    if hsv[11][35][2] < 220:
        red_on = False
    else:
        red_on = True
    if red_prev != red_on:
        red_count += 1
        if red_count == 2:
            red_count = 0
            # print('cycle red')
            cyclecount += 1
            data += str(int(green_on))
            #print(int(green_on))

    green_prev = green_on
    if hsv[12][16][2] < 220:
        green_on = False
    else:
        green_on = True

    #cv.imshow('frame', frame)
    #cv.imshow('red', mask_green)
    # cv.imshow('res',res)
    k = cv.waitKey(5) & 0xFF
    if k == 27:
        break
cv.destroyAllWindows()
print(data)
data = data[3:]

print(bytes(str(hex(int(str(data),2))[2:]), 'utf-8')[2:])
#print(binascii.unhexlify(bytes(str(hex(int(str(data),2))[2:]), 'utf-8')[2:]))


