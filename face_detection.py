import cv2
# capture frames from a camera or image
detect = cv2.CascadeClassifier("haarcascades/haarcascade_frontalface_default.xml")
#detect = cv2.CascadeClassifier("haarcascades/haarcascade_eye.xml")
#imp_img = cv2.VideoCapture("images\\moneyheist.jpg")

img = cv2.imread("images\moneyheist.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# detect faces of different sizes in input image
# we get four co-ordinates x,y,width and height in faces
faces = detect.detectMultiScale(gray, 1.1, 5) # grayscaleimage, resizing command
# (image,pti,pt2,color,thickness)
# pt1 = vertex of rectangle
# pt2= opposite vertex of pt1
for (x, y, w, h) in faces:
    final_img = cv2.rectangle(img, (x, y), (x+w, y+w), (255, 255, 0), 2)
# print my square box
#print(type(final_img))
#print(final_img)
#resized = cv2.resize(img, (int(img.shape[1]/2), int(img.shape[0]/2)))
cv2.imshow("Elon Image", img)

cv2.waitKey(0)
# img.release()  # release the camera in some milliseconds
cv2.destroyAllWindows()
