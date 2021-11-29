import cv2
import pytesseract

img = cv2.imread('IMG.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
print(pytesseract.image_to_string(img))
cv2.imshow('Result', img)
cv2.waitKey(0)

# print("aok")