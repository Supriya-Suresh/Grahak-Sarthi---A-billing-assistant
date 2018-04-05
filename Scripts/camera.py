import cv2
def camera_image():
    cam = cv2.VideoCapture(1)
    s, im = cam.read()# captures image
    image_dir = r"C:\Users\sathish\Desktop\Veggie\tensorflow-for-poets-2\Images/Veg.jpg"
    cv2.imwrite(image_dir,im) # writes image in jpg format to folder Images
    cam.release()
    cv2.destroyAllWindows()
    return im
