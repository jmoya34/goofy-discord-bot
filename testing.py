import cv2
import json
var1 = 0

days_gone = 1000

img = cv2.imread('obama.jpg', cv2.IMREAD_ANYCOLOR)

if days_gone == 0:
    cv2.putText(img, "Days gone without", (215,300), cv2.FONT_HERSHEY_COMPLEX, 0.6, (0,0,0), 1)
    cv2.putText(img, "chocolate", (245,330), cv2.FONT_HERSHEY_COMPLEX, 0.6, (0,0,0), 1)
    cv2.putText(img, str(days_gone), (290,400), cv2.FONT_HERSHEY_COMPLEX, 1.0, (0,0,0), 1)
        
elif days_gone < 10:
    cv2.putText(img, "Days gone without", (215,300), cv2.FONT_HERSHEY_COMPLEX, 0.6, (0,0,0), 1)
    cv2.putText(img, "chocolate", (245,330), cv2.FONT_HERSHEY_COMPLEX, 0.6, (0,0,0), 1)
    cv2.putText(img, str(days_gone), (290,400), cv2.FONT_HERSHEY_COMPLEX, 1.0, (0,0,0), 1)

elif days_gone < 100:
    cv2.putText(img, "Days gone without", (215,300), cv2.FONT_HERSHEY_COMPLEX, 0.6, (0,0,0), 1)
    cv2.putText(img, "chocolate", (245,330), cv2.FONT_HERSHEY_COMPLEX, 0.6, (0,0,0), 1)
    cv2.putText(img, str(days_gone), (290,400), cv2.FONT_HERSHEY_COMPLEX, 1.0, (0,0,0), 1)

elif days_gone < 1000:
    cv2.putText(img, "Days gone without", (215,300), cv2.FONT_HERSHEY_COMPLEX, 0.6, (0,0,0), 1)
    cv2.putText(img, "chocolate", (245,330), cv2.FONT_HERSHEY_COMPLEX, 0.6, (0,0,0), 1)
    cv2.putText(img, str(days_gone), (290,400), cv2.FONT_HERSHEY_COMPLEX, 1.0, (0,0,0), 1)

elif days_gone < 10000:
    cv2.putText(img, "Days gone without", (215,300), cv2.FONT_HERSHEY_COMPLEX, 0.6, (0,0,0), 1)
    cv2.putText(img, "chocolate", (245,330), cv2.FONT_HERSHEY_COMPLEX, 0.6, (0,0,0), 1)
    cv2.putText(img, str(days_gone), (270,400), cv2.FONT_HERSHEY_COMPLEX, 1.0, (0,0,0), 1)

cv2.imwrite("output.png", img, [cv2.IMWRITE_PNG_COMPRESSION])