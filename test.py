import cv2 as cv

image = cv.imread('anz_1.png')

if image is not None:
    gray_image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)  
    cv.imwrite('gray_image.png', gray_image)            
    cv.imshow('Image', gray_image)
    cv.waitKey(0)
    cv.destroyAllWindows()
else:
    print("Failed to load image.")
