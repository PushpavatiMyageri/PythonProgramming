import cv2
import numpy as np

img = cv2.imread('C:/Users/User/Desktop/python_programs/Assignment/Assignment_folder/module_3/module_4/module_6/watch.jpg',cv2.IMREAD_COLOR)
cv2.imshow('image',img)
cv2.waitKey(0)
print("KILL")
cv2.destroyAllWindows()
